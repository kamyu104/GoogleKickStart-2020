# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round H - Problem B. Boring Numbers
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043b0c6
#
# Time:  O(logR)
# Space: O(1)
#

def f(x):
    digits = map(int, list(str(x)))  # abcdefg
    result = 0
    base = 5**(len(digits)-1)
    is_prefix_valid = True
    for i, digit in enumerate(digits):
        if is_prefix_valid:
            result += (digit+i%2)//2 * base  # ab?xxxx
            if i%2 == digit%2:
                is_prefix_valid = False
        result += base  # 000xxxx
        base //= 5
    if is_prefix_valid:
        result += 1
    return result

def boring_numbers():
    L, R = map(int, raw_input().strip().split())
    return f(R)-f(L-1)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, boring_numbers())
