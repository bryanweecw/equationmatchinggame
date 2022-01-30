import tkinter as tk
import random
from random import randint
from tkinter import Button, Entry, Label

dispexpress = ""
testword = ""
testwordarr = []
turn = -1


def resetGame():
    global testword
    global dispexpress
    global testwordarr
    testword = ""
    testwordarr = []
    dispexpress = ""
    newWord()
    equation.set("")


def resetScore():
    game.score = 0
    gamescore.set(game.score)


def newWord():
    global testword
    probdecider = True
    randops = ["+", "-", "÷", "x"]
    testword = (
        testword
        + str(randint(0, 999))
        + randops[(randint(0, 3))]
        + str(randint(0, 999))
    )
    while probdecider:
        testword = testword + randops[(randint(0, 3))] + str(randint(0, 999))
        if len(testword) > 35:
            probdecider = False
        else:
            probs = randint(0, 100)
            if probs < 85:
                probdecider = True
            else:
                probdecider = False
    testequation.set(testword)
    testwordarr[:0] = testword


def press(num):
    global dispexpress
    global turn
    dispexpress = dispexpress + str(num)
    equation.set(dispexpress)
    game.randompos()
    turn += 1
    print(len(testword))
    print(turn)
    if dispexpress[turn] == testword[turn]:
        if (turn + 1) == len(testword):
            game.score += 1
            gamescore.set(game.score)
            resetGame()
            turn = -1
    else:
        resetGame()
        turn = -1


class GameState:
    def __init__(self):
        self.runstate = False
        self.hasLost = False
        self.score = 0
        self.buttonRows = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5]
        self.buttonColumns = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1]
        self.buttonCoords = [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [3, 0],
            [3, 1],
            [3, 2],
            [3, 3],
            [4, 0],
            [4, 1],
            [4, 2],
            [4, 3],
            [5, 0],
            [5, 1],
        ]

    def start(self):
        if self.runstate == True:
            return
        self.score = 0
        self.runstate = True
        self.hasLost = False

    def end(self):
        if self.runstate == False:
            return
        print("your score is: ", self.score)
        self.runstate = True
        self.hasLost = False

    def randompos(self):
        random.shuffle(self.buttonColumns)
        random.shuffle(self.buttonRows)
        random.shuffle(self.buttonCoords)
        window.update()


if __name__ == "__main__":

    window = tk.Tk()
    window.title("Simple Calculator")
    game = GameState()
    equation = tk.StringVar()
    testequation = tk.StringVar()
    gamescore = tk.IntVar()
    newWord()

    def replaceButtons():
        button1.grid(row=game.buttonCoords[0][0], column=game.buttonCoords[0][1])
        button2.grid(row=game.buttonCoords[1][0], column=game.buttonCoords[1][1])
        button3.grid(row=game.buttonCoords[2][0], column=game.buttonCoords[2][1])
        button4.grid(row=game.buttonCoords[3][0], column=game.buttonCoords[3][1])
        button5.grid(row=game.buttonCoords[4][0], column=game.buttonCoords[4][1])
        button6.grid(row=game.buttonCoords[5][0], column=game.buttonCoords[5][1])
        button7.grid(row=game.buttonCoords[6][0], column=game.buttonCoords[6][1])
        button8.grid(row=game.buttonCoords[7][0], column=game.buttonCoords[7][1])
        button9.grid(row=game.buttonCoords[8][0], column=game.buttonCoords[8][1])
        button10.grid(row=game.buttonCoords[9][0], column=game.buttonCoords[9][1])
        button11.grid(row=game.buttonCoords[10][0], column=game.buttonCoords[10][1])
        button12.grid(row=game.buttonCoords[11][0], column=game.buttonCoords[11][1])
        button13.grid(row=game.buttonCoords[12][0], column=game.buttonCoords[12][1])
        button14.grid(row=game.buttonCoords[13][0], column=game.buttonCoords[13][1])

    equation_field = Entry(window, textvariable=equation)
    equation_field.grid(columnspan=4, ipadx=70)
    answer_field = Entry(window, textvariable=testequation)
    answer_field.grid(columnspan=4, ipadx=70)
    user_score = Label(window, text="score:").grid(row=6, column=0)
    user_score_field = Entry(window, textvariable=gamescore).grid(row=6, column=1)
    button1 = Button(
        window, text="1", fg="black", command=lambda: [press(1), replaceButtons()]
    )
    button1.grid(row=game.buttonRows[0], column=game.buttonColumns[0])
    button2 = Button(
        window, text="2", fg="black", command=lambda: [press(2), replaceButtons()]
    )
    button2.grid(row=game.buttonRows[1], column=game.buttonColumns[1])
    button3 = Button(
        window, text="3", fg="black", command=lambda: [press(3), replaceButtons()]
    )
    button3.grid(row=game.buttonRows[2], column=game.buttonColumns[2])
    button4 = Button(
        window, text="+", fg="black", command=lambda: [press("+"), replaceButtons()]
    )
    button4.grid(row=game.buttonRows[3], column=game.buttonColumns[3])
    button5 = Button(
        window, text="4", fg="black", command=lambda: [press(4), replaceButtons()]
    )
    button5.grid(row=game.buttonRows[4], column=game.buttonColumns[4])
    button6 = Button(
        window, text="5", fg="black", command=lambda: [press(5), replaceButtons()]
    )
    button6.grid(row=game.buttonRows[5], column=game.buttonColumns[5])
    button7 = Button(
        window, text="6", fg="black", command=lambda: [press(6), replaceButtons()]
    )
    button7.grid(row=game.buttonRows[6], column=game.buttonColumns[6])
    button8 = Button(
        window, text="-", fg="black", command=lambda: [press("-"), replaceButtons()]
    )
    button8.grid(row=game.buttonRows[7], column=game.buttonColumns[7])
    button9 = Button(
        window, text="7", fg="black", command=lambda: [press(7), replaceButtons()]
    )
    button9.grid(row=game.buttonRows[8], column=game.buttonColumns[8])
    button10 = Button(
        window, text="8", fg="black", command=lambda: [press(8), replaceButtons()]
    )
    button10.grid(row=game.buttonRows[9], column=game.buttonColumns[9])
    button11 = Button(
        window, text="9", fg="black", command=lambda: [press(9), replaceButtons()]
    )
    button11.grid(row=game.buttonRows[10], column=game.buttonColumns[10])
    button12 = Button(
        window, text="x", fg="black", command=lambda: [press("x"), replaceButtons()]
    )
    button12.grid(row=game.buttonRows[11], column=game.buttonColumns[11])
    button13 = Button(
        window, text="0", fg="black", command=lambda: [press(0), replaceButtons()]
    )
    button13.grid(row=game.buttonRows[12], column=game.buttonColumns[12])
    button14 = Button(
        window, text="÷", fg="black", command=lambda: [press("÷"), replaceButtons()]
    )
    button14.grid(row=game.buttonRows[13], column=game.buttonColumns[13])
    startbutton = Button(
        window,
        text="New Game",
        fg="black",
        command=lambda: [game.end, game.start, resetGame(), resetScore()],
    )
    startbutton.grid(row=6, column=2)
    endbutton = Button(window, text="End Game", fg="black", command=lambda: [game.end])
    endbutton.grid(row=6, column=3)

    window.mainloop()
