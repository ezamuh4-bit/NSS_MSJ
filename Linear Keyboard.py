n=int(input())
for i in range(n):
    n1=input()
    n2=input()
    c=0
    for i in range(1,len(n2)):
        c+=abs(n1.index(n2[i])-n1.index(n2[i-1]))
    
    print (c)
