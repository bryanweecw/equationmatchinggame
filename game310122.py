import random
from random import randint
import tkinter
import pygame

dispexpress = ""
testword = ""
turn = -1
timeleft = 30
highestscore = 0
congratsplayedbefore = False


def bgm():
    pygame.mixer.music.load("kahootbgm.wav")
    pygame.mixer.music.play(loops=-1)


def bing():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("ding.wav"))


def bong():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound("shortbuzz.wav"))


def buzz():
    pygame.mixer.Channel(2).play(pygame.mixer.Sound("buzz.wav"))


def ticksound():
    pygame.mixer.Channel(3).play(pygame.mixer.Sound("ticksound.wav"), loops=-1)


def stopticksound():
    pygame.mixer.Channel(3).stop()


def congratsplayable():
    pygame.mixer.Channel(4).play(pygame.mixer.Sound("congratsplayable.wav"))


def congratsunplayable():
    pygame.mixer.Channel(5).play(pygame.mixer.Sound("congratsunplayable.wav"))


def highscoresound():
    pygame.mixer.Channel(6).play(pygame.mixer.Sound("highscore.wav"))


def resetGame():
    global testword
    global dispexpress
    global timeleft
    global turn
    global highestscore
    global congratsplayedbefore
    if game.score > highestscore:
        if not congratsplayedbefore:
            highscoresound()
            congratsplayedbefore = True
        highestscore = game.score
        highscore.set(highestscore)
    testword = ""
    dispexpress = ""
    newWord()
    stopticksound()
    equation.set("")
    timeleft = 30
    turn = -1


def resetScore():
    global congratsplayedbefore
    game.score = 0
    gamescore.set(game.score)
    congratsplayedbefore = False


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
            if probs < 0:
                probdecider = True
            else:
                probdecider = False
    testequation.set(testword)


def press(num):
    global dispexpress
    global turn
    global highestscore
    dispexpress = dispexpress + str(num)
    equation.set(dispexpress)
    game.randompos()
    turn += 1
    print(len(testword))
    print(turn)
    if dispexpress[turn] == testword[turn]:
        bing()
        if (turn + 1) == len(testword):
            if game.score > 10:
                congratsunplayable()
            game.score += 1
            congratsplayable()
            gamescore.set(game.score)
            resetGame()
    else:
        bong()
        resetScore()
        resetGame()


class GameState:
    def __init__(self):
        self.runstate = False
        self.hasLost = False
        self.pause = False
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

    def toggle(self):
        self.pause = not self.pause
        if self.pause:
            stopticksound()
        if not self.pause:
            if timeleft < 15:
                ticksound()
        print(self.pause)


if __name__ == "__main__":

    window = tkinter.Tk()
    window.title("Simple Calculator")
    window.geometry("480x300")
    window.resizable(False, False)
    game = GameState()
    equation = tkinter.StringVar()
    testequation = tkinter.StringVar()
    gamescore = tkinter.IntVar()
    highscore = tkinter.IntVar()
    sec = tkinter.StringVar()
    newWord()
    pygame.mixer.init()
    bgm()

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

    equation_field = tkinter.Label(
        window, textvariable=equation, font="Helvetica 20", fg="green"
    )
    equation_field.grid(columnspan=4, ipadx=70)
    answer_field = tkinter.Label(
        window,
        textvariable=testequation,
        font="Helvetica 15",
    )
    answer_field.grid(columnspan=4, ipadx=70)
    user_score = tkinter.Label(
        window, text="Score:", font="Helvetica 20", fg="green"
    ).grid(row=6, column=0)
    user_score_field = tkinter.Label(
        window, textvariable=gamescore, font="Helvetica 20", fg="green"
    ).grid(row=6, column=1)
    gametimer = tkinter.Label(window, text=timeleft, fg="firebrick1")
    gametimer.grid(column=0, row=0)
    high_score = tkinter.Label(window, text="Highscore:", font="Helvetica 20").grid(
        row=7, column=0
    )
    high_score_field = tkinter.Label(
        window, textvariable=highscore, font="Helvetica 20"
    ).grid(row=7, column=1)
    instructions = tkinter.Label(
        window,
        text="Press the buttons to re-create the equation shown before the timer runs out",
        font="Helvetica 14",
        fg="firebrick1",
    )
    instructions.grid(row=8, column=0, columnspan=4)

    def tock():
        global timeleft
        if game.pause:
            timeleft = timeleft
        else:
            timeleft -= 1
            gametimer.config(text=timeleft)
            if timeleft == 15:
                ticksound()
            if timeleft == 0:
                stopticksound()
                buzz()
                resetGame()

    def tick():
        if timeleft > 0:
            tock()
            window.after(1000, tick)

    tick()

    button1 = tkinter.Button(
        window,
        text="1",
        fg="black",
        command=lambda: [press(1), replaceButtons()],
        font="Helvetica 25",
        width="5",
    )
    button1.grid(row=game.buttonRows[0], column=game.buttonColumns[0])
    button2 = tkinter.Button(
        window,
        text="2",
        fg="black",
        command=lambda: [press(2), replaceButtons()],
        font="Helvetica 25",
        width="5",
    )
    button2.grid(row=game.buttonRows[1], column=game.buttonColumns[1])
    button3 = tkinter.Button(
        window,
        text="3",
        fg="black",
        command=lambda: [press(3), replaceButtons()],
        font="Helvetica 25",
        width="5",
    )
    button3.grid(row=game.buttonRows[2], column=game.buttonColumns[2])
    button4 = tkinter.Button(
        window,
        text="+",
        fg="black",
        command=lambda: [press("+"), replaceButtons()],
        font="Helvetica 25",
        width="5",
    )
    button4.grid(row=game.buttonRows[3], column=game.buttonColumns[3])
    button5 = tkinter.Button(
        window,
        text="4",
        fg="black",
        command=lambda: [press(4), replaceButtons()],
        font="Helvetica 25",
        width="5",
    )
    button5.grid(row=game.buttonRows[4], column=game.buttonColumns[4])
    button6 = tkinter.Button(
        window,
        text="5",
        fg="black",
        command=lambda: [press(5), replaceButtons()],
        font="Helvetica 25",
        width="5",
    )
    button6.grid(row=game.buttonRows[5], column=game.buttonColumns[5])
    button7 = tkinter.Button(
        window,
        text="6",
        fg="black",
        command=lambda: [press(6), replaceButtons()],
        font="Helvetica 25",
        width="5",
    )
    button7.grid(row=game.buttonRows[6], column=game.buttonColumns[6])
    button8 = tkinter.Button(
        window,
        text="-",
        fg="black",
        command=lambda: [press("-"), replaceButtons()],
        font="Helvetica 25",
        width="5",
    )
    button8.grid(row=game.buttonRows[7], column=game.buttonColumns[7])
    button9 = tkinter.Button(
        window,
        text="7",
        fg="black",
        command=lambda: [press(7), replaceButtons()],
        font="Helvetica 25",
        width="5",
    )
    button9.grid(row=game.buttonRows[8], column=game.buttonColumns[8])
    button10 = tkinter.Button(
        window,
        text="8",
        fg="black",
        command=lambda: [press(8), replaceButtons()],
        font="Helvetica 25",
        width="5",
    )
    button10.grid(row=game.buttonRows[9], column=game.buttonColumns[9])
    button11 = tkinter.Button(
        window,
        text="9",
        fg="black",
        command=lambda: [press(9), replaceButtons()],
        font="Helvetica 25",
        width="5",
    )
    button11.grid(row=game.buttonRows[10], column=game.buttonColumns[10])
    button12 = tkinter.Button(
        window,
        text="x",
        fg="black",
        command=lambda: [press("x"), replaceButtons()],
        font="Helvetica 25",
        width="5",
    )
    button12.grid(row=game.buttonRows[11], column=game.buttonColumns[11])
    button13 = tkinter.Button(
        window,
        text="0",
        fg="black",
        command=lambda: [press(0), replaceButtons()],
        font="Helvetica 25",
        width="5",
    )
    button13.grid(row=game.buttonRows[12], column=game.buttonColumns[12])
    button14 = tkinter.Button(
        window,
        text="÷",
        fg="black",
        command=lambda: [press("÷"), replaceButtons()],
        font="Helvetica 25",
        width="5",
    )
    button14.grid(row=game.buttonRows[13], column=game.buttonColumns[13])
    startbutton = tkinter.Button(
        window,
        text="New Game",
        fg="black",
        command=lambda: [game.end(), game.start(), resetGame(), resetScore()],
    )
    startbutton.grid(row=6, column=2)
    endbutton = tkinter.Button(
        window, text="Toggle Timer", fg="black", command=lambda: [game.toggle()]
    )
    endbutton.grid(row=6, column=3)

    window.mainloop()
