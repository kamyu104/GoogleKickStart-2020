# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round G - Problem A. Kick Start
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414bfb
#
# Time:  O(N)
# Space: O(1)
#

def kick_start():
    S = raw_input().strip()

    result = count = 0
    for i in xrange(len(S)-len(START)+1):
        if S[i:i+len(KICK)] == KICK:
            count += 1
        elif S[i:i+len(START)] == START:
            result += count
    return result

KICK = "KICK"
START = "START"
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, kick_start())
