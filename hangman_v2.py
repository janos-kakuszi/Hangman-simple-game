import random
from tkinter import *
import os


word_list = []
guessed = []
counter = 0



def core_game():
    word = ""
    lang = input("What language do you want?\n" 
                 "If Hungarian, please enter: hun\nIf english, please enter: eng\nIf Python, please enter: pyt")
    if lang == "hun" or lang == "Hun":
        the_word = (random.choice(open("szavak.txt", 'r').read().splitlines()))
        word_list.append(the_word)
        word1 = ''.join(word_list[0])
    elif lang == "eng" or lang == "Eng":
        the_word = (random.choice(open("words.txt", 'r').read().splitlines()))
        word_list.append(the_word)
        word1 = ''.join(word_list[0])
    elif lang == "pyt" or lang == "Pyt":
        the_word = (random.choice(open("python.txt", 'r').read().splitlines()))
        word_list.append(the_word)
        word1 = ''.join(word_list[0])
    else:
        print("\nInvalid input, please repeat your choice in correct form\n")
        core_game()
    print(word1)
    return word1

word = core_game()

root = Tk()
root.title('Simple Hangman Game')
v = Canvas(root, height=330, width=600)
v.pack()

akasztofa1 = v.create_line(30, 50, 200, 50)
akasztofa2 = v.create_line(50, 50, 50, 250)
akasztofa3 = v.create_line(50, 250, 200, 250)
akasztófa4 = v.create_line(200, 50, 200, 110)


#wrong_guess1 = v.create_oval(182, 125, 217, 90, fill='black')
#wrong_guess2 = v.create_line(200, 125, 200, 180
#wrong_guess3 = v.create_line(200, 140, 170, 160)
#wrong_guess4 = v.create_line(200, 140, 230, 160)
#wrong_guess5 = v.create_line(200, 180, 170, 220)
#wrong_guess6 = v.create_line(200, 180, 230, 220)

label = Label(root, text='.: Hangman V2.0:.', fg="red", font="Verdana 14 bold \n")
label.place(relx=0.7, rely=0.1, anchor='n')
label2 = Label(root, text='Guess the word!', fg="black", font="Verdana 10 bold \n")
label2.place(relx=0.7, rely=0.2, anchor='n')

progress = StringVar()
progress.set("?"*len(word))

label3 = Label(root, textvariable=progress, fg="black", font="Verdana 24 bold \n")
label3.place(relx=0.7, rely=0.5, anchor='n')


#------------functions-----------------------------------------------


# --------- buttons ---------------------------------------------------
def buttonA():
    global guessed
    global counter
    if 'a' in word:
        guessed.append('a')
        for qw in range(len(word)):
            if word[qw] == 'a':
                print(word.index('a'))
                progress.set(progress.get()[0:qw]+'a'+progress.get()[1+qw:])
        buttona.config(state=DISABLED)
    else:
        guessed.append('a')
        print(guessed)
        print("none")
        counter += 1
        buttona.config(state=DISABLED)

def buttonB():
    global guessed
    global counter
    if 'b' in word:
        guessed.append('b')
        for qw in range(len(word)):
            if word[qw] == 'b':
                print(word.index('b'))
                progress.set(progress.get()[0:qw]+'b'+progress.get()[1+qw:])
        buttonb.config(state=DISABLED)
        countered()
    else:
        guessed.append('b')
        print(guessed)
        print("none")
        counter += 1
        buttonb.config(state=DISABLED)
        countered()


def buttonC():
    global guessed
    global counter
    if 'c' in word:
        guessed.append('c')
        for qw in range(len(word)):
            if word[qw] == 'c':
                print(word.index('c'))
                progress.set(progress.get()[0:qw]+'c'+progress.get()[1+qw:])
        buttonc.config(state=DISABLED)
        countered()
    else:
        guessed.append('c')
        print(guessed)
        print("none")
        counter += 1
        buttonc.config(state=DISABLED)
        countered()


def buttonD():
    global guessed
    global counter
    if 'd' in word:
        guessed.append('d')
        for qw in range(len(word)):
            if word[qw] == 'd':
                print(word.index('d'))
                progress.set(progress.get()[0:qw]+'d'+progress.get()[1+qw:])
        buttond.config(state=DISABLED)
        countered()
    else:
        guessed.append('d')
        print(guessed)
        print("none")
        counter += 1
        buttond.config(state=DISABLED)
        countered()

def buttonE():
    global guessed
    global counter
    if 'e' in word:
        guessed.append('e')
        for qw in range(len(word)):
            if word[qw] == 'e':
                print(word.index('e'))
                progress.set(progress.get()[0:qw]+'e'+progress.get()[1+qw:])
        buttone.config(state=DISABLED)
    else:
        guessed.append('e')
        print(guessed)
        print("none")
        counter += 1
        buttone.config(state=DISABLED)
        countered()


def buttonF():
    global guessed
    global counter
    if 'f' in word:
        guessed.append('f')
        for qw in range(len(word)):
            if word[qw] == 'f':
                print(word.index('f'))
                progress.set(progress.get()[0:qw]+'f'+progress.get()[1+qw:])
        buttonf.config(state=DISABLED)
    else:
        guessed.append('f')
        print(guessed)
        print("none")
        counter += 1
        buttonf.config(state=DISABLED)
        countered()


def buttonG():
    global guessed
    global counter
    if 'g' in word:
        guessed.append('g')
        for qw in range(len(word)):
            if word[qw] == 'g':
                print(word.index('g'))
                progress.set(progress.get()[0:qw]+'g'+progress.get()[1+qw:])
        buttong.config(state=DISABLED)
    else:
        guessed.append('g')
        print(guessed)
        print("none")
        counter += 1
        buttong.config(state=DISABLED)
        countered()


def buttonH():
    global guessed
    global counter
    if 'h' in word:
        guessed.append('h')
        for qw in range(len(word)):
            if word[qw] == 'h':
                print(word.index('h'))
                progress.set(progress.get()[0:qw]+'h'+progress.get()[1+qw:])
        buttonh.config(state=DISABLED)
    else:
        guessed.append('h')
        print(guessed)
        print("none")
        counter += 1
        buttonh.config(state=DISABLED)
        countered()

def buttonI():
    global guessed
    global counter
    if 'i' in word:
        guessed.append('i')
        for qw in range(len(word)):
            if word[qw] == 'i':
                print(word.index('i'))
                progress.set(progress.get()[0:qw]+'i'+progress.get()[1+qw:])
        buttoni.config(state=DISABLED)
    else:
        guessed.append('i')
        print(guessed)
        print("none")
        counter += 1
        buttoni.config(state=DISABLED)
        countered()

def buttonJ():
    global guessed
    global counter
    if 'j' in word:
        guessed.append('j')
        for qw in range(len(word)):
            if word[qw] == 'j':
                print(word.index('j'))
                progress.set(progress.get()[0:qw]+'j'+progress.get()[1+qw:])
        buttonj.config(state=DISABLED)
    else:
        guessed.append('j')
        print(guessed)
        print("none")
        counter += 1
        buttonj.config(state=DISABLED)
        countered()


def buttonK():
    global guessed
    global counter
    if 'k' in word:
        guessed.append('k')
        for qw in range(len(word)):
            if word[qw] == 'k':
                print(word.index('k'))
                progress.set(progress.get()[0:qw]+'k'+progress.get()[1+qw:])
        buttonk.config(state=DISABLED)
    else:
        guessed.append('k')
        print(guessed)
        print("none")
        counter += 1
        buttonk.config(state=DISABLED)
        countered()


def buttonL():
    global guessed
    global counter
    if 'l' in word:
        guessed.append('l')
        for qw in range(len(word)):
            if word[qw] == 'l':
                print(word.index('l'))
                progress.set(progress.get()[0:qw]+'l'+progress.get()[1+qw:])
        buttonk.config(state=DISABLED)
    else:
        guessed.append('l')
        print(guessed)
        print("none")
        counter += 1
        buttonk.config(state=DISABLED)
        countered()


def buttonM():
    global guessed
    global counter
    if 'm' in word:
        guessed.append('m')
        for qw in range(len(word)):
            if word[qw] == 'm':
                print(word.index('m'))
                progress.set(progress.get()[0:qw]+'m'+progress.get()[1+qw:])
        buttonm.config(state=DISABLED)
    else:
        guessed.append('m')
        print(guessed)
        print("none")
        counter += 1
        buttonm.config(state=DISABLED)
        countered()


def buttonN():
    global guessed
    global counter
    if 'n' in word:
        guessed.append('n')
        for qw in range(len(word)):
            if word[qw] == 'n':
                print(word.index('n'))
                progress.set(progress.get()[0:qw]+'n'+progress.get()[1+qw:])
        buttonn.config(state=DISABLED)
    else:
        guessed.append('n')
        print(guessed)
        print("none")
        counter += 1
        buttonn.config(state=DISABLED)
        countered()


def buttonO():
    global guessed
    global counter
    if 'o' in word:
        guessed.append('o')
        for qw in range(len(word)):
            if word[qw] == 'o':
                print(word.index('o'))
                progress.set(progress.get()[0:qw]+'o'+progress.get()[1+qw:])
        buttono.config(state=DISABLED)
    else:
        guessed.append('o')
        print(guessed)
        print("none")
        counter += 1
        buttono.config(state=DISABLED)
        countered()


def buttonP():
    global guessed
    global counter
    if 'p' in word:
        guessed.append('p')
        for qw in range(len(word)):
            if word[qw] == 'p':
                print(word.index('p'))
                progress.set(progress.get()[0:qw]+'p'+progress.get()[1+qw:])
        buttonp.config(state=DISABLED)
    else:
        guessed.append('p')
        print(guessed)
        print("none")
        counter += 1
        buttonp.config(state=DISABLED)
        countered()


def buttonQ():
    global guessed
    global counter
    if 'q' in word:
        guessed.append('q')
        for qw in range(len(word)):
            if word[qw] == 'q':
                print(word.index('q'))
                progress.set(progress.get()[0:qw]+'q'+progress.get()[1+qw:])
        buttonq.config(state=DISABLED)
    else:
        guessed.append('q')
        print(guessed)
        print("none")
        counter += 1
        buttonq.config(state=DISABLED)
        countered()


def buttonR():
    global guessed
    global counter
    if 'r' in word:
        guessed.append('r')
        for qw in range(len(word)):
            if word[qw] == 'r':
                print(word.index('r'))
                progress.set(progress.get()[0:qw]+'r'+progress.get()[1+qw:])
        buttonr.config(state=DISABLED)
    else:
        guessed.append('r')
        print(guessed)
        print("none")
        counter += 1

def buttonS():
    global guessed
    global counter
    if 's' in word:
        guessed.append('s')
        for qw in range(len(word)):
            if word[qw] == 's':
                print(word.index('s'))
                progress.set(progress.get()[0:qw]+'s'+progress.get()[1+qw:])
        buttons.config(state=DISABLED)
    else:
        guessed.append('s')
        print(guessed)
        print("none")
        counter += 1
        buttons.config(state=DISABLED)
        countered()


def buttonT():
    global guessed
    global counter
    if 't' in word:
        guessed.append('t')
        for qw in range(len(word)):
            if word[qw] == 't':
                print(word.index('t'))
                progress.set(progress.get()[0:qw]+'t'+progress.get()[1+qw:])
        buttont.config(state=DISABLED)
    else:
        guessed.append('t')
        print(guessed)
        print("none")
        counter += 1
        buttont.config(state=DISABLED)
        countered()


def buttonU():
    global guessed
    global counter
    if 'u' in word:
        guessed.append('u')
        for qw in range(len(word)):
            if word[qw] == 'u':
                print(word.index('u'))
                progress.set(progress.get()[0:qw]+'u'+progress.get()[1+qw:])
        buttonu.config(state=DISABLED)
    else:
        guessed.append('u')
        print(guessed)
        print("none")
        counter += 1
        buttonu.config(state=DISABLED)
        countered()


def buttonV():
    global guessed
    global counter
    if 'v' in word:
        guessed.append('v')
        for qw in range(len(word)):
            if word[qw] == 'v':
                print(word.index('v'))
                progress.set(progress.get()[0:qw]+'v'+progress.get()[1+qw:])
        buttonv.config(state=DISABLED)
    else:
        guessed.append('v')
        print(guessed)
        print("none")
        counter += 1
        buttonv.config(state=DISABLED)
        countered()


def buttonW():
    global guessed
    global counter
    if 'w' in word:
        guessed.append('w')
        for qw in range(len(word)):
            if word[qw] == 'w':
                print(word.index('w'))
                progress.set(progress.get()[0:qw]+'w'+progress.get()[1+qw:])
        buttonw.config(state=DISABLED)
    else:
        guessed.append('w')
        print(guessed)
        print("none")
        counter += 1
        buttonw.config(state=DISABLED)
        countered()


def buttonX():
    global guessed
    global counter
    if 'x' in word:
        guessed.append('x')
        for qw in range(len(word)):
            if word[qw] == 'x':
                print(word.index('x'))
                progress.set(progress.get()[0:qw]+'x'+progress.get()[1+qw:])
        buttonx.config(state=DISABLED)
    else:
        guessed.append('x')
        print(guessed)
        print("none")
        counter += 1
        buttonx.config(state=DISABLED)
        countered()


def buttonY():
    global guessed
    global counter
    if 'y' in word:
        guessed.append('y')
        for qw in range(len(word)):
            if word[qw] == 'y':
                print(word.index('y'))
                progress.set(progress.get()[0:qw]+'y'+progress.get()[1+qw:])
        buttony.config(state=DISABLED)
    else:
        guessed.append('y')
        print(guessed)
        print("none")
        counter += 1
        buttony.config(state=DISABLED)
        countered()


def buttonZ():
    global guessed
    global counter
    if 'z' in word:
        guessed.append('z')
        for qw in range(len(word)):
            if word[qw] == 'z':
                print(word.index('z'))
                progress.set(progress.get()[0:qw]+'z'+progress.get()[1+qw:])
        buttonz.config(state=DISABLED)
    else:
        guessed.append('z')
        print(guessed)
        print("none")
        counter += 1
        buttonz.config(state=DISABLED)
        countered()

def buttonÁ():
    global guessed
    global counter
    if 'á' in word:
        guessed.append('á')
        for qw in range(len(word)):
            if word[qw] == 'á':
                print(word.index('á'))
                progress.set(progress.get()[0:qw]+'á'+progress.get()[1+qw:])
        buttoná.config(state=DISABLED)
    else:
        guessed.append('á')
        print(guessed)
        print("none")
        counter += 1
        buttoná.config(state=DISABLED)
        countered()



def countered():
    if counter == 1:
        wrong_guess1 = v.create_oval(182, 125, 217, 90, fill='black')
    if counter == 2:
        wrong_guess2 = v.create_line(200, 125, 200, 180)
    if counter == 3:
        wrong_guess3 = v.create_line(200, 140, 170, 160)
    if counter == 4:
        wrong_guess4 = v.create_line(200, 140, 230, 160)
    if counter == 5:
        wrong_guess5 = v.create_line(200, 180, 170, 220)
        print(word)
    if counter == 6:
        wrong_guess6 = v.create_line(200, 180, 230, 220)
        root.destroy()

# --------- buttons ---------------------------------------------------

buttona = Button(root, text="a", command=buttonA)
buttona.pack(side=LEFT)
buttonb = Button(root, text="b", command=buttonB)
buttonb.pack(side=LEFT)
buttonc = Button(root, text="c", command=buttonC)
buttonc.pack(side=LEFT)
buttond = Button(root, text="d", command=buttonD)
buttond.pack(side=LEFT)
buttone = Button(root, text="e", command=buttonE)
buttone.pack(side=LEFT)
buttonf = Button(root, text="f", command=buttonF)
buttonf.pack(side=LEFT)
buttong = Button(root, text="g", command=buttonG)
buttong.pack(side=LEFT)
buttonh = Button(root, text="h", command=buttonH)
buttonh.pack(side=LEFT)
buttoni = Button(root, text="i", command=buttonI)
buttoni.pack(side=LEFT)
buttonj = Button(root, text="j", command=buttonJ)
buttonj.pack(side=LEFT)
buttonk = Button(root, text="k", command=buttonK)
buttonk.pack(side=LEFT)
buttonl = Button(root, text="l", command=buttonL)
buttonl.pack(side=LEFT)
buttonm = Button(root, text="m", command=buttonM)
buttonm.pack(side=LEFT)
buttonn = Button(root, text="n", command=buttonN)
buttonn.pack(side=LEFT)
buttono = Button(root, text="o", command=buttonO)
buttono.pack(side=LEFT)
buttonp = Button(root, text="p", command=buttonP)
buttonp.pack(side=LEFT)
buttonq = Button(root, text="q", command=buttonQ)
buttonq.pack(side=LEFT)
buttonr = Button(root, text="r", command=buttonR)
buttonr.pack(side=LEFT)
buttons = Button(root, text="s", command=buttonS)
buttons.pack(side=LEFT)
buttont = Button(root, text="t", command=buttonT)
buttont.pack(side=LEFT)
buttonu = Button(root, text="u", command=buttonU)
buttonu.pack(side=LEFT)
buttonv = Button(root, text="v", command=buttonV)
buttonv.pack(side=LEFT)
buttonw = Button(root, text="w", command=buttonW)
buttonw.pack(side=LEFT)
buttonx = Button(root, text="x", command=buttonX)
buttonx.pack(side=LEFT)
buttony = Button(root, text="y", command=buttonY)
buttony.pack(side=LEFT)
buttonz = Button(root, text="z", command=buttonZ)
buttonz.pack(side=LEFT)
buttoná = Button(root, text="á", command=buttonÁ)
buttoná.pack(side=LEFT)
buttoné = Button(root, text="é")
buttoné.pack(side=LEFT)
buttoní = Button(root, text="í")
buttoní.pack(side=LEFT)
buttonó = Button(root, text="ó")
buttonó.pack(side=LEFT)
buttonú = Button(root, text="ú")
buttonú.pack(side=LEFT)
buttonö = Button(root, text="ö")
buttonö.pack(side=LEFT)
buttonő = Button(root, text="ő")
buttonő.pack(side=LEFT)
buttonü = Button(root, text="ü")
buttonü.pack(side=LEFT)
buttonű = Button(root, text="ű")
buttonű.pack(side=LEFT)
buttonEXIT = Button(root, text="Exit").pack(side=BOTTOM)


root.mainloop()

replay = input("Wanna play another?: Yes(y) or Not(press any key)")
if replay == "y" or replay == "Y":
    del word_list[:]
    import new
else:
    exit()
