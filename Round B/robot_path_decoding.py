from operator import mul
from functools import reduce 

bdr=10**9
t=int(input())
d={'N':-1,'S':1,'E':1,"W":-1} 
nums=set([str(i) for i in range(10)]) 

def solve(T): 
    sol=[1,1] 
    array=list(input())
    multipliyers=[1]
    while len(array)!=0:
        mult=reduce(mul, multipliyers, 1)
        top=array.pop(0)
        if top=='N' or top=='S': 
            sol[1]+=d[top]*mult
        if top=='E' or top=='W':
            sol[0]+=d[top]*mult
        if top in nums:
            multipliyers.append(int(top))
            array.pop(0) 
        if top==')': 
            multipliyers.pop(-1)
    
    if sol[0]<1 or sol[0]>bdr: 
        sol[0]=sol[0]%bdr
        if sol[0]==0:
            sol[0]=bdr

    if sol[1]<1 or sol[1]>bdr:
        sol[1]=sol[1]%bdr
        if sol[1]==0:
            sol[1]=bdr

    print("Case #{}: {} {}".format(T,sol[0], sol[1]))

for test_case in range(1,t+1):
    solve(test_case)