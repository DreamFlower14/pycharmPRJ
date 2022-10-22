import random
import turtle

# 변수 설정
pSize, tSize = 10,0
r,g,b = 0.0 , 0.0 , 0.0

# 함수 작성

def 좌클릭(x,y):
    global r,g,b
    turtle.pencolor(r,g,b)
    turtle.pendown()
    turtle.goto(x,y)

def 우클릭(x,y):
    turtle.penup()
    turtle.goto(x,y)

def 휠(x,y):
    global r,g,b
    r = random.random()
    g = random.random()
    b = random.random()
    tSize = random.randrange(1,10)
    turtle.shapesize(tSize)

# 중요 코드

turtle.title("9999")
turtle.shape("turtle")

turtle.pensize(pSize)

turtle.onscreenclick(좌클릭,1)
turtle.onscreenclick(휠,2)
turtle.onscreenclick(우클릭,3)

turtle.done()
