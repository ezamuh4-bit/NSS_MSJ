n, x= map (int, raw_input().split())
c=0
for i in range (n):
    d=input()
    if d+x>=0:
        x+=d
    else:
        c+=1
print x,c
