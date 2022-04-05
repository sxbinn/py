import turtle as t

t.screensize(canvwidth=800, canvheight=1200)
t.shape('turtle')
s=int(input('속도를 입력하세요: '))
t.speed(s)

t.penup()
t.goto(-250,250)

def strips(color):
    t.color(color)
    t.begin_fill()
    for i in range(2):
        t.forward(500)
        t.right(90)
        t.forward(20)
        t.right(90)
    t.end_fill()
    t.right(90)
    t.forward(20)
    t.left(90)

def moon(x,y,size):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color('#ffcc24')
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    t.penup()
    t.goto(x+size/4,y-3.3+size/4)
    t.pendown()
    t.color('#020075')
    t.begin_fill()
    t.circle(45)
    t.end_fill()

def star():
    t.left(4)
    t.color('#ffcc24')
    t.begin_fill()
    for i in range(14):
        t.forward(30)
        t.right(162)
        t.forward(30)
        t.left(136.2857)
    t.end_fill()

for rine in range(7):
    strips('#cc0000')
    strips('white')
t.goto(-250,250)
t.begin_fill()
t.color('#020075')

for blue in range(2):
    t.forward(270)
    t.right(90)
    t.forward(160)
    t.right(90)
t.end_fill()
moon(-160,117,55)
t.goto(-65,184)
star()
t.clearscreen()