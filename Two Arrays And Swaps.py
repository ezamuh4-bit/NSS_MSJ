t=input()
for i in range (t):
    n,k=map(int,raw_input().split())
    a=list(map(int,raw_input().split()))
    b=list(map(int,raw_input().split()))
    for i in range (k):
      if min(a)<max(b):
       a[a.index(min(a))]=b[b.index(max(b))]
       b[b.index(max(b))]=a[a.index(min(a))]
    print (sum(a))
