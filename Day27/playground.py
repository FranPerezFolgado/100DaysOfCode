
import tkinter


window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=400, height=400)

#Label
label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
label.grid(row=0,column=0)

label.config(text="new_text")

def button_click():

  label.config(text=input.get())
  print(input.get())

button = tkinter.Button(text="Click Me", command=button_click)
button.grid(row=1,column=1)
button1 = tkinter.Button(text="Click Me 1", command=button_click)
button1.grid(row=0,column=2)
#Entry
entry = tkinter.Entry()
entry.grid(row=2, column=3)


window.mainloop()
#def add(*args):
#  return sum(args)
#
#print(add(1,2,3,4,5,6,7,7))        
#
#def calulate(n,**kwargs):
#    print(kwargs)
#    n+=kwargs['add']
#    n*=kwargs['multiply']
#    return n
#
#print(calulate(2, add=2, multiply=3))
#
#
##window.mainloop()
#class Car:
#
#    def __init__(self, **kw) -> None:
#       self.make = kw['make']
#       self.model = kw.get('model')
#
#car = Car(make='nissan')
#print(car.model)