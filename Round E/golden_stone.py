# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round E - Problem D. Golden Stone
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bef29
#
# Time:  O((N * S + M * S + R * N) * log(N * S))
# Space: O(N * S + N * R + M)
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
    recipe_count = [0]*R
    recipe_adj = [[] for _ in xrange(S)]  # Space: O(S + K * R) = O(S + 3 * R)
    recipe_out = [0]*R
    for r in xrange(R):
        recipe = map(lambda x: int(x)-1, raw_input().strip().split())[1:]
        recipe_out[r] = recipe.pop()
        for s in recipe:
            recipe_adj[s].append(r)
        recipe_count[r] = len(recipe)

    stone_dist = [[INF for _ in xrange(S)] for _ in xrange(N)]  # Space: O(N * S)
    min_heap = []  # Space: O(N * S)
    for u in xrange(N):
        for s in C[u]:
            stone_dist[u][s] = 0
            heappush(min_heap, (0, u, s))
    recipe_dist = [[[0, 0] for _ in xrange(R)] for _ in xrange(N)]  # Space: O(N * R)
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
            if lookup[u][recipe_out[r]]:
                continue
            recipe_dist[u][r][0] += 1
            recipe_dist[u][r][1] += d
            if recipe_dist[u][r][0] == recipe_count[r]:  # able to apply recipe
                nd = recipe_dist[u][r][1]
                if nd < stone_dist[u][recipe_out[r]]:
                    stone_dist[u][recipe_out[r]] = nd
                    heappush(min_heap, (nd, u, recipe_out[r]))
    result = min(stone_dist[u][0] for u in xrange(N))
    return result if result < INF else -1

INF = 10**12
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, golden_stone())
