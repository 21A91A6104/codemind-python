n=int(input())
for i in range(n):
    t=int(input())
    li=list(map(int,input().split()))
    p=sorted(li)
    if li==p:
        print("0")
        break
    else:
        q=p[-1]-p[0]
        print(q)
        
    