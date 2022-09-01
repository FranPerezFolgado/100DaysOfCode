from cgitb import text
import tkinter

def calculate():
    km = int(text_input.get()) * 1.609
    var.set(str(km))

window = tkinter.Tk()
window.title("My first GUI program")
window.config(padx=20, pady=20)

text_input= tkinter.Entry()
text_input.grid(row=0, column=1)
miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label= tkinter.Label(text="is equal to")
equal_label.grid(row=1, column=0)
var = tkinter.StringVar(value="0")
result_label = tkinter.Label(textvariable=var)
result_label.grid(row=1, column=1)
km_label = tkinter.Label(text="Km")
km_label.grid(row=1,column=2)


button = tkinter.Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()