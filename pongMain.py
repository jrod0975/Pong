# CREDITS TO freeCodeCamp.org on YouTube
# https://www.youtube.com/watch?v=C6jJg9Zan7w

#   My twist: Ball goes faster everytime it is hit by a paddle
#   game window actually resembles a table tennis table
#   i'll work on a single player version of this in which the player hits the ball
#   against the wall and the ball bounces back faster each time. With a scoring system like an arcade game
#   i'll use this program as reference

import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("dark green")
window.setup(width=800, height=600) # COORDINATE PLANE X = [-400, 400] Y = [-300, 300]
window.tracer(0) #STOPS WINDOW FROM UPDATING...MAKES GAME RUN SMOOTH

# PLAYER SCORE
blueScore = 0;
redScore = 0;

#Line
line = turtle.Turtle()
line.speed(0)
line.shape("square")
line.color("white")
line.shapesize(stretch_wid=.25, stretch_len=400)
line.penup()

# PADDLE A
paddleA = turtle.Turtle()
paddleA.speed(0) # ANIMATION SPEED
paddleA.shape("square")
paddleA.color("blue")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0) # X AND Y COORDINATES


# PADDLE B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("red")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.6 # BALL MOVEMENT SPEED
ball.dy = 2.6

# PEN ?
pen = turtle.Turtle()
pen.speed(0) #Animation speed NOT movement speed
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Blue: 0  Red: 0", align="center", font=("Courier", 24, "bold"))


# UP DOWN FUNCTIONS
def paddleA_UP():
    y = paddleA.ycor() # .ycor() FROM TURTLE MODULE
    y += 40
    paddleA.sety(y)

def paddleA_DOWN():
    y = paddleA.ycor() # .ycor() FROM TURTLE MODULE
    y -= 40
    paddleA.sety(y)

def paddleB_UP():
    y = paddleB.ycor() # .ycor() FROM TURTLE MODULE
    y += 40
    paddleB.sety(y)

def paddleB_DOWN():
    y = paddleB.ycor() # .ycor() FROM TURTLE MODULE
    y -= 40
    paddleB.sety(y)


# KEYBOARD BINDING
window.listen()
window.onkeypress(paddleA_UP, "w")  # IF USER HITS "W" PADDLE WILL GO UP
window.onkeypress(paddleA_DOWN, "s")  # IF USER HITS "D" PADDLE WILL GO DOWN
window.onkeypress(paddleB_UP, "Up") #ARROWS CANT BE TYPED SO THEYRE CALLED "UP"
window.onkeypress(paddleB_DOWN, "Down") #AND "DOWN"


# MAIN GAME LOOP
while True:
    window.update()

    # MOVING THE BALL
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # BORDERS
    # KEEP IN MIND THE WINDOW HEIGHT AND WIDTH
    # BAll SPEED WILL RESET IF A PLAYER SCORES
    if ball.ycor() > 290:  #AS SOON AS THE BALL REACHES 390 ON THE COORDINATE PLANE
        ball.sety(290)
        #ball.dy = 2.6
        ball.dy *= -1  #REVERSES THE DIRECTION

    if ball.ycor() < -280:
        ball.sety(-280)
        #ball.dy = 2.6
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = 2.6
        ball.dx *= -1
        blueScore += 1;
        pen.clear()
        pen.write("Blue: {}  Red: {}".format(blueScore, redScore), align="center", font=("Courier", 24, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = 2.6
        ball.dx *= -1
        redScore += 1;
        pen.clear()
        pen.write("Blue: {}  Red: {}".format(blueScore, redScore), align="center", font=("Courier", 24, "bold"))


    #PADDLE AND BALL COLLISION
    # BALL SPEED WILL INCREASE EVERYTIME A PLAYER HITS THE BALL BY 1.1

    if (ball.xcor() > 330 and ball.xcor() < 340) and (ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1.1
        # if edges are touching ball will bounce back

    if (ball.xcor() < -330 and ball.xcor() > -340) and (ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1.1
