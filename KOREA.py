import turtle as t
import math as m

t.screensize(canvwidth=800, canvheight=1200)
t.shape('turtle')
s=int(input('속도를 입력하세요: '))
t.speed(s)

t.won=m.asin(3/m.sqrt(13))*180/m.pi
t.won_b=m.asin(2/m.sqrt(13))*180/m.pi

t.penup()
t.goto(0,-200)
t.circle(200,t.won)

t.color('red')
t.pendown()
t.begin_fill()
t.circle(200,180)
t.end_fill()
t.penup()

t.color('blue')
t.pendown()
t.begin_fill()
t.circle(200,180)
t.circle(100,180)
t.end_fill()

t.color('red')
t.begin_fill()
t.circle(-100,180)
t.end_fill()
t.penup()

def long ():
    t.right(90)
    t.pendown()
    t.begin_fill()
    t.forward(100)
    t.left(90)
    t.forward(400/12)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(400/12)
    t.left(90)
    t.forward(100)
    t.end_fill()
    t.penup()

def short ():
    t.right(90)
    t.forward(400/48)
    t.pendown()
    t.begin_fill()
    t.forward(100-400/48)
    t.left(90)
    t.forward(400/12)
    t.left(90)
    t.forward(100-400/48)
    t.left(90)
    t.forward(400/12)
    t.end_fill()
    t.penup()

    t.right(90)
    t.forward(400/48*2)
    t.right(90)
    t.pendown()
    t.begin_fill()
    t.forward(400/12)
    t.left(90)
    t.forward(100-400/48)
    t.left(90)
    t.forward(400/12)
    t.left(90)
    t.forward(100-400/48)
    t.end_fill()
    t.penup()

t.color('black')
t.left(90)
t.forward(100)
long()

t.left(90)
t.forward(400/12+400/24)
long()

t.left(90)
t.forward(400/12+400/24)
long()

t.goto(0,0)
t.setheading(180+t.won_b)
t.forward(300)
long()

t.left(90)
t.forward(400/12+400/24)
short()

t.forward(400/48)
t.left(90)
t.forward(400/12+400/24)
long()

t.goto(0,0)
t.setheading(-t.won_b)
t.forward(300)
short()

t.goto(0,0)
t.setheading(-t.won_b)
t.forward(300+400/12+400/24)
short()

t.goto(0,0)
t.setheading(-t.won_b)
t.forward(300+400/12*2+400/24*2)
short()

t.goto(0,0)
t.setheading(t.won_b)
t.forward(300)
short()

t.forward(400/48)
t.left(90)
t.forward(400/12+400/24)
long()

t.goto(0,0)
t.setheading(t.won_b)
t.forward(300+400/12*2+400/24*2)
short()
t.hideturtle()
t.clearscreen()