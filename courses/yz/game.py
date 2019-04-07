#Turtle graphic
import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("bouncing balls")

mypen = turtle.Turtle()
mypen.speed(0)
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()
mypen.penup()

player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)

score = 0

maxGoals = 6
goals = []

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goal = goals[-1]
    goal.color('red')
    goal.shape('circle')
    goal.penup()
    goal.speed(0)
    goal.setposition(random.randint(-300, 300), random.randint(-300, 300))
    goal.left( random.randint(0, 360) )

speed = 1
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed += 1

def decreasespeed():
    global speed
    speed -= 1

def isCollision( t1, t2):
    d = math.sqrt( (t1.xcor() - t2.xcor())**2 + (t1.ycor() - t2.ycor())**2 )
    if d<20:
        return True
    else:
        return False

def inscope( player ):
    if player.xcor() > 300 or player.xcor() < -300:
        player.left(180)
    if player.ycor() > 300 or player.ycor() < -300:
        player.left(180)

wn.onkey(turnleft, 'Left')
wn.onkey(turnright, 'Right')
wn.onkey(increasespeed, "Up")
wn.onkey(decreasespeed, "Down")
wn.listen()
wn.tracer(3)

while True:
    player.forward(speed)
    inscope(player)

    for i in range(maxGoals):
        goal = goals[i]
        goal.forward(1)
        inscope(goal)
        if isCollision(player, goal):
            goal.setposition( random.randint(-300, 300), random.randint(-300, 300))
            goal.left( random.randint(0, 360) )
            score += 1
            mypen.undo()
            mypen.penup()
            mypen.setposition(-290, 310)
            scoreString ='Score: %s' % score
            mypen.write(scoreString, False, align='left', font=("Arial", 14, 'normal'))

deply = input("abc")

