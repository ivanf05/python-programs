#Ivan Fonseca
#intro to computer science
#This program illustrates a trutle race.
#Two turtles will fight to the death and one will remain victorious.

import turtle
import random
red_turtle = input("What do you want the name of the red turtle to be?: ")
green_turtle = input("what do you want the name of the green turtle to be?: ")

ivan = turtle.Turtle()
ivan.penup()
ivan.goto(-200,-200)
ivan.pensize(10)
ivan.pendown()
ivan.hideturtle()
ivan.seth(0)
ivan.speed(10000)#worlds fastest turtle
for i in range(4):
    ivan.forward(400)
    ivan.left(90)

red = turtle.Turtle()
green = turtle.Turtle()
red.shape("turtle")
green.shape("turtle")
red.color(1,0,0)
green.color(0,1,0)


red_dist = 0
green_dist = 0

red_x = -200
green_x = -200
red_y = 100
green_y = -100

red.penup()
red.pensize(3)
green.penup()
green.pensize(3)
red.goto(red_x,red_y)
green.goto(green_x,green_y)
red.pendown()
green.pendown()

red.speed(5)
green.speed(5)

while red_dist < 400 and green_dist < 400:
    red_change_x = random.randint(1,10)
    red_change_y = random.randint(-10,10)
    red_x = red_x + red_change_x
    red_y = red_y + red_change_y
    if red_y < 95:
        red_y = 95
    if red_y > 105:
        red_y = 105
    red.goto(red_x,red_y)
    red_dist = red_dist + red_change_x 

    green_change_x = random.randint(1,10)
    green_change_y = random.randint(-10,10)
    green_x = green_x + green_change_x
    green_y = green_y + green_change_y
    if green_y < -95:
        green_y = -95
    if green_y > 105:
        green_y = 105
    green.goto(green_x,green_y)
    green_dist = green_dist + green_change_x
john = turtle.Turtle()
john.penup()
john.goto(-235,-235)
john.pendown()
john.pensize(2)

if red_dist >= 400:
    print("The winner of the race is %s." % red_turtle)
    print("The steps of %s is %d." % (red_turtle,red_x))
    print("The distance of %s is %d." % (red_turtle,red_dist))
    print("The steps of %s is %d." % (green_turtle,green_x))
    print("The distance of %s is %d." % (green_turtle,green_dist))
    john.write("The winner of the race is %s , %s distance %d , %s distance %d." % (red_turtle,red_turtle,red_dist,green_turtle,green_dist), font=("arial",12,"normal"))

elif red_dist == green_dist:
    print("The race is a tie.")
    print("The steps of %s is %d." % (red_turtle,red_x))
    print("The distance of %s is %d." % (red_turtle,red_dist))
    print("The steps of %s is %d." % (green_turtle,green_x))
    print("The distance of %s is %d." % (green_turtle,green_dist))
    john.write("The race is a tie , %s distance %d , %s distance %d." % (red_turtle,red_dist,green_turtle,green_dist), font=("arial",12,"normal"))

else:
    print("The winner of the race is %s." % green_turtle)
    print("The steps of %s is %d." % (red_turtle,red_x))
    print("The distance of %s is %d." % (red_turtle,red_dist))
    print("The steps of %s is %d." % (green_turtle,green_x))
    print("The distance of %s is %d." % (green_turtle,green_dist))
    john.write("The winner of the race is %s , %s distance %d , %s distance %d." % (green_turtle,red_turtle,red_dist,green_turtle,green_dist), font=("arial",12,"normal"))


#Both turtle's did a great job.
#Teenage Mutant Ninja Turtles










