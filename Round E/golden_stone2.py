# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round E - Problem D. Golden Stone
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bef29
#
# Time:  O((N * S + M * S + R * N) * log(N * S))
# Space: O(N * S + M)
#

from heapq import heappush, heappop

def golden_stone():
    N, M, S, R = map(int, raw_input().strip().split())
    adj = [[] for _ in xrange(N)]  # Space: O(N + M)
    for _ in xrange(M):
        U, V = map(lambda x: int(x)-1, raw_input().strip().split())
        adj[U].append(V)
        adj[V].append(U)
    C = [map(lambda x: int(x)-1, raw_input().strip().split()[1:]) for _ in xrange(N)]
    recipes = []
    recipe_adj = [[] for _ in xrange(S)]  # Space: O(S + K * R) = O(S + 3 * R)
    for r in xrange(R):
        recipes.append(map(lambda x: int(x)-1, raw_input().strip().split())[1:])
        for s in recipes[-1]:
            recipe_adj[s].append(r)
    stone_dist = [[INF for _ in xrange(S)] for _ in xrange(N)]  # Space: O(N * S)
    min_heap = []  # Space: O(N * S)
    for u in xrange(N):
        for s in C[u]:
            stone_dist[u][s] = 0
            heappush(min_heap, (0, u, s))
    lookup = [[False for _ in xrange(S)] for _ in xrange(N)]  # Space: O(N * S)
    while min_heap:
        d, u, s = heappop(min_heap)
        if lookup[u][s]:
            continue
        lookup[u][s] = True
        for v in adj[u]:  # Time: O((|V| + |E|) * log|V|) = O((N * S + M * S) * log(N * S))
            if lookup[v][s]:
                continue
            nd = d+1
            if nd < stone_dist[v][s]:
                stone_dist[v][s] = nd
                heappush(min_heap, (nd, v, s))
        for r in recipe_adj[s]:  # Time: O(K * R * N * log|V|) = O(3 * R * N * log(N * S))
            r = recipes[r]
            if lookup[u][r[-1]]:
                continue
            nd = sum(stone_dist[u][r[i]] for i in xrange(len(r)-1))
            if nd < stone_dist[u][r[-1]]:
                stone_dist[u][r[-1]] = nd
                heappush(min_heap, (nd, u, r[-1]))
    result = min(stone_dist[u][0] for u in xrange(N))
    return result if result < INF else -1

INF = 10**12
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, golden_stone())
