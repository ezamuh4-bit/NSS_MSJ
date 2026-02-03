n=int(input())
for i in range(n):
    n2=int(input())
    n3=list(map(int,input().split()))
    if n3[n2-1]==0:
        print("NO")
    elif n3[n3[n2-1]-1]==0:
        print ("NO")
    else:
        print ("YES")
