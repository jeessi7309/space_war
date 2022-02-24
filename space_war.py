from microbit import*
import random
a=0
b=0
c=0
d=0
e=2
x=0
y=0
z=0
t=0
q=0
r=0
zeit=1500
h=0
level=0
while True:
    h+=1
    if zeit>=300 and h//20:
        zeit=zeit-30
    if h//20==0:
        h=0
        level=level+1

    q+=1
    if q>=1:
        x=4
    if q>=2:
        y=4
    if q>=3:
        z=4
    if q>=4:
        t=4
    for i in range(5):
        if button_b.get_presses():
            e+=1
            if e==5:
                e=4
        if button_a.get_presses():
            e-=1
            if e==-1:
                e=0
        display.clear()
        display.set_pixel(a,0,x)
        sleep(10)
        display.set_pixel(b,1,y)
        display.set_pixel(c,2,z)
        display.set_pixel(d,3,t)
        display.set_pixel(d,3,t)
        display.set_pixel(e,4,9)

    if r==e:
        display.scroll("Game Over")
        display.scroll("Level "+ str(level))
    r=d
    d=c
    c=b
    b=a

    a=random.randint(0,4)
    sleep(zeit)

