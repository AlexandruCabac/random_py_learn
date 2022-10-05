from random import randint
n,m,s,c=int(input()),0,0,0
while (n>0):
    b=int(input)
    s+=b
    if(b>m):
        m=b
        c=0
    if(b==m):
        c+=1
    print(b,"  ",s)
    n-=1
s-=m*c
print(s)