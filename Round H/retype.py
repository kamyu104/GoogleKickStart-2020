# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round G - Problem A. Retype
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043adc7
#
# Time:  O(1)
# Space: O(1)
#

def retype():
    N, K, S = map(int, raw_input().strip().split())
    return (K-1) + min((K-S)+(N-S+1), 1+N)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, retype())
