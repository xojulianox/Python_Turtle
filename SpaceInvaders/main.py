#Space Invaders - Part 1
#Set up screen
#Python 2.7 on Mac

#see the turtle documentation : https://docs.python.org/3.3/library/turtle.html?highlight=turtle
import turtle
import math
import os
import random

#Set up the screen


#This makes a turtle screen singleton
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("giphy.gif")

#Register the shapes
turtle.register_shape("raumschiff.gif")
turtle.register_shape("monster.gif")

#Draw border: Draws a border


#instanciates a Turtle object.
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")


#pulls the pen up no drawing when moving
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

#side is the variable and in range(4) means 4 times from 0 to 3
for side in range(4):


    #moves the turtle forward by the specific distance
    border_pen.fd(600)

    #Turns the turtle left by 90 degree
    border_pen.lt(90)

#makes the turtle invisible (the turtle is a little arrow on the screen)
border_pen.hideturtle()


#SET THE SCORE to 0
score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score :%s" %score
score_pen.write(scorestring, False, align="left",font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("raumschiff.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
#this sets the turtle direction turned left by 90 degree
player.setheading(90)

playerspeed = 15


#Create the enemy


enemyspeed=2

#Choose a number of enemies
number_of_enemies = 5
#Create an empty list of enemies

enemies =[]
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("monster.gif")
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-200,200)
    y=random.randint(100,200)
    enemy.setposition(x, y)


#Create the player's bullet
bullet = turtle.Turtle()
bullet.hideturtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)#fastest speed
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)


bulletspeed = 20



#Define bullet state
#ready - ready to fire
#fire - bullet is firing

bulletstate = "ready"









#We need to create function for moving left and right and bind them to a key and also for the bullet
def move_left():
    x = player.xcor() #the x coordinate
    x -= playerspeed #reduce it
    if x < -280:
        x=-280
    player.setx(x) #reset it

def move_right():
    x = player.xcor()
    x += playerspeed
    if x >280:
        x=280
    player.setx(x)

def fire_bullet():
    global bulletstate #if it is defined outside the function it is a global variable and if we
    #to change the state outside the function it needs to be global
    if bulletstate=="ready":
        bulletstate= "fire"
        x=player.xcor()
        y=player.ycor()

        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2)+math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

#Create keyboard bindings a for left and d for right
turtle.listen()
turtle.onkey(move_left, "a")
turtle.onkey(move_right, "d")
turtle.onkey(fire_bullet, " ")


#Main game loop
while True:
    for enemy in enemies:
        x= enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)



        if enemy.xcor() > 280:
            for i in enemies:
                y= i.ycor()
                y-= 40

                i.sety(y)
            enemyspeed *= -1

        if enemy.xcor() < -280:
            for i in enemies:
                y= i.ycor()
                y-= 40

                i.sety(y)
            enemyspeed *= -1


        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(100, 200)
            enemy.setposition(x, y)
            score += 10
            scorestring = "Score :%s" % score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            score_pen.hideturtle()


        if isCollision(enemy, player):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    #Move the bullet
    if bulletstate == "fire":
        y= bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bulletstate =="ready":
        bullet.hideturtle()


    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate="ready"





turtle.done()
