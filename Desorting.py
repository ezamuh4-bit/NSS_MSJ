n=input()
for i in range (n):
    ld=[]
    n1=input()
    l1=list(map(int,raw_input().split()))
    for i in range (1,len(l1)):
        ld.append(l1[i]-l1[i-1])
    x1=0
    x2=min(ld)
    x3=x2
    c=0
    #print x2
    '''
    while x2>=x1:
        x2-=1
        x1+=1
        c+=1
    '''
    if x2>=0:
        print x2/2 +1
    else:
        print 0
