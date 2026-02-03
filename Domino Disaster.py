n=int(input())
for i in range(n):
    n1=int(input())
    n2=input()
    s=""
    for i in n2:
        if i=="U":
            s=s+"D"
        elif i=="D":
            s=s+"U"
        else:
            s=s+i
    print (s)
