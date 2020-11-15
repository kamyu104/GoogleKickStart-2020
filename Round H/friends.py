# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round H - Problem D. Friends
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043aee7
#
# Time:  O(A^3 + A^2 * (N + Q)) = O(N + Q) since O(A) = O(26), pass in PyPy2 but Python2
# Space: O(N * A + A^2)
#
# if A is much smaller than L, this solution would be better
#

def floyd_warshall(dist):
     for k in xrange(len(dist)):
        for i in xrange(len(dist)):
            for j in xrange(len(dist[0])):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

def friends():
    N, Q = map(int, raw_input().strip().split())
    S = raw_input().strip().split()

    masks = [0]*N
    dist = [[0 if i == j else INF for j in xrange(ALPHA_SIZE)] for i in xrange(ALPHA_SIZE)]
    for k, s in enumerate(S):  # Time: O(A^2 * N)
        mask_i = masks[k] = reduce(lambda x, y: x|y, (1<<(ord(c)-ord('A')) for c in s))
        while mask_i:
            i = LOG[mask_i & -mask_i]
            mask_j = masks[k]
            while mask_j:
                j = LOG[mask_j & -mask_j]
                if i != j:
                    dist[i][j] = 1
                mask_j -= mask_j & -mask_j
            mask_i -= mask_i & -mask_i
    floyd_warshall(dist)  # Time: O(A^3)
    result = []
    for _ in xrange(Q):  # Time: O(A^2 * Q)
        X, Y = map(int, raw_input().strip().split())
        X -= 1
        Y -= 1
        result.append(INF)
        mask_i = masks[X]
        while mask_i:
            i = LOG[mask_i & -mask_i]
            mask_j = masks[Y]
            while mask_j:
                j = LOG[mask_j & -mask_j]
                result[-1] = min(result[-1], dist[i][j]+2)
                mask_j -= mask_j & -mask_j
            mask_i -= mask_i & -mask_i
        if result[-1] >= INF:
            result[-1] = -1
    return " ".join(map(str, result))

ALPHA_SIZE = 26
INF = ALPHA_SIZE+1
LOG, base = {}, 1
for i in xrange(ALPHA_SIZE):
    LOG[base] = i
    base <<= 1
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, friends())
