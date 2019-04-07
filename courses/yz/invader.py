import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Space Invaders')
wn.tracer(1)

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.setposition( -300, -300 )
pen.down()
pen.pensize(3)
for i in range(4):
    pen.fd(600)
    pen.lt(90)
pen.hideturtle()

player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

step = 15

enemyspeed = 2

number_of_enemies = 5
enemies = []

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
    enemy = enemies[-1]
    enemy.color('red')
    enemy.shape('circle')
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(random.randint(-200, 200), random.randint(100,250))

bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.speed(0)
bullet.hideturtle()
bullet.setposition( player.xcor(), player.ycor()+15 )
bulletstep = 20
bulletstate = 'ready'

def moveleft():
    x = player.xcor()
    x -= step
    if x < -280:
        x= -280
    player.setx( x )

def moveright():
    x = player.xcor()
    x += step
    if x > 280:
        x= 280
    player.setx( x )

def firebullet():
    global bulletstate
    if bulletstate == 'ready':
        bulletstate = 'firing'
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition( x, y )
        bullet.showturtle()

def iscollition(t1, t2):
    d = math.sqrt( (t1.xcor() - t2.xcor())**2 + (t1.ycor() - t2.ycor())**2 )
    if d<15:
        return True
    else:
        return False

wn.onkey(moveleft, 'Left')
wn.onkey(moveright, 'Right')
wn.onkey(firebullet, 'space')
wn.listen()

while True:
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            enemyspeed = -enemyspeed
            y = enemy.ycor()
            y -= 40
            enemy.sety(y)

    if bulletstate == 'firing':
        y = bullet.ycor( )
        y += bulletstep
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet.sety(-240)
        bulletstate='ready'

    for enemy in enemies:
        if iscollition(bullet, enemy):
            bullet.hideturtle()
            bulletstate = 'ready'
            enemy.setposition(random.randint(-200, 200), random.randint(100,250))

        if iscollition(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game over")
            break

delay = input("press Enter to end.")