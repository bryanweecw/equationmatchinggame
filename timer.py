# Import the required library
from tkinter import *
import time

# Create an instance of tkinter frame
result = 60
win = Tk()
win.geometry("750x300")
win.resizable(False, False)
# Configure the background
win.config(bg="burlywood1")
# Create Entry Widgets for HH MM SS
gametimer = Label(win, text=result, width=2, font="Helvetica 14").place(x=220, y=120)


def clicked():
    global result
    result -= 1
    gametimer.config(text=result)


def tick():
    clicked()
    win.after(1000, tick)


tick()


# # Define the function for the timer
# def countdowntimer():
#     times = 60
#     while times > -1:
#         sec.set(times)
#         # Update the time
#         time.sleep(1)
#         win.update()
#         if times == 0:
#             sec.set("00")
#         times -= 1


# countdowntimer()

Label(win, font=("Helvetica bold", 22), text="Set the Timer", bg="burlywood1").place(
    x=105, y=70
)
win.mainloop()
