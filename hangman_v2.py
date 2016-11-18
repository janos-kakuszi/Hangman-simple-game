import random
from tkinter import *
import os


word_list = []
guessed = []
counter = 0

# ----------------- Selecting Language ---------------------
def core_game():
    print("You can play 2 games in a row, dont forget!")
    lang = input("What language do you want?\n"
                 "If Hungarian, please enter: hun\nIf english, please enter: eng\nIf Python, please enter: pyt\n")
    if lang == "hun" or lang == "Hun":
        the_word = (random.choice(open("for_game_hungarian.md", 'r').read().splitlines()))
        word_list.append(the_word)
        word1 = ''.join(word_list[0])
    elif lang == "eng" or lang == "Eng":
        the_word = (random.choice(open("for_game_english.md", 'r').read().splitlines()))
        word_list.append(the_word)
        word1 = ''.join(word_list[0])
    elif lang == "pyt" or lang == "Pyt":
        the_word = (random.choice(open("for_game_python.md", 'r').read().splitlines()))
        word_list.append(the_word)
        word1 = ''.join(word_list[0])
    else:
        print("\nInvalid input, please repeat your choice in correct form, start the game again!\n")
        exit()
    return word1

word = core_game()

# ----------------- Tkinter window ---------------------
root = Tk()
root.title('Simple Hangman Game')
v = Canvas(root, height=330, width=600)
v.pack()

akasztofa1 = v.create_line(30, 50, 200, 50, width=3)
akasztofa2 = v.create_line(50, 50, 50, 250, width=3)
akasztofa3 = v.create_line(50, 250, 200, 250, width=3)
akasztófa4 = v.create_line(200, 50, 200, 110, width=3)

label = Label(root, text='.: Hangman V2.0:.', fg="red", font="Verdana 14 bold \n")
label.place(relx=0.7, rely=0.1, anchor='n')
label2 = Label(root, text='Guess the word!', fg="black", font="Verdana 10 bold \n")
label2.place(relx=0.7, rely=0.2, anchor='n')

progress = StringVar()
progress.set("?"*len(word))

label3 = Label(root, textvariable=progress, fg="black", font="Verdana 24 bold \n")
label3.place(relx=0.7, rely=0.5, anchor='n')


# ----------------- Functions ---------------------

def win():
    print("""

      _____  ____  _   _  _____ _____         _______ _____ _
'    / ____|/ __ \| \ | |/ ____|  __ \     /\|__   __/ ____| |
'   | |  __| |  | |  \| | |  __| |__) |   /  \  | | | (___ | |
'   | | |_ | |  | | . ` | | |_ |  _  /   / /\ \ | |  \___ \| |
'   | |__| | |__| | |\  | |__| | | \ \  / ____ \| |  ____) |_|
'   _\_____|\____/|_| \_|\_____|_|  \_\/_/___ \_\_|_|_____/(_)
'   \ \   / / __ \| |  | | \ \        / / __ \| \ | | |
'    \ \_/ / |  | | |  | |  \ \  /\  / / |  | |  \| | |
'     \   /| |  | | |  | |   \ \/  \/ /| |  | | . ` | |
'      | | | |__| | |__| |    \  /\  / | |__| | |\  |_|
'      |_|  \____/ \____/      \/  \/   \____/|_| \_(_)
'
'
                    """)


def lose():
    print("""

'   __     ______  _    _   _      ____   _____ _______ _
'   \ \   / / __ \| |  | | | |    / __ \ / ____|__   __| |
'    \ \_/ / |  | | |  | | | |   | |  | | (___    | |  | |
'     \   /| |  | | |  | | | |   | |  | |\___ \   | |  | |
'      | | | |__| | |__| | | |___| |__| |____) |  | |  |_|
'      |_|  \____/ \____/  |______\____/|_____/   |_|  (_)
'
'                                                         """)
    
def search(szo):
    need = open("for_game_hungarian.md")
    text = need.read().strip().split()

    if szo in text:
        return True
    else:
        return False
        need.close()
# ----------------- Buttons function (A-Z) + exit - long section ---------------------
def buttonA():
    global guessed
    global counter
    if 'a' in word:
        guessed.append('a')
        for qw in range(len(word)):
            if word[qw] == 'a':
                progress.set(progress.get()[0:qw]+'a'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttona.config(state=DISABLED)
    else:
        guessed.append('a')
        counter += 1
        buttona.config(state=DISABLED)
        countered()


def buttonB():
    global guessed
    global counter
    if 'b' in word:
        guessed.append('b')
        for qw in range(len(word)):
            if word[qw] == 'b':
                progress.set(progress.get()[0:qw]+'b'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonb.config(state=DISABLED)
    else:
        guessed.append('b')
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
                progress.set(progress.get()[0:qw]+'c'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonc.config(state=DISABLED)
        buttonc.config(state=DISABLED)
        countered()
    else:
        guessed.append('c')
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
                progress.set(progress.get()[0:qw]+'d'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttond.config(state=DISABLED)
    else:
        guessed.append('d')
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
                progress.set(progress.get()[0:qw]+'e'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttone.config(state=DISABLED)
    else:
        guessed.append('e')
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
                progress.set(progress.get()[0:qw]+'f'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonf.config(state=DISABLED)
    else:
        guessed.append('f')
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
                progress.set(progress.get()[0:qw]+'g'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttong.config(state=DISABLED)
        buttong.config(state=DISABLED)
    else:
        guessed.append('g')
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
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonh.config(state=DISABLED)
    else:
        guessed.append('h')
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
                progress.set(progress.get()[0:qw]+'i'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttoni.config(state=DISABLED)
    else:
        guessed.append('i')
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
                progress.set(progress.get()[0:qw]+'j'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonj.config(state=DISABLED)
    else:
        guessed.append('j')
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
                progress.set(progress.get()[0:qw]+'k'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonk.config(state=DISABLED)
    else:
        guessed.append('k')
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
                progress.set(progress.get()[0:qw]+'l'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonl.config(state=DISABLED)
    else:
        guessed.append('l')
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
                progress.set(progress.get()[0:qw]+'m'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonm.config(state=DISABLED)
    else:
        guessed.append('m')
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
                progress.set(progress.get()[0:qw]+'n'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonn.config(state=DISABLED)
    else:
        guessed.append('n')
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
                progress.set(progress.get()[0:qw]+'o'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttono.config(state=DISABLED)
    else:
        guessed.append('o')
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
                progress.set(progress.get()[0:qw]+'p'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonp.config(state=DISABLED)
    else:
        guessed.append('p')
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
                progress.set(progress.get()[0:qw]+'q'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonq.config(state=DISABLED)
    else:
        guessed.append('q')
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
                progress.set(progress.get()[0:qw]+'r'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonr.config(state=DISABLED)
    else:
        guessed.append('r')
        counter += 1
        buttonr.config(state=DISABLED)
        countered()

def buttonS():
    global guessed
    global counter
    if 's' in word:
        guessed.append('s')
        for qw in range(len(word)):
            if word[qw] == 's':
                progress.set(progress.get()[0:qw]+'s'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttons.config(state=DISABLED)
    else:
        guessed.append('s')
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
                progress.set(progress.get()[0:qw]+'t'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttont.config(state=DISABLED)
    else:
        guessed.append('t')
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
                progress.set(progress.get()[0:qw]+'u'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonu.config(state=DISABLED)
    else:
        guessed.append('u')
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
                progress.set(progress.get()[0:qw]+'v'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonv.config(state=DISABLED)
    else:
        guessed.append('v')
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
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttona.config(state=DISABLED)
    else:
        guessed.append('w')
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
                progress.set(progress.get()[0:qw]+'x'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonx.config(state=DISABLED)
    else:
        guessed.append('x')
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
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttony.config(state=DISABLED)
    else:
        guessed.append('y')
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
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonz.config(state=DISABLED)
    else:
        guessed.append('z')
        counter += 1
        buttonz.config(state=DISABLED)
        countered()


def buttonA1():
    global guessed
    global counter
    if 'á' in word:
        guessed.append('á')
        for qw in range(len(word)):
            if word[qw] == 'á':
                progress.set(progress.get()[0:qw]+'á'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttoná.config(state=DISABLED)
    else:
        if search(word) is False:
            buttoná.config(state=DISABLED)
        else:
            guessed.append('á')
            counter += 1
            buttoná.config(state=DISABLED)
            countered()


def buttonE1():
    global guessed
    global counter
    if 'é' in word:
        guessed.append('é')
        for qw in range(len(word)):
            if word[qw] == 'é':
                progress.set(progress.get()[0:qw]+'é'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttoná.config(state=DISABLED)
    else:
        if search(word) is False:
            buttoné.config(state=DISABLED)
        else:
            guessed.append('é')
            counter += 1
            buttoné.config(state=DISABLED)
            countered()
            
            
def buttonI1():
    global guessed
    global counter
    if 'í' in word:
        guessed.append('í')
        for qw in range(len(word)):
            if word[qw] == 'í':
                progress.set(progress.get()[0:qw]+'í'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttoní.config(state=DISABLED)
    else:
        if search(word) is False:
            buttoní.config(state=DISABLED)
        else:
            guessed.append('í')
            counter += 1
            buttoní.config(state=DISABLED)
            countered()

            
def buttonO1():
    global guessed
    global counter
    if 'ó' in word:
        guessed.append('ó')
        for qw in range(len(word)):
            if word[qw] == 'ó':
                progress.set(progress.get()[0:qw]+'ó'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttoná.config(state=DISABLED)
    else:
        if search(word) is False:
            buttonó.config(state=DISABLED)
        else:
            guessed.append('ó')
            counter += 1
            buttonó.config(state=DISABLED)
            countered()


def buttonU1():
    global guessed
    global counter
    if 'ú' in word:
        guessed.append('ú')
        for qw in range(len(word)):
            if word[qw] == 'ú':
                progress.set(progress.get()[0:qw]+'ú'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonú.config(state=DISABLED)
    else:
        if search(word) is False:
            buttonú.config(state=DISABLED)
        else:
            guessed.append('ú')
            counter += 1
            buttonú.config(state=DISABLED)
            countered()

            
def buttonU2():
    global guessed
    global counter
    if 'ü' in word:
        guessed.append('ü')
        for qw in range(len(word)):
            if word[qw] == 'ü':
                progress.set(progress.get()[0:qw]+'ü'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonü.config(state=DISABLED)
    else:
        if search(word) is False:
            buttonü.config(state=DISABLED)
        else:
            guessed.append('ü')
            counter += 1
            buttonü.config(state=DISABLED)
            countered()
            
            
def buttonU3():
    global guessed
    global counter
    if 'ű' in word:
        guessed.append('ű')
        for qw in range(len(word)):
            if word[qw] == 'ű':
                progress.set(progress.get()[0:qw]+'ű'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonű.config(state=DISABLED)
    else:
        if search(word) is False:
            buttonű.config(state=DISABLED)
        else:
            guessed.append('ű')
            counter += 1
            buttonű.config(state=DISABLED)
            countered()
            
def buttonO2():
    global guessed
    global counter
    if 'ö' in word:
        guessed.append('ö')
        for qw in range(len(word)):
            if word[qw] == 'ö':
                progress.set(progress.get()[0:qw]+'ö'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonö.config(state=DISABLED)
    else:
        if search(word) is False:
            buttonö.config(state=DISABLED)
        else:
            guessed.append('ö')
            counter += 1
            buttonö.config(state=DISABLED)
            countered()

def buttonO3():
    global guessed
    global counter
    if 'ő' in word:
        guessed.append('ő')
        for qw in range(len(word)):
            if word[qw] == 'ő':
                progress.set(progress.get()[0:qw]+'ő'+progress.get()[1+qw:])
                if("?" not in progress.get()):
                    win()
                    root.destroy()
                if("?" in progress.get()):
                    buttonő.config(state=DISABLED)
    else:
        if search(word) is False:
            buttonő.config(state=DISABLED)
        else:
            guessed.append('ő')
            counter += 1
            buttonő.config(state=DISABLED)
            countered()

def exit():
    import sys
    sys.exit()

# ----------------- Guesses in game ---------------------
def countered():
    if counter == 1:
        wrong_guess1 = v.create_oval(182, 125, 217, 90, fill='black', width=3)
    if counter == 2:
        wrong_guess2 = v.create_line(200, 125, 200, 180, width=3)
    if counter == 3:
        wrong_guess3 = v.create_line(200, 140, 170, 160, width=3)
    if counter == 4:
        wrong_guess4 = v.create_line(200, 140, 230, 160, width=3)
    if counter == 5:
        wrong_guess5 = v.create_line(200, 180, 170, 220, width=3)
    if counter == 6:
        wrong_guess6 = v.create_line(200, 180, 230, 220, width=3)
        lose()
        root.destroy()

# ----------------- Buttons as you see ---------------------

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
buttoná = Button(root, text="á", command=buttonA1)
buttoná.pack(side=LEFT)
buttoné = Button(root, text="é", command=buttonE1)
buttoné.pack(side=LEFT)
buttoní = Button(root, text="í", command=buttonI1)
buttoní.pack(side=LEFT)
buttonó = Button(root, text="ó", command=buttonO1)
buttonó.pack(side=LEFT)
buttonú = Button(root, text="ú", command=buttonU1)
buttonú.pack(side=LEFT)
buttonö = Button(root, text="ö", command=buttonO2)
buttonö.pack(side=LEFT)
buttonő = Button(root, text="ő", command=buttonO3)
buttonő.pack(side=LEFT)
buttonü = Button(root, text="ü", command=buttonU2)
buttonü.pack(side=LEFT)
buttonű = Button(root, text="ű", command=buttonU3)
buttonű.pack(side=LEFT)
buttonEXIT = Button(root, text="Exit", command=exit)
buttonEXIT.pack(side=LEFT)


root.mainloop()


# ----------------- New Game ---------------------
resul = print("The word was: ", word)
replay = input("Wanna play another?: Yes(y) or Not(press any key)")
if replay == "y" or replay == "Y":
    del word_list[:]
    import hangman_v20
else:
    exit()
