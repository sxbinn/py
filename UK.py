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
        t.fd(length)
        t.right(90)
        t.fd(width)
        t.right(90)
    t.end_fill()

rectangle(-300,150,600,300,'#00247D')

t.setheading(27)
rectangle(-310,-130,750,60,'white')
t.setheading(27)
rectangle(-290,-153,350,20,'#CF142B')
rectangle(-12,10,350,20,'#CF142B')

t.setheading(-27)
rectangle(-330,200,750,60,'white')
t.stamp()
t.setheading(-27)
rectangle(-300,150,350,20,'#CF142B')
rectangle(10,15,350,20,'#CF142B')

t.setheading(0)
rectangle(-300,50,600,100,'white')
t.setheading(0)
rectangle(-50,150,100,300,'white')
t.setheading(0)
rectangle(-30,150,60,300,'#CF142B')
rectangle(-300,30,600,60,'#CF142B')

rectangle(-320,160,20,300,'white')
rectangle(-300,180,650,50,'white')
rectangle(-300,-150,610,30,'white')
t.setheading(180)
rectangle(350,-170,50,400,'white')
t.clearscreen()