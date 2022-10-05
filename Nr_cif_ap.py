from random import randint
a=randint(0,999999999)
v=[0,0,0,0,0,0,0,0,0,0]
while a>0:
    v[a%10]+=1
    a//=10
for i in range(0,10):
    print("Cifra ",i," se repeta de ",v[i]," ori")