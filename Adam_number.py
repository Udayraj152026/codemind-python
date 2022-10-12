n=int(input())
t=n**2
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
s=rev*rev
rev1=0
while s>0:
    r=s%10
    rev1=rev1*10+r
    s=s//10
print(rev1==t)
    