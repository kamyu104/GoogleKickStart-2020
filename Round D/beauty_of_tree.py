# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2020 Round D - Problem C. Beauty of Truee
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000386edd
#
# Time:  O(N)
# Space: O(N)
#

from itertools import izip
from functools import partial

def iter_dfs(adj, A, B):
    def divide(A, B, curr, d, stk, A_prefix, B_prefix, A_cnt, B_cnt):
        prev_A_cnt, prev_B_cnt = [0], [0]
        stk.append(partial(postprocess, A, B, curr, d, A_prefix, B_prefix, prev_A_cnt, prev_B_cnt, A_cnt, B_cnt))
        for node in reversed(adj[curr]):
            stk.append(partial(divide, A, B, node, d+1, stk, A_prefix, B_prefix, A_cnt, B_cnt))
        stk.append(partial(preprocess, A, B, d, prev_A_cnt, prev_B_cnt, A_prefix, B_prefix))

    def preprocess(A, B, d, prev_A_cnt, prev_B_cnt, A_prefix, B_prefix):
        prev_A_cnt[0] = A_prefix[d%A]
        prev_B_cnt[0] = B_prefix[d%B]
        A_prefix[d%A] += 1
        B_prefix[d%B] += 1

    def postprocess(A, B, curr, d, A_prefix, B_prefix, prev_A_cnt, prev_B_cnt, A_cnt, B_cnt):
        A_cnt[curr] = A_prefix[d%A]-prev_A_cnt[0]
        B_cnt[curr] = B_prefix[d%B]-prev_B_cnt[0]

    A_prefix, B_prefix, A_cnt, B_cnt = [0]*len(adj), [0]*len(adj), [0]*len(adj), [0]*len(adj)
    stk = []
    stk.append(partial(divide, A, B, 0, 0, stk, A_prefix, B_prefix, A_cnt, B_cnt))
    while stk:
        stk.pop()()
    return A_cnt, B_cnt

def beauty_of_tree():
    N, A, B = map(int, raw_input().strip().split())
    adj = [[] for _ in xrange(N)]
    for i, p in enumerate(map(int, raw_input().strip().split()), 1):
        adj[p-1].append(i)
    return float(sum((a+b)*N - a*b for a, b in izip(*iter_dfs(adj, A, B))))/N/N

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, beauty_of_tree())
