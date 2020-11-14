# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2020 Round D - Problem B. Alien Piano
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000387174
#
# Time:  O(K)
# Space: O(1)
#

def alien_piano():
    K = input()
    A = map(int, raw_input().strip().split())

    result = inc_cnt = dec_cnt = 0
    for i in xrange(1, len(A)):
        if A[i] > A[i-1]:
            inc_cnt += 1
            dec_cnt = 0
        elif A[i] < A[i-1]:
            dec_cnt += 1
            inc_cnt = 0
        else:
            continue
        if inc_cnt == MAX_KEY_NUM or dec_cnt == MAX_KEY_NUM:
            result += 1
            inc_cnt = dec_cnt = 0
    return result

MAX_KEY_NUM = 4
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, alien_piano())
