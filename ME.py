import turtle as t

t.screensize(canvwidth=800, canvheight=1200)
t.shape('turtle')
s=int(input('속도를 입력하세요: '))
t.speed(s)

def rectangle(X,Y,length,width,clr):
    t.penup()
    t.goto(X,Y)
    t.color(clr)
    t.begin_fill()
    for i in range (2):
        t.forward(length)
        t.right(90)
        t.forward(width)
        t.right(90)
    t.end_fill()

rectangle(-350,200,700,400,'black')
rectangle(-350,125,75,250,'white')
rectangle(-250,125,500,250,'white')
rectangle(275,125,75,250,'white')

t.color('white')

def rine(X,Y):
    t.penup()
    t.goto(X,Y)
    for i in range(13):
        t.pensize(30)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(45)
        t.pendown()

rine(-330,162.5)
rine(-330,-162.5)
t.penup()

t.goto(0,0)
t.pendown()
t.color('pink')
t.width(1)
COLORS = ['red','orange','yellow','green','blue','navy','purple','gray']

for color in COLORS:
    t.fillcolor(color)
    t.begin_fill()
    t.circle(60)
    t.circle(55, -360)
    t.circle(50)
    t.circle(45, -360)
    t.end_fill()
    t.right(45)
t.hideturtle()
t.clearscreen()