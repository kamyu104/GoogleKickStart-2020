# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round F - Problem D. Yeehtzee
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f4dea
#
# Time:  O(M * states), states = sum(partition(i) for i in [0..K])
# Space: O(M * states)
#

def memoization(A, curr, lookup):
    if tuple(curr) not in lookup:
        count, total = float(len(curr)), 0
        left = 0
        while left < len(curr):
            right = left
            while right+1 < len(curr) and curr[right+1] == curr[left]:
                right += 1
            if curr[right]+1 <= A[right]:
                curr[right] += 1
                count += memoization(A, curr, lookup)*(right-left+1)
                curr[right] -= 1
                total += right-left+1
            left = right+1
        lookup[tuple(curr)] = count/total
    return lookup[tuple(curr)]

def yeehtzee():
    N, M, K = map(int, raw_input().strip().split())
    A = [0]*(M-K)
    for _ in xrange(K):
        A.append(input())
    return memoization(A, [0]*M, {tuple(A):0.0})

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, yeehtzee())
