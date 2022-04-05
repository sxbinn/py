import turtle as t

t.screensize(canvwidth=800, canvheight=1200)
t.shape('turtle')
t.pensize(1)
s=int(input('속도를 입력하세요: '))
t.speed(s)

t.penup()
t.goto(-400, 250)
t.pendown()

def rectangle(color):
    t.color(color)
    t.begin_fill()
    t.forward(800)
    t.right(90)
    t.forward(167)
    t.right(90)
    t.forward(800)
    t.end_fill()

rectangle('#FF9933')

t.penup()
t.left(90)
t.forward(167)
t.left(90)
t.pendown()

rectangle('#138808')

def circle(n,color):
    t.penup()
    t.goto(0,n)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(n)
    t.end_fill()

circle(70,'#000080')
circle(60,'white')

t.penup()
t.goto(7,-57)
t.pendown()
t.color('#000080')
for i in range(24):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
    t.forward(15)
    t.right(15)
    t.pendown()

circle(15,'#000080')

t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(2)
for i in range(24):
    t.forward(60)
    t.backward(60)
    t.left(15)
t.clearscreen()