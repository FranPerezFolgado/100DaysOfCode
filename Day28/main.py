from cgitb import text
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks = ''
checkmark = '✓'
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_lbl.config(text='Timer', fg=GREEN)
    check_lbl.config(text='')
    canvas.itemconfig(timer_text, text='00:00')
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        timer_lbl.config(text="BREAK",fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_lbl.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_lbl.config(text="WORK", fg=GREEN)
        count_down(work_sec)    
     

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global checkmarks
    global timer
    count_mins = math.floor(count/60)
    count_seconds = count%60 if count%60 >= 10 else f'0{count%60}'
    
    canvas.itemconfig(timer_text, text=f'{count_mins}:{count_seconds}')
    if count > 0:
        timer = window.after(1, count_down, count-1)
    else:
        print(reps)
        if reps %2 != 0:
            checkmarks+=checkmark
            if len(checkmarks) > 4:
                checkmarks=''
            check_lbl.config(text=checkmarks)
            

        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, background=YELLOW)


timer_lbl = Label(text='Timer', fg=GREEN, font=(FONT_NAME,40,'bold'), bg=YELLOW)
timer_lbl.grid(row=0,column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='Day28/tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(row=1,column=1)

start_btn = Button(text="Start", command=start_timer) #command=start
start_btn.grid(row=2,  column=0, sticky='W')

reset_btn = Button(text='Reset', command=reset_timer) #command=reset
reset_btn.grid(row=2, column=2, sticky='E')


check_lbl = Label(text='',fg=GREEN, font=(FONT_NAME,20,'bold'), bg=YELLOW)
check_lbl.grid(row=3, column=1)
window.mainloop()





