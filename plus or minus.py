n=input()
for i in range(n):
    a,b,c =map(int,raw_input().split())
    if a+b==c:
        print "+"
    else:
        print "-"
