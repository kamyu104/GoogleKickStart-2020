# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round H - Problem D. Friends
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043b027
#
# Time:  O(A^3 + L^2 * (N + Q)) = O(N + Q) since O(A) = O(26), O(L) = O(20), pass in PyPy2 but Python2
# Space: O(A^2) = O(1)
#

def floyd_warshall(dist):
     for k in xrange(len(dist)):
        for i in xrange(len(dist)):
            for j in xrange(len(dist[0])):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

def friends():
    N, Q = map(int, raw_input().strip().split())
    S = raw_input().strip().split()

    dist = [[0 if i == j else INF for j in xrange(MAX_ALPHA)] for i in xrange(MAX_ALPHA)]
    for k, s in enumerate(S):  # Time: O(L^2 * N)
        for i in s:
            for j in s:
                if i == j:
                    continue
                dist[ord(i)-ord('A')][ord(j)-ord('A')] = 1
    floyd_warshall(dist)  # Time: O(A^3)
    result = []
    for _ in xrange(Q):  # Time: O(L^2 * Q)
        X, Y = map(int, raw_input().strip().split())
        X -= 1
        Y -= 1
        result.append(INF)
        for i in S[X]:
            for j in S[Y]:
                result[-1] = min(result[-1], dist[ord(i)-ord('A')][ord(j)-ord('A')]+2)
        if result[-1] >= INF:
            result[-1] = -1
    return " ".join(map(str, result))

MAX_ALPHA = 26
INF = MAX_ALPHA+1
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, friends())
