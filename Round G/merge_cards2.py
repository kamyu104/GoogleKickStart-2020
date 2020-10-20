# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round G - Problem D. Merge Cards
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000415054
#
# Time:  O(N^2), if we can neglate precomputing time  O(MAX_N^2), it's O(N)
# Space: O(N^2), if we can neglate precomputing space O(MAX_N^2), it's O(1)
#
# this solution is optimized from merge_cards.py
#

def merge_cards():
    N = input()
    A = map(int, raw_input().strip().split())
    return sum(a*dp[N][min(i, N-1-i)] for i, a in enumerate(A))

MAX_N = 5000
dp = [[0.0]*((MAX_N+1)//2) for _ in xrange(MAX_N+1)]  # dp[i][j]: expected count of (j+1)-th cards with total i cards 
for i in xrange(2, MAX_N+1):  # precompute
    for j in xrange((i+1)//2):  # dp[i] is symmetric since dp[i][j] = dp[i][i-1-j], we can only precompute left part of dp[i] to save more time
        if j > 0:
            dp[i][j] += ((j-1)-1+1)*dp[i-1][min(j-1, (i-2)-(j-1))]   # merge any of (0,1)~(j-2,j-1), count j with ev(i-1, j-1)
            dp[i][j] += 1.0 + dp[i-1][min(j-1, (i-2)-(j-1))]         # merge (j-1,j), count j with 1 + ev(i-1, j-1)
        if j < i-1:
            dp[i][j] += 1.0 + dp[i-1][min(j, (i-2)-j)]               # merge (j,j+1), count j with 1 + ev(i-1, j)
            dp[i][j] += ((i-1)-(j+2)+1)*dp[i-1][min(j, (i-2)-j)]     # merge any of (j+1,j+2)~(i-2,i-1), count j with ev(i-1, j)
        dp[i][j] /= (i-1)  # (i-1) choices in i cards

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, merge_cards())
