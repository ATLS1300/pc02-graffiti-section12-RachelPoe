#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

boxup = turtle.up()
boxmove = turtle.forward(300)
boxturn1 = turtle.right(90)
boxmovedown = turtle.forward(300)
boxturn2 = turtle.right(90)
boxdown = turtle.down()
boxcolor = turtle.color("blue3")
boxfill = turtle.begin_fill()
boxmove2 = turtle.forward(600)
boxturn3 = turtle.right(90)
boxmove4 = turtle.forward(200)
boxturn4 = turtle.right(90)
boxmove5 = turtle.forward(600)
boxturn5 = turtle.right(90)
boxmove6 = turtle.forward(200)
boxfillend = turtle.end_fill()

bubup = turtle.up()
bubturn1 = turtle.right(180)
bubmove1 = turtle.forward(500)
bubturn2 = turtle.left(90)
bubmove2 = turtle.forward(75)
bubdown = turtle.down()
bubcolor = turtle.color("aquamarine3")
bubfill = turtle.begin_fill()
bubcircle = turtle.circle(45)
bubendfill = turtle.end_fill()

bub2up = turtle.up()
bub2turn1 = turtle.left(90)
bub2move1 = turtle.forward(200)
bub2turn2 = turtle.right(90)
bub2move2 = turtle.forward(100)
bub2color = turtle.color("DarkCyan")
bub2down = turtle.down()
bub2fill = turtle.begin_fill()
bub2circle = turtle.circle(30)
bub2end = turtle.end_fill()

bub3up = turtle.up()
bub3move1 = turtle.forward(300)
bub3turn1 = turtle.right(90)
bub3move2 = turtle.forward(75)
bub3color = turtle.color("DarkSlateGray3")
bub3down = turtle.down()
bub3fill = turtle.begin_fill()
bub3circle = turtle.circle(50)
bub3end = turtle.end_fill()

lineup = turtle.up()
linemove1 = turtle.forward(250)
lineturn2 = turtle.right(90)
linemove2 = turtle.forward(300)
lineturn3 = turtle.right(180)
linecolor = turtle.color("DeepSkyBlue")
linedown = turtle.down()
linesize = turtle.pensize(10)
linemove3 = turtle.forward(500)
                        
#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
