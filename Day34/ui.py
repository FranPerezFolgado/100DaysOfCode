THEME_COLOR = "#375362"
FONT=('Arial',20,'bold')
from tkinter import * 
from question_model import Question
from quiz_brain import QuizBrain

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')

        self.window.config(background=THEME_COLOR,padx=20,pady=20)
        self.create_score()
        self.create_canva()   

        image_true = PhotoImage(file='Day34/images/true.png')
        image_false = PhotoImage(file='Day34/images/false.png')

        self.true_btn = Button(image=image_true, highlightthickness=0, command=self.response_true)
        self.true_btn.grid(row=2, column=0)

        self.false_btn = Button(image=image_false, highlightthickness=0, command=self.response_false)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()
        
    
    def create_score(self):
        self.score = Label(text='Score: 0',fg='white', bg=THEME_COLOR)
        self.score.grid(row=0,column=1)
    
    def update_score(self):
        self.score.config(text='Score: '+str(self.quiz.score+1))

    def create_canva(self):
        self.canvas = Canvas(width=300, height=250,background='white')
        self.question = self.canvas.create_text(
            150,
            125,
            text='Some question text',
            font=FONT,
            fill=THEME_COLOR,
            width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfigure(self.question, text=q_text,font=FONT)



    def response_true(self):
        if self.quiz.check_answer('true'):
            self.update_score()
        
        self.get_next_question()
    def response_false(self):
        if self.quiz.check_answer('false'):
            self.update_score()
        
        self.get_next_question()

