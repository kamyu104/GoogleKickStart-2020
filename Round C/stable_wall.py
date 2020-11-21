# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round C - Problem B. Stable Wall
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003379bb
#
# Time:  O(R * C)
# Space: O(1)
#

from collections import defaultdict

def dfs(adj, node, curr, lookup, result):
    lookup.add(node)
    curr.add(node)
    for child in adj[node]:
        if child in curr:
            return False
        if child in lookup:
            continue
        if not dfs(adj, child, curr, lookup, result):
            return False
    curr.remove(node)
    result.append(node)
    return True

def stable_wall():
    R, C = map(int, raw_input().strip().split())
    adj = defaultdict(set)
    row = [[0]*C for _ in xrange(2)]
    for i in xrange(R):
        row[i%2] = list(raw_input().strip())
        for x in row[i%2]:
            adj[x]
        if not i:
            continue
        for j, x in enumerate(row[(i-1)%2]):
            if x != row[i%2][j]: 
                adj[x].add(row[i%2][j])
    result, lookup = [], set()
    for x in adj.iterkeys():
        if x in lookup:
            continue
        if not dfs(adj, x, set(), lookup, result):
            return -1
    return "".join(result)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, stable_wall())
