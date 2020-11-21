# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round B - Problem A. Bike Tour
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d82e6
#
# Time:  O(N)
# Space: O(1)
#

def bike_tour():
    N = input()
    H = map(int, raw_input().strip().split())

    result = 0
    for i in xrange(1, len(H)-1):
        if H[i-1] < H[i] > H[i+1]:
            result += 1
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, bike_tour())
