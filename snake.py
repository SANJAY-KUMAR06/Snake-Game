from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_turtle()
        self.head = self.turtles[0]

    def create_turtle(self):
        for position in STARTING_POS:
            self.add_turtle(position)

    def add_turtle(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(position)
        self.turtles.append(new_turtle)

    def extend(self):
        self.add_turtle(self.turtles[-1].position())  # it gets last value from the turtles list

    def move(self):

        for turtle in range(len(self.turtles) - 1, 0, -1):
            # if turtle length =3 then start=3,stop=0 and step=-1(it goes in backward
            # we need to move 3rd turtle over 2nd's pos and 2nd's to 1st's pos so that dispart in snake will not occur

            current_x = self.turtles[turtle - 1].xcor()  # provides the previous turtles x pos
            current_y = self.turtles[turtle - 1].ycor()  # provides the previous turtles y pos
            self.turtles[turtle].goto(current_x, current_y)  # it moves current turtle to previous turtle's postion

        self.turtles[0].forward(MOVE_FORWARD)

    def reset(self):
        for turtle in self.turtles:
            turtle.goto(1000, 1000)  # making the collision turtle to disappear from screen
        self.turtles.clear()  # clears all the turtles in the turtles list
        self.create_turtle()
        self.head = self.turtles[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
