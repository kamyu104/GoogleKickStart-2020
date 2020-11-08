# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round E - Problem D. Golden Stone
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bef29
#
# Time:  O((N * S + M * S + R * N) * log(N * S))
# Space: O(N * S + M * S)
#

from heapq import heappush, heappop

def golden_stone():
    N, M, S, R = map(int, raw_input().strip().split())
    adj = [set() for _ in xrange(N)]
    for _ in xrange(M):
        U, V = map(int, raw_input().strip().split())
        U -= 1
        V -= 1
        adj[U].add(V)
        adj[V].add(U)
    C = [map(lambda x: int(x)-1, raw_input().strip().split()[1:]) for _ in xrange(N)]
    R = [map(lambda x: int(x)-1, raw_input().strip().split()[1:]) for _ in xrange(R)]

    cost = [[INF for _ in xrange(S)] for _ in xrange(N)]
    min_heap = []
    for u in xrange(N):
        for s in C[u]:
            cost[u][s] = 0
            heappush(min_heap, (0, u, s))
    lookup = [[False for _ in xrange(S)] for _ in xrange(N)]
    while min_heap:
        _, u, s = heappop(min_heap)
        if lookup[u][s]:
            continue
        lookup[u][s] = True
        for v in adj[u]:  # Time: O((|V| + |E|) * log|V|) = O((N * S + M * S) * log(N * S))
            if lookup[v][s]:
                continue
            new_cost = cost[u][s]+1
            if new_cost < cost[v][s]:
                cost[v][s] = new_cost
                heappush(min_heap, (new_cost, v, s))
        for r in R:  # Time: O(R * N * log|V|) = O(R * N * log(N * S))
            if lookup[u][r[-1]]:
                continue
            new_cost = sum(cost[u][r[i]] for i in xrange(len(r)-1))  # Time: O(K) = O(3)
            if new_cost < cost[u][r[-1]]:
                cost[u][r[-1]] = new_cost
                heappush(min_heap, (new_cost, u, r[-1]))
    result = min(cost[u][0] for u in xrange(N))
    return result if result < INF else -1

INF = 10**12
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, golden_stone())
