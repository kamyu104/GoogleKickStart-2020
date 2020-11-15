# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round G - Problem B. Boring Numbers
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043b0c6
#
# Time:  O(logR)
# Space: O(1)
#

def f(x):
    digits = map(int, list(str(x)))  # abcdefg
    base = 5**(len(digits)-1)
    result = (5*base-5)//(5-1)  # count 0xxxxxx, 00xxxxx, 000xxxx, ..., 000000x => (5^len(digits)-5)/(5-1)
    for i, digit in enumerate(digits, 1):
        result += (digit+1-i%2)//2 * base  # count ab?xxxx
        if i%2 != digit%2:
            break
        base //= 5
    else:
        result += 1  # count abcdefg
    return result

def boring_numbers():
    L, R = map(int, raw_input().strip().split())
    return f(R)-f(L-1)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, boring_numbers())
