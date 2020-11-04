# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round F - Problem C. Painter's Duel
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f47fb
#
# Time:  O(2^(S^2))
# Space: O(2^(S^2))
#

def id(R, P):
    return (R-1)**2+P-1

def valid(S, R, P, visited_mask):
    return 1 <= R <= S and 1 <= P <= 2*R-1 and not (visited_mask & (1<<id(R, P)))

def neighbors(S, R, P, visited_mask):
    result = []
    if valid(S, R, P-1, visited_mask):
        result.append((R, P-1))
    if valid(S, R, P+1, visited_mask):
        result.append((R, P+1))
    if P%2:
        if valid(S, R+1, P+1, visited_mask):
            result.append((R+1, P+1))
    else:
        if valid(S, R-1, P-1, visited_mask):
            result.append((R-1, P-1))
    return result

def maxmin(S, is_max, RA, PA, RB, PB, visited_mask, can_a_move, can_b_move, lookup, alpha, beta):
    if not can_a_move and not can_b_move:  # terminated state
        return 0
    if (is_max, RA, PA, RB, PB, visited_mask) not in lookup:  # memoization
        if is_max:
            max_score = float("-inf")
            moves = neighbors(S, RA, PA, visited_mask)
            if not moves:
                max_score = maxmin(S, not is_max, RA, PA, RB, PB, visited_mask, False, can_b_move, lookup, alpha, beta)
            else:
                for R, P in moves:
                    max_score = max(max_score, 1+maxmin(S, not is_max, R, P, RB, PB, visited_mask|(1<<id(R, P)), can_a_move, can_b_move, lookup, alpha, beta))
                    alpha = max(alpha, max_score)
                    if (-1+alpha) >= beta:  # alpha beta pruning, since it can not update parent's beta anymore
                        break
            lookup[is_max, RA, PA, RB, PB, visited_mask] = max_score
        else:
            min_score = float("inf")
            moves = neighbors(S, RB, PB, visited_mask)
            if not moves:
                min_score = maxmin(S, not is_max, RA, PA, RB, PB, visited_mask, can_a_move, False, lookup, alpha, beta)
            else:
                for R, P in moves:
                    min_score = min(min_score, -1+maxmin(S, not is_max, RA, PA, R, P, visited_mask|(1<<id(R, P)), can_a_move, can_b_move, lookup, alpha, beta))
                    beta = min(beta, min_score)
                    if (1+beta) <= alpha:  # alpha beta pruning, since it can not update parent's alpha anymore
                        break
            lookup[is_max, RA, PA, RB, PB, visited_mask] = min_score
    return lookup[is_max, RA, PA, RB, PB, visited_mask]

def painters_duel():
    S, RA, PA, RB, PB, C = map(int, raw_input().strip().split())
    visited_mask = 0
    for _ in xrange(C):
        R, P = map(int, raw_input().strip().split())
        visited_mask |= 1<<id(R, P)
    visited_mask |= 1<<id(RA, PA)
    visited_mask |= 1<<id(RB, PB)
    return maxmin(S, True, RA, PA, RB, PB, visited_mask, True, True, {}, float("-inf"), float("inf"))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, painters_duel())
