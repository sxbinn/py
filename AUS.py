import turtle as t

t.screensize(canvwidth=800, canvheight=1200)
t.shape('turtle')
s=int(input('속도를 입력하세요: '))
t.speed(s)

def rectangle(X,Y,length,width,clr):
    t.up()
    t.goto(X,Y)
    t.color(clr)
    t.begin_fill()
    for i in range (2):
        t.forward(length)
        t.right(90)
        t.forward(width)
        t.right(90)
    t.end_fill()

def star(X1,Y1,size,points,clr):
    t.goto(X1,Y1)
    t.color(clr)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.left(180-180/points)
    t.end_fill()

rectangle(-200,100,400,200,'#00247D')
star(-130,-65,50,7,'white')
star(100,-60,25,7,'white')
star(100,60,25,7,'white')
star(20,10,25,7,'white')
star(150,20,25,7,'white')
t.right(35)
star(120,-10,15,5,'white')

t.setheading(27)
rectangle(-210,0,240,20,'white')

t.setheading(27)
rectangle(-210,-10,240,5,'#CF142B')

t.setheading(-27)
rectangle(-210,110,240,20,'white')
t.stamp()

t.setheading(-27)
rectangle(-210,100,240,5,'#CF142B')

t.setheading(0)
rectangle(-200,60,200,40,'white')

t.setheading(0)
rectangle(-120,100,40,120,'white')

t.setheading(0)
rectangle(-110,100,20,120,'#CF142B')
rectangle(-200,50,200,20,'#CF142B')

rectangle(-220,110,20,200,'white')

rectangle(-200,-10,210,10,'#00247D')

t.setheading(180)

rectangle(20,-30,30,130,'#00247D')
t.clearscreen()
