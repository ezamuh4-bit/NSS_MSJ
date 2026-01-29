n=input()
for i in range (n):
    c=0
    d=input()
    d1=list(map(int, raw_input().split()))
    d1.sort()
    for i in range(1,d):
        c+=(d1[i]-d1[i-1])
    print c
