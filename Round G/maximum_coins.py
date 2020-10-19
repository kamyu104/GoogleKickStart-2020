# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round G - Problem B. Maximum Coins
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414a23
#
# Time:  O(N^2)
# Space: O(1)
#

def sum_diag(C, i, j):
    total = 0
    while i < len(C) and j < len(C[0]):
        total += C[i][j]
        i += 1
        j += 1
    return total

def maximum_coins():
    N = input()
    C = [map(int, raw_input().strip().split()) for _ in xrange(N)]

    result = 0
    for i in xrange(len(C)):
        result = max(result, sum_diag(C, i, 0))
    for j in xrange(1, len(C[0])):
        result = max(result, sum_diag(C, 0, j))
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, maximum_coins())
