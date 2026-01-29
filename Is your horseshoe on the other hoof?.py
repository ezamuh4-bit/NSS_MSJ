d1=map(int, raw_input().split())
c1=0
for i in d1:
  c=d1.count(i)
  c1+=c
if c1==16:
      print 3
elif c1==10 or c1==8:
      print 2
elif c1==6:
      print 1
else:
      print 0
