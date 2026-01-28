B=input()
for I in range (B):
    n,m=map(int,raw_input().split())
    Alpha=raw_input()
    A="ABCDEFG"
    b=Alpha
    b1=0
    for i in range (m):
        for j in range(len(A)):
            if A[j] in b :
                b=b.replace(A[j],"",1)
            else:
                b1+=1
    print b1
    del n,m, A, b1,i,j,b
