# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round E - Problem C. Toys
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bede9
#
# Time:  O(NlogN)
# Space: O(N)
#

from heapq import heappush, heappop

def toys():
    N = input()
    toys = [map(int, raw_input().strip().split()) for _ in xrange(N)]

    max_time = curr_time = total = sum(e for e, _ in toys)
    max_remove, remove = 0, 0
    max_heap = []
    for i, (e, r) in enumerate(toys):
        curr_time += e
        heappush(max_heap, (-(e+r), i))
        while max_heap and -max_heap[0][0] > total:
            e = toys[heappop(max_heap)[1]][0]
            total -= e
            curr_time -= 2*e
            remove += 1
        if curr_time > max_time:
            max_time = curr_time
            max_remove = remove
    if not max_heap:
        return "%s %s" % (max_remove, max_time)
    return "%s %s" % (remove, "INDEFINITELY")

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, toys())
