# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round C - Problem B. Stable Wall
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003379bb
#
# Time:  O(R * C)
# Space: O(1)
#

def dfs(adj, node, lookup, result):
    lookup[node] = VISITING
    for child in adj[node]:
        if child not in lookup:
            if not dfs(adj, child, lookup, result):
                return False
        elif lookup[child] == VISITING:  # circular dependency
            return False
    lookup[node] = VISITED
    result.append(node)
    return True

def stable_wall():
    R, C = map(int, raw_input().strip().split())
    adj = {}
    row = [[0]*C for _ in xrange(2)]
    for i in xrange(R):
        row[i%2] = list(raw_input().strip())
        for x in row[i%2]:
            adj.setdefault(x, set())
        if not i:
            continue
        for j, x in enumerate(row[(i-1)%2]):
            if x != row[i%2][j]: 
                adj[x].add(row[i%2][j])
    result, lookup = [], {}
    for x in adj.iterkeys():
        if x in lookup:
            continue
        if not dfs(adj, x, lookup, result):
            return -1
    return "".join(result)

VISITING, VISITED = range(2)
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, stable_wall())
