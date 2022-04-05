import turtle as t

swidth,sheight=500,500

t.title('무지개색  사각형 그리기')
t.shape('turtle')
t.setup(width=swidth+50, height=sheight+50)
t.screensize(swidth,sheight)
t.penup()
t.goto(0,-sheight/2)
t.pendown()
t.speed(0)

def nemo():
    for i in range(4):
        t.forward(100)
        t.left(90)

for square in range(1,250):
    if square%6==0:
        t.pencolor('red')
    elif square%5==0:
        t.pencolor('orange')
    elif square%4==0:
        t.pencolor('yellow')
    elif square%3==0:
        t.pencolor('green')
    elif square%2==0:
        t.pencolor('blue')
    elif square%1==0:
        t.pencolor('navyblue')
    else:
        t.pencolor('purple')



t.done()
