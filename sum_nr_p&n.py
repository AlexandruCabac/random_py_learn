from random import randint
n=int(input())
sp,sn=0,0
while n>0:
    x=randint(-50,50)
    if(x<0):
        sn+=x
    else:
        sp+=x
    n-=1
print("Spoz ",sp)
print("Sneg ",sn)