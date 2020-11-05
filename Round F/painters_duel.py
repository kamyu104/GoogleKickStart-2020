# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round F - Problem C. Painter's Duel
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f47fb
#
# Time:  O(2^(S^2))
# Space: O(2^(S^2))
#

def pos(r, p):
    return 1<<((r-1)**2+p-1)

def valid(S, r, p):
    return 1 <= r <= S and 1 <= p <= 2*r-1

def neighbors(S, r, p):
    if valid(S, r, p-1): yield (r, p-1)
    if valid(S, r, p+1): yield (r, p+1)
    if p%2 == 1 and valid(S, r+1, p+1): yield (r+1, p+1)
    if p%2 == 0 and valid(S, r-1, p-1): yield (r-1, p-1)

def maxmin(S, is_max, ra, pa, rb, pb, visited_mask, can_a_move, can_b_move, lookup, alpha, beta):
    if not can_a_move and not can_b_move:  # terminated state
        return 0
    if (ra, pa, rb, pb, visited_mask) not in lookup:  # memoization
        if is_max:
            max_score = float("-inf")
            for r, p in neighbors(S, ra, pa):
                if visited_mask & pos(r, p):
                    continue
                max_score = max(max_score, 1+maxmin(S, not is_max, r, p, rb, pb, visited_mask|(pos(r, p)), can_a_move, can_b_move, lookup, alpha, beta))
                alpha = max(alpha, max_score)
                if (-1+alpha) >= beta:  # alpha beta pruning, since it can not update parent's beta anymore
                    break
            if max_score == float("-inf"):
                max_score = maxmin(S, not is_max, ra, pa, rb, pb, visited_mask, False, can_b_move, lookup, alpha, beta)
            lookup[ra, pa, rb, pb, visited_mask] = max_score
        else:
            min_score = float("inf")
            for r, p in neighbors(S, rb, pb):
                if visited_mask & pos(r, p):
                    continue
                min_score = min(min_score, -1+maxmin(S, not is_max, ra, pa, r, p, visited_mask|(pos(r, p)), can_a_move, can_b_move, lookup, alpha, beta))
                beta = min(beta, min_score)
                if (1+beta) <= alpha:  # alpha beta pruning, since it can not update parent's alpha anymore
                    break
            if min_score == float("inf"):
                min_score = maxmin(S, not is_max, ra, pa, rb, pb, visited_mask, can_a_move, False, lookup, alpha, beta)
            lookup[ra, pa, rb, pb, visited_mask] = min_score
    return lookup[ra, pa, rb, pb, visited_mask]

def painters_duel():
    S, RA, PA, RB, PB, C = map(int, raw_input().strip().split())
    visited_mask = pos(RA, PA) | pos(RB, PB)
    for _ in xrange(C):
        R, P = map(int, raw_input().strip().split())
        visited_mask |= pos(R, P)
    return maxmin(S, True, RA, PA, RB, PB, visited_mask, True, True, {}, float("-inf"), float("inf"))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, painters_duel())
