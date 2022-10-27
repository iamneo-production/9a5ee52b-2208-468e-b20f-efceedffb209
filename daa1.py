n=int(input())
m=int(input())
x=[]
b=[]
t=1
for i in range(0,n):
    x.append(0)
for j in range (0,n):
    a=list(map(int,input("enter adj matrix").strip().split()))
    b.append(a)
def mco(k):
    while t==1:
        nxt(k)
        if x[k]==0:
            return
        if k==n:
            print(x)
        else:
            mco(k+1)
def nxt(k):
    while t==1:
        x[k]=(x[k]+1)%(m+1)
        if x[k]==0:
            return
        for j in range(1,n):
            if b[i][j]!=0 and x[k]==x[j]:
                break
        if j==n+1:
            return
mco(0)            
