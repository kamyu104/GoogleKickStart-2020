# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round C - Problem C. Perfect Subarray
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003381cb
#
# Time:  O(N * sqrt(N * MAX_A)), pass in PyPy2 but Python2
# Space: O(N * MAX_A)
#

def perfect_subarray():
    N = input()
    A = map(int, raw_input().strip().split())

    max_prefix, min_prefix, prefix = 0, 0, 0
    for x in A:
        prefix += x
        min_prefix = min(min_prefix, prefix)
        max_prefix = max(max_prefix, prefix)

    result, prefix = 0, 0
    count = [0]*(max_prefix-min_prefix+1)
    count[prefix-min_prefix] += 1
    for x in A:
        prefix += x
        i = 0
        while i*i <= prefix-min_prefix:
            result += count[(prefix-min_prefix)-i*i]
            i += 1
        count[prefix-min_prefix] += 1 
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, perfect_subarray())
