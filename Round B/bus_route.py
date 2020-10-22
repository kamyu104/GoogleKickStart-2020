from math import gcd
t=int(input())

def solve(T):
    routes,days=list(map(int,input().split()))
    journey=list(map(int,input().split()))
    sol=(days//journey[routes-1])*journey[routes-1]
    for i in [v for v in range(routes-1)][::-1]:
        if journey[i+1]%journey[i]==0: continue
        else:
            sol=(sol//journey[i])*journey[i]
    print("Case #{}: {}".format(T,sol))
for test_case in range(1,t+1):
    solve(test_case)