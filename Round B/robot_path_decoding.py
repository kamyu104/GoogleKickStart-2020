# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round B - Problem C. Robot Path Decoding
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83dc
#
# Time:  O(N)
# Space: O(N)
#

from sys import setrecursionlimit

def parse(P, i):
    if i[0] == len(P):
        return 0, 0
    if P[i[0]] == ')':
        i[0] += 1
        return 0, 0
    elif P[i[0]].isalpha():
        dx, dy = DIR[P[i[0]]]
        i[0] += 1
    elif P[i[0]].isdigit():
        d = int(P[i[0]])
        i[0] += 2  # moving extra 1 step is for '('
        dx, dy = parse(P, i)
        dx, dy = (d*dx)%MOD, (d*dy)%MOD
    dx2, dy2 = parse(P, i)
    return (dx+dx2)%MOD, (dy+dy2)%MOD

def robot_path_decoding():
    P = raw_input().strip()

    return "%s %s" % tuple(map(lambda x:x+1, parse(P, [0])))

BASE = 3
MAX_P_LENGTH = 2000
setrecursionlimit(BASE+MAX_P_LENGTH)
DIR = {'E':(1, 0), 'S':(0, 1), 'W':(-1, 0), 'N':(0, -1)}
MOD = 10**9
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, robot_path_decoding())
