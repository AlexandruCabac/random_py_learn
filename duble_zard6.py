from random import randint
a=0
def arunc():
    return randint(1,6)
while(a==0):
    b=arunc()
    if(b==arunc()):
        print(2*b)
        a=1