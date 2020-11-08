# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round E - Problem B. High Buildings
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bef73
#
# Time:  O(N)
# Space: O(N)
#

def high_buildings():
    N, A, B, C = map(int, raw_input().strip().split())
    if not (A+B-C <= N and (N == 1 or A+B-C > 1)):
        return "IMPOSSIBLE"
    
    result = [N-1]*(A-C) + [N]*C + [N-1]*(B-C)
    result = result[:1] + [N-2]*(N-(A+B-C)) + result[1:]  # if N <= 2, N-(A+B-C) = 0
    return " ".join(map(str, result))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, high_buildings())
