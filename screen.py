from turtle import Screen


class Screen:

    def __init__(self):
        screen = Screen()
        screen.setup(width=600, height=600)
        screen.title("My Snake Game")
        screen.bgcolor("black")
        screen.tracer(0)
