# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round F - Problem A. ATM Queue
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f4ed8
#
# Time:  O(NlogN)
# Space: O(N)
#

def atm_queue():
    N, X = map(int, raw_input().strip().split())
    A = map(int, raw_input().strip().split())
    return " ".join(map(lambda x:str(x), [x for _, x, in sorted(((x-1)//X+1, i) for i, x in enumerate(A, 1))]))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, atm_queue())
