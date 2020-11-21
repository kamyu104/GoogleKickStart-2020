# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round C - Problem D. Candies
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/0000000000337b4d
#
# Time:  O(N + QlogN)
# Space: O(N)
#

class BIT(object):  # 1-indexed.
    def __init__(self, nums, M):  # Time: O(N)
        self.__bit = [0]*(len(nums)+1)  # Extra one for dummy node.
        for i in xrange(1, len(self.__bit)):
            sign = 1 if i%2 == 1 else -1
            self.__bit[i] = sign*nums[i-1]*(i if M else 1) + self.__bit[i-1]
        for i in reversed(xrange(1, len(self.__bit))):
            self.__bit[i] -= self.__bit[i-(i&-i)]

    def add(self, i, val):  # Time: O(logN)
        while i < len(self.__bit):
            self.__bit[i] += val
            i += (i & -i)

    def query(self, i):  # Time: O(logN)
        ret = 0
        while i > 0:
            ret += self.__bit[i]
            i -= (i & -i)
        return ret

def update(A, T, MT, i, v):
    diff = v-A[i]
    sign = 1 if i%2 == 0 else -1
    T.add(i+1, sign*diff)
    MT.add(i+1, sign*diff*(i+1))
    A[i] = v

def range_sum(bit, l, r):
    return bit.query(r)-bit.query(l-1)

def candies():
    N, Q = map(int, raw_input().strip().split())
    A = map(int, raw_input().strip().split())

    T, MT = BIT(A, False), BIT(A, True)
    result = 0
    for _ in xrange(Q):
        o, a, b = raw_input().strip().split()
        if o == 'U':
            x, v = int(a)-1, int(b)
            update(A, T, MT, x, v)
            continue
        l, r = int(a), int(b)
        sign = 1 if (l-1)%2 == 0 else -1
        result += sign*(range_sum(MT, l, r) - (l-1)*range_sum(T, l, r))
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, candies())
