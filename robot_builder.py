# This is the main page
import turtle as t


def rectangle(horizontal, vertical, color):
    t.pendown()  # Put's the turtle pen to start drawing
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1, 3):  # using the range(1, 3) makes the loop run twice
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()  # put's the pen back to stop drawing
    t.penup()  # Pull the pen back up
    t.speed('slow')  # set's the turtle speed
    t.bgcolor('Dodger blue')  # Makes the background of the window dodge blue

    # Feet
    t.goto(-100, -150)  # Move the turtle position x = -100 and y = 150
    rectangle(50, 20, 'blue')  # We use the rectangle function to draw a blue rect 50 wide and 20 high
    t.goto(-30, - 150)
    rectangle(50, 20, 'blue')

    # legs
    t.goto(-25, -50)  # the turtle moves to position x = -25, y = 50
    rectangle(15, 100, 'grey')  # Draws the left leg
    t.goto(-55, -50)
    rectangle(-15, 100, 'grey')  # Draws the Right leg

    # body
    t.goto(-90, 100)
    rectangle(100, 150, 'red')

    # arms
    t.goto(-150, 70)
    rectangle(60, 15, 'grey')  # Upper right arm
    t.goto(-150, 110)
    rectangle(15, 40, 'grey')  # lower right arm

    t.goto(10, 70)
    rectangle(60, 15, 'grey')  # Upper left arm
    t.goto(55, 110)
    rectangle(15, 40, 'grey')  # Lower left arm

    # Neck
    t.goto(-50, 120)
    rectangle(15, 20, 'grey')

    # Head
    t.goto(-85, 170)
    rectangle(80, 50, 'red')

    # Eyes
    t.goto(-60, 160)
    rectangle(30, 10, 'white')  # White part of the eye
    t.goto(-55, 155)
    rectangle(5, 5, 'black')  # Draw the Right Pupil
    t.goto(-40, 155)
    rectangle(5, 5, 'black')  # Draw the left pupil

    # Mouth
    t.goto(-65, 135)
    rectangle(40, 5, 'black')
    t.hideturtle()  # This will make the turtle invisible
