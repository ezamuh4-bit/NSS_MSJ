n=int(input())
l=list(map(int,input().split()))
s,d=0,0
for i in range(n):
    if l[0]>=l[-1]:
        ma=l[0]
        l.pop(0)
    else:
        ma=l[-1]
        l.pop(-1)
    if i%2==0:
        s+=ma
    else:
        d+=ma
print(s,d)
