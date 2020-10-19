# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round G - Problem D. Merge Cards
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000415054
#
# Time:  O(N), neglating precomputing time  O(N^2)
# Space: O(1), neglating precomputing space O(N^2)
#

def merge_cards():
    N = input()
    A = map(int, raw_input().strip().split())
    return sum(a*dp[N][i] for i, a in enumerate(A))

MAX_N = 5000
dp = [[0.0]*MAX_N for _ in xrange(MAX_N+1)]  # dp[i][j]: expected count of (j+1)-th cards with total i cards 
for i in xrange(2, MAX_N+1):  # precompute
    for j in xrange(i):
        if j > 0:
            dp[i][j] += ((j-1)-1+1)*dp[i-1][j-1]    # merge any of (0,1)~(j-2,j-1), count j with ev(i-1, j-1)
            dp[i][j] += 1.0 + dp[i-1][j-1]          # merge (j-1,j), count j with 1 + ev(i-1, j-1)
        if j < i-1:
            dp[i][j] += 1.0 + dp[i-1][j]            # merge (j,j+1), count j with 1 + ev(i-1, j)
            dp[i][j] += ((i-1)-(j+2)+1)*dp[i-1][j]  # merge any of (j+1,j+2)~(i-2,i-1), count j with ev(i-1, j)
        dp[i][j] /= (i-1)  # (i-1) choices in i cards

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, merge_cards())
