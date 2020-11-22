# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round A - Problem B. Plates
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d40bb
#
# Time:  O(N * P * K)
# Space: O(P)
#

def plates():
    N, K, P = map(int, raw_input().strip().split())
    stks = [map(int, raw_input().strip().split()) for _ in xrange(N)]
    prefixes = []  
    for stk in stks:
        prefix = [0]
        for x in stk:
            prefix.append(prefix[-1] + x)
        prefixes.append(prefix)

    dp = [0]*(P+1)  # dp[j] = max sum of beauty values with j plates
    for i in xrange(N):
        new_dp = [0]*(P+1)
        for j in xrange(P+1):
            for p in xrange(min(j, K)+1):
                new_dp[j] = max(new_dp[j], dp[j-p] + prefixes[i][p])
        dp = new_dp
    return dp[-1]

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, plates())
