d1,d2,d3=map(int,input().split())
if d1+d2<d3 :
    print (2*(d1+d2))
elif d1+d3<d2:
    print (2*(d1+d3))
elif d3+d2<d1:
    print (2*(d3+d2))
else:
    print (d1+d2+d3)
