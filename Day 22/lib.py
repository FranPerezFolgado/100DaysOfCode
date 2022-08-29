from turtle import Screen

def setup_screen() -> Screen:
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("PONG")
    screen.listen()
    screen.tracer(0)
    return screen