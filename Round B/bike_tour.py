t=int(input())

def solve(T):
    sol=0
    number=int(input())
    checkpoints=list(map(int,input().split()))
    for i in range(1,number-1):
        if checkpoints[i]>checkpoints[i-1] and checkpoints[i]>checkpoints[i+1]: 
            sol+=1
    print("Case #{}: {}".format(T,sol))

for test_case in range(1,t+1):
    solve(test_case)