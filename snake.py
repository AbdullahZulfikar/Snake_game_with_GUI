from turtle import Turtle

STARTING_POSITION = ((0, 0), (0, -20), (0, -40))
Y_COORDINATES = 0
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.CreateSnake()
        self.head = self.segments[0]

    def CreateSnake(self):
        for index in STARTING_POSITION:
            self.add_segment(index)

    def add_segment(self, position):
        new_segments = Turtle("square")
        new_segments.penup()
        new_segments.goto(position)
        self.segments.append(new_segments)

    def extent(self):
        self.add_segment(self.segments[-1].position())

    def Move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.CreateSnake()
        self.head = self.segments[0]

    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
