# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round E - Problem A. High Buildings
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bef73
#
# Time:  O(N)
# Space: O(N)
#

def high_buildings():
    N, A, B, C = map(int, raw_input().strip().split())
    if A+B-C > N or (N > 1 and A+B-C <= 1):
        return "IMPOSSIBLE"
    
    result = [N-1]*(A-C) + [N]*C + [N-1]*(B-C)
    if N-2 >= 1:
        result = result[:1] + [N-2]*(N-(A+B-C)) + result[1:]
    return " ".join(map(str, result))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, high_buildings())
