# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round B - Problem C. Robot Path Decoding
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83dc
#
# Time:  O(N)
# Space: O(N)
#

def robot_path_decoding():
    P = raw_input().strip()

    i = dx = dy = d = 0
    stk = []
    while i < len(P):
        if P[i].isalpha():
            dx, dy, d = (dx+DIR[P[i]][0])%MOD, (dy+DIR[P[i]][1])%MOD, 0
        elif P[i].isdigit():
            d = 10*d+int(P[i])
        elif P[i] == '(':
            stk.append((dx, dy, d))
            dx = dy = d = 0
        elif P[i] == ')':
            prev_dx, prev_dy, d = stk.pop()
            dx, dy, d = (prev_dx+d*dx)%MOD, (prev_dy+d*dy)%MOD, 0
        i += 1
    return "%s %s" % (dx+1, dy+1)

DIR = {'E':(1, 0), 'S':(0, 1), 'W':(-1, 0), 'N':(0, -1)}
MOD = 10**9
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, robot_path_decoding())
