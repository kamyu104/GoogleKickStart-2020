# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2020 Round D - Problem D. Locked Doors
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000386d5c
#
# Time:  O(NlogN + QlogN), pass in PyPy2 but Python2
# Space: O(N)
#

from functools import partial

# Template:
# https://github.com/kamyu104/GoogleCodeJam-2020/blob/master/Round%202/emacs++2_concise.py
class TreeInfos(object):  # Time: O(NlogN), Space: O(NlogN), N is the number of nodes
    def __init__(self, root, children):
        def preprocess(curr, parent):
            D[curr] = 1 if parent == -1 else D[parent]+1  # depth of the node i
            if parent != -1:
                P[curr].append(parent)  # ancestors of the node i
            i = 0
            while i < len(P[curr]):
                if i < len(P[P[curr][i]]):
                    P[curr].append(P[P[curr][i]][i])
                i += 1
            C[0] += 1
            L[curr] = C[0]  # the subtree of the node i is represented by traversal index L[i]..R[i]

        def divide(curr, parent):
            stk.append(partial(postprocess, curr))
            for child in reversed(children[curr]):
                if child == -1:
                    continue
                stk.append(partial(divide, child, curr))
            stk.append(partial(preprocess, curr, parent))

        def postprocess(curr):
            R[curr] = C[0]  # the subtree of the node i is represented by traversal index L[i]..R[i]

        N = len(children)
        L, R, D, P, C = [0]*N, [0]*N, [0]*N, [[] for _ in xrange(N)], [-1]
        stk = []
        stk.append(partial(divide, root, -1))
        while stk:
            stk.pop()()
        assert(C[0] == N-1)
        self.L, self.R, self.D, self.P = L, R, D, P

    def size(self, curr):
        return self.R[curr]-self.L[curr]+1
    
    def binary_lift(self, a, k):  # Time: O(logN)
        if self.size(a) >= k:
            return a 
        for i in reversed(xrange(len(self.P[a]))):  # O(logN)
            if i < len(self.P[a]) and self.size(self.P[a][i]) < k:
                a = self.P[a][i]
        assert(self.P[a] and self.size(self.P[a][0]) >= k)
        return self.P[a][0]

# Template:
# https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/maximum-binary-tree.py
def build_cartesian_tree(nums):  # Time: O(N), Space: O(N)
    decreasing_stk = []
    children = [[-1, -1] for _ in xrange(len(nums))]
    for i, num in enumerate(nums):
        while decreasing_stk and nums[decreasing_stk[-1]] < num:
            children[i][0] = decreasing_stk.pop()
        if decreasing_stk:
            children[decreasing_stk[-1]][1] = i
        decreasing_stk.append(i)
    return decreasing_stk[0], children

def locked_doors():
    N, Q = map(int, raw_input().strip().split())
    D = map(int, raw_input().strip().split())

    root, children = build_cartesian_tree(D)  # Time: O(N)
    tree_infos = TreeInfos(root, children)    # Time: O(NlogN)
    result = []
    for _ in xrange(Q):                       # Time: O(QlogN)
        S, K = map(int, raw_input().strip().split())
        if K == 1:
            result.append(S)
            continue
        K -= 1
        X = S-1 if S == N or (S > 1 and D[(S-1)-1] < D[S-1]) else S
        Y = tree_infos.binary_lift(X-1, K)+1  # Time: O(logN)
        if X == Y:
            result.append(S-K if X == S-1 else S+K)
        else:
            result.append(Y+(K-tree_infos.size(children[Y-1][0])) if X < Y else Y+1-(K-tree_infos.size(children[Y-1][1])))
    return " ".join(map(str, result))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, locked_doors())
