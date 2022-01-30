from tkinter import *
import time

result = 60

window = Tk()
window.title("Numbers Game")
window.geometry("360x240")

label = Label(window, text=result)
label.grid(column=0, row=0)


def clicked():
    global result
    result -= 1
    label.config(text=result)


def tick():
    clicked()
    window.after(1000, tick)  # after 1,000 milliseconds, call tick() again


tick()  # start the "loop"
window.mainloop()
