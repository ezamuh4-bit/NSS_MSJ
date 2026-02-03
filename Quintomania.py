n=int(input())
for i in range(n):
    b1=1
    n1=int(input())
    n2=list(map(int, input().split()))
    for i in range(1,n1):
        b=abs((n2[i])-n2[i-1])
        if b==7 or b==5:
            continue
        else:
            print ('NO')
            b1=0
            break
    if b1==1:
        print("YES")
