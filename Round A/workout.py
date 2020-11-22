# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round A - Problem C. Workout
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f5b
#
# Time:  O(Nlog(MAX_DIFF))
# Space: O(1)
#

def check(M, K, target):
    count = 0
    for i in xrange(1, len(M)):
        count += ((M[i]-M[i-1])-1)//target  # ceiling(diff/target)-1
        if count > K:
            return False
    return True

def workout():
    N, K = map(int, raw_input().strip().split())
    M = map(int, raw_input().strip().split())

    left, right = 1, max(M[i]-M[i-1] for i in xrange(1, len(M)))
    while left <= right:
        mid = left + (right-left)//2
        if check(M, K, mid):
            right = mid-1
        else:
            left =mid+1
    return left

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, workout())
