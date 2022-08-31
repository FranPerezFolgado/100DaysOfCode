from tkinter import CENTER, LEFT
import pandas
from turtle import Turtle, Screen, title

BASE_PATH = 'Day25/us-states-game/'
FONT = ("Courier", 7, "bold")
def setup_screen() -> Screen:
    screen = Screen()
    screen.title("U.S States Game")
    background = BASE_PATH+'blank_states_img.gif'
    screen.setup(width=725, height=491)
    screen.bgpic(background)
    return screen

def setup_writer() -> Turtle:
    writer = Turtle()
    writer.penup()
    writer.hideturtle()
    writer.color("black")
    return writer


screen = setup_screen()
writer = setup_writer()
states_data = pandas.read_csv(BASE_PATH+'50_states.csv')
guessed_states = []


while len(guessed_states) < 50:
    guess_state = screen.textinput(title=f"Guess the State ({len(guessed_states)}/50)", prompt="What's your guessing:").title()
    state_obj = states_data[states_data.state == guess_state]
    if not state_obj.empty:
        state_x = int(state_obj.x)
        state_y = int(state_obj.y)
        writer.goto(x=state_x,y=state_y)
        writer.write(state_obj.state.item(), align=CENTER,font=FONT)
        guessed_states.append(guess_state)
    if guess_state == 'Exit':
        states_to_learn = []
        for state in states_data['state'].to_list():
            print(state)
            if not state in guessed_states:
                states_to_learn.append(state)

        states_to_learn_csv = BASE_PATH+'states_to_learn.csv'
        state_dataframe = pandas.DataFrame(states_to_learn, columns=['state'])
        state_dataframe.to_csv(states_to_learn_csv)
        break


