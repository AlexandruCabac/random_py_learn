from random import randint
n,s=int(input()),0
while n>0:
    x=randint(1,6)
    if(x==6):
        s+=1
    print(x)
    n-=1
print("6 a cazut de ",s," ori")