"""
Creates a simple etch-a-sketch clone using the native Python turtle module
Up arrow to move forward
Down arrow to move backwards
Right arrow to rotate right
Left arrow to rotate left
C key to reset the etch-a-sketch
"""

my_turtle = turtle.Turtle()
screen = turtle.Screen()
my_turtle.speed(10)

def move_forward():
    my_turtle.forward(5)

def move_backwards():
    my_turtle.backward(5)

def turn_right():
    my_turtle.right(5)

def turn_left():
    my_turtle.left(5)

def clear_screen():
    my_turtle.reset()

screen.listen()
screen.onkey(key="Up",fun=move_forward)
screen.onkey(key="Down",fun=move_backwards)
screen.onkey(key="Right",fun=turn_right)
screen.onkey(key="Left",fun=turn_left)
screen.onkey(key="c",fun=clear_screen)

screen.exitonclick()




