n=input()
d2=0
d1=list(map(int, raw_input().split()))
x=d1.index(max(d1))
d1.reverse()
y=d1.index(min(d1))
if x > n-y-1:
    d2=-1
print x+y+d2
