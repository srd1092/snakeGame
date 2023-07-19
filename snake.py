from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
HEAD_UP = 90
HEAD_DOWN = 270
HEAD_LEFT = 180
HEAD_RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for current_position in STARTING_POSITIONS:
            self.add_segment(current_position)

    def add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def reset_snake(self):
        for seg in self.segments:
            # seg.goto(1000, 1000)
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[seg_num - 1].xcor()
            new_ycor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_xcor, new_ycor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != HEAD_DOWN:
            self.head.setheading(HEAD_UP)

    def down(self):
        if self.head.heading() != HEAD_UP:
            self.head.setheading(HEAD_DOWN)

    def left(self):
        if self.head.heading() != HEAD_RIGHT:
            self.head.setheading(HEAD_LEFT)

    def right(self):
        if self.head.heading() != HEAD_LEFT:
            self.head.setheading(HEAD_RIGHT)
