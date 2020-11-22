# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round A - Problem A. Alloction
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f56
#
# Time:  O(N)
# Space: O(MAX_A)
#

# Template:
# https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/special-array-with-x-elements-greater-than-or-equal-x.py
def inplace_counting_sort(nums):  # Time: O(n), Space: O(max_num)
    count = [0]*(max(nums)+1)
    for num in nums:
        count[num] += 1
    for i in xrange(1, len(count)):
        count[i] += count[i-1]
    for i in reversed(xrange(len(nums))):  # inplace but unstable sort
        if nums[i] < 0:  # processed
            continue
        while i != count[nums[i]]-1:
            count[nums[i]] -= 1
            nums[count[nums[i]]], nums[i] = ~nums[i], nums[count[nums[i]]]
        count[nums[i]] -= 1
        nums[i] = ~nums[i]
    for i in xrange(len(nums)):
        nums[i] = ~nums[i]  # restore values

def allocation():
    N, B = map(int, raw_input().strip().split())
    A = map(int, raw_input().strip().split())

    inplace_counting_sort(A)
    result = 0
    for x in A:
        if B < x:
            break
        B -= x
        result += 1
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, allocation())
