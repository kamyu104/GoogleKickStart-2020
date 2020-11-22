# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round A - Problem D. Bundling
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3ff3
#
# Time:  O(N * L), L is the average length of strings
# Space: O(T), T is the size of trie
#

from collections import defaultdict
from functools import reduce

def iter_dfs(K, node):
    result = 0
    stk = [(1, (node, 0))]
    while stk:
        step, params = stk.pop()
        if step == 1:
            node, depth = params
            if "_count" not in node:
                node["_count"] = 0
            stk.append((2, (node, depth)))
            stk.extend(((1, (child, depth+1)) for k, child in node.iteritems() if k != "_count"))  
        elif step == 2:
            node, depth = params
            node["_count"] += sum(child["_count"] for k, child in node.iteritems() if k != "_count")
            q, node["_count"] = divmod(node["_count"], K)
            result += q*depth
    return result

def bundling():
    N, K = map(int, raw_input().strip().split())

    _trie = lambda: defaultdict(_trie)
    trie = _trie()
    for _ in xrange(N):
        s = raw_input().strip()
        node = reduce(dict.__getitem__, s, trie)
        if "_count" not in node:
            node["_count"] = 0
        node["_count"] += 1    
    return iter_dfs(K, trie)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, bundling())
