import turtle as t

t.screensize(canvwidth=800, canvheight=1200)
t.shape('turtle')
t.pensize(1)
s=int(input('속도를 입력하세요: '))
t.speed(s)

t.penup()
t.goto(-559,316)

t.color('#B22234')
t.pendown()

for i in range(0,13,2):
     t.begin_fill()
     t.goto(559,316-48.5*i)
     t.goto(559,316-48.5*(1+i))
     t.goto(-559,316-48.5*(1+i))
     t.goto(-559,316-48.5*i)
     t.end_fill()
     t.penup()
     t.goto(-559,316-48.6*(2+i%13))
     t.pendown()

t.penup()
t.goto(-559,316)
t.pendown()
t.color('#3C3B62')
t.begin_fill()
t.goto(-559+8.5*52,316)
t.goto(-559+8.5*52,316-48.5*7)
t.goto(-559,316-48.5*7)
t.goto(-559,316)
t.end_fill()

def draw_star(r):
    t.setheading(0)
    t.pendown()
    t.color('white')
    t.begin_fill()
    for i in range(5):
        t.forward(r)
        t.right(360*2//5)
    t.end_fill()
    t.penup()

def star(n):
    for i in range(n):
        t.pendown()
        draw_star(30)
        t.penup()
        t.setheading(0)
        t.forward(r*2+10)

def star_6(x,m):
    t.penup()
    t.goto(-559+r,316-(x)*r-(m))
    star(6)

def star_5(x,m):
    t.penup()
    t.goto(-559+r*2+5,316-(x)*r-(m))
    star(5)

r=30

star_6(1,0)
star_5(2,4)

star_6(3,8)
star_5(4,12)

star_6(5,16)
star_5(6,20)

star_6(7,24)
star_5(8,28)

star_6(9,32)

t.hideturtle()
t.clearscreen()