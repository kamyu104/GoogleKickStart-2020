t= int(int(input()))
def solve(T):
    size,budget=list(map(int,input().split())) 
    sol=0
    array=list(map(int,input().split()))
    array.sort()
    for i in range(size):
        if array[i]<=budget:
            budget-=array[i]
            sol+=1 
        else:
            break
    print("Case #{}: {}".format(T,sol))

for i in range(1,t+1):
    solve(i)