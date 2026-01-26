n=input()
c=raw_input()
p=str(c[0])
for i in range(1,len(c)):
    if c[i]!= p[len(p)-1]:
        p=p+c[i]
print len(c)-len(p)
