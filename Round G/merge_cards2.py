# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round G - Problem D. Merge Cards
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000415054
#
# Time:  ctor:    O(MAX_N^2)
#        runtime: O(N)
# Space: ctor:    O(MAX_N^2)
#        runtime: O(1)
#
# this solution is optimized from merge_cards.py
#

def merge_cards():
    N = input()
    A = map(int, raw_input().strip().split())
    return sum(a*dp[N-1][min(i, (N-1)-i)] for i, a in enumerate(A))

MAX_N = 5000
dp = [[0.0]*((MAX_N+1)//2) for _ in xrange(MAX_N)]  # dp[i][j]: expected count of the (j+1)th card in total i+1 cards
for i in xrange(1, MAX_N):  # precompute
    for j in xrange(((i+1)+1)//2):  # dp[i] is symmetric since dp[i][j] = dp[i][i-j], we can only precompute left part of dp[i] to save more time
        if j-1 >= 0:
            dp[i][j] += ((j-1)-1+1)*dp[i-1][min(j-1, (i-1)-(j-1))]  # merge any of (0,1)~(j-2,j-1), count j with EV(i-1, j-1)
            dp[i][j] += 1.0 + dp[i-1][min(j-1, (i-1)-(j-1))]        # merge (j-1,j), count j with 1 + EV(i-1, j-1)
        if j <= i-1:
            dp[i][j] += 1.0 + dp[i-1][min(j, (i-1)-j)]              # merge (j,j+1), count j with 1 + EV(i-1, j)
            dp[i][j] += (i-(j+2)+1)*dp[i-1][min(j, (i-1)-j)]        # merge any of (j+1,j+2)~(i-1,i), count j with EV(i-1, j)
        dp[i][j] /= i  # i choices in i+1 cards

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, merge_cards())
