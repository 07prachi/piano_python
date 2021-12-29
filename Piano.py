import pygame
from tkinter import *

pygame.init()

def note_Cs():
    num1.set("C#")
    sound = pygame.mixer.Sound("C:\python lab\piano notes\Music_Notes\C_s.wav")
    sound.play()
    return

def note_Ds():
    num1.set("D#")
    sound = pygame.mixer.Sound("C:\python lab\piano notes\Music_Notes\D_s.wav")
    sound.play()
    return

def note_Fs():
    num1.set("F#")
    sound = pygame.mixer.Sound("C:\python lab\piano notes\Music_Notes\F_s.wav")
    sound.play()
    return

def note_Gs():
    num1.set("G#")
    sound = pygame.mixer.Sound("C:\python lab\piano notes\Music_Notes\G_s.wav")
    sound.play()
    return

def note_Bb():
    num1.set("Bb")
    sound = pygame.mixer.Sound("C:\python lab\piano notes\Music_Notes\Bb.wav")
    sound.play()
    return

def note_Cs1():
    num1.set("C#1")
    sound = pygame.mixer.Sound("C:\python lab\piano notes\Music_Notes\C_s1.wav")
    sound.play()
    return

def note_Ds1():
    num1.set("D#1")
    sound = pygame.mixer.Sound("C:\python lab\piano notes\Music_Notes\D_s1.wav")
    sound.play()
    return

def note_C():
    num1.set("C")
    sound = pygame.mixer.Sound("C:\python lab\piano notes\Music_Notes\C.wav")
    sound.play()
    return

def note_D():
    num1.set("D")
    sound = pygame.mixer.Sound("C:\python lab\piano notes\Music_Notes\D.wav")
    sound.play()
    return

def note_E():
    num1.set("E")
    sound = pygame.mixer.Sound("C:\python lab\piano notes\Music_Notes\E.wav")
    sound.play()
    return

def note_F():
    num1.set("F")
    sound = pygame.mixer.Sound("C:\python lab\piano notes\Music_Notes\F.wav")
    sound.play()
    return

def note_G():
    num1.set("G")
    sound = pygame.mixer.Sound("C:\python lab\piano notes\Music_Notes\G.wav")
    sound.play()
    return

def note_A():
    num1.set("A")
    sound = pygame.mixer.Sound("C:\python lab\piano notes\Music_Notes\A.wav")
    sound.play()
    return

def note_B():
    num1.set("B")
    sound = pygame.mixer.Sound("C:\python lab\piano notes\Music_Notes\B.wav")
    sound.play()
    return

def note_C1():
    num1.set("C1")
    sound = pygame.mixer.Sound("C:\python lab\piano notes\Music_Notes\C1.wav")
    sound.play()
    return

def note_D1():
    num1.set("D1")
    sound = pygame.mixer.Sound("C:\python lab\piano notes\Music_Notes\D1.wav")
    sound.play()
    return

def note_E1():
    num1.set("E1")
    sound = pygame.mixer.Sound("C:\python lab\piano notes\Music_Notes\E1.wav")
    sound.play()
    return

def note_F1():
    num1.set("F1")
    sound = pygame.mixer.Sound("C:\python lab\piano notes\Music_Notes\F1.wav")
    sound.play()
    return

#creating a window and frame
window = Tk()
frame = Frame(window)
frame.pack()

#title of the window
window.title("Piano")
num1 = StringVar()


#name of the note which is being played
textDis = Entry(frame, textvariable = num1, bd = 20, insertwidth = 1, font = 30, justify = 'center', width = 4)
textDis.pack(side = TOP)

#two frames are created for two rows of keys
#this is the top frame
topframe = Frame(frame, bd=20)
topframe.pack(side = TOP)

#all the buttons in the top frame
# key C#
button1 = Button(topframe, padx = 8, height = 6, pady = 8, bd = 8, text = "C#", bg = "black", fg = "white", command = note_Cs)
button1.pack(side = LEFT)

# space between keys C# and D#
button22 = Button(topframe, state = DISABLED, height = 7, width = 1, padx = 0, pady = 0, relief = RIDGE)
button22.pack(side = LEFT)

# key D#
button2 = Button(topframe, padx = 8, height = 6, pady = 8, bd = 8, text = "D#", bg = "black", fg = "white", command = note_Ds)
button2.pack(side = LEFT)

#space between keys D# and F#
button22 = Button(topframe, state = DISABLED, height = 7, width = 4, padx = 0, pady = 0, relief = RIDGE)
button22.pack(side = LEFT)

# key F#
button3 = Button(topframe, padx = 8, height = 6, pady = 8, bd = 8, text = "F#", bg = "black", fg = "white", command = note_Fs)
button3.pack(side = LEFT)

# space between keys F# and G#
button22 = Button(topframe, state = DISABLED, height = 7, width = 1, padx = 0, pady = 0, relief = RIDGE)
button22.pack(side = LEFT)

# key G#
button4 = Button(topframe, padx = 8, height = 6, pady = 8, bd = 8, text = "G#", bg = "black", fg = "white", command = note_Gs)
button4.pack(side = LEFT)

# space between keys G# and Bb
button22 = Button(topframe, state = DISABLED, height = 7, width = 4, padx = 0, pady = 0, relief = RIDGE)
button22.pack(side = LEFT)

# key Bb
button2 = Button(topframe, padx = 8, height = 6, pady = 8, bd = 8, text = "Bb", bg = "black", fg = "white", command = note_Bb)
button2.pack(side = LEFT)

# space between keys Bb and C#1
button22 = Button(topframe, state = DISABLED, height = 7, width = 1, padx = 0, pady = 0, relief = RIDGE)
button22.pack(side = LEFT)

# key C#1
button3 = Button(topframe, padx = 8, height = 6, pady = 8, bd = 8, text = "C#1", bg = "black", fg = "white", command = note_Cs1)
button3.pack(side = LEFT)

# space between keys C#1 and D#1
button22 = Button(topframe, state = DISABLED, height = 7, width = 1, padx = 0, pady = 0, relief = RIDGE)
button22.pack(side = LEFT)

# key D#1
button4 = Button(topframe, padx = 8, height = 6, pady = 8, bd = 8, text = "D#1", bg = "black", fg = "white", command = note_Ds1)
button4.pack(side = LEFT)

#this is the bottom frame
frame1 = Frame(frame, bd =20)
frame1.pack(side = TOP)

#all the keys in the bottom frame

# key C
button1 = Button(frame1, padx = 16, pady = 16, height=6, bd = 8, text = "C", fg = "black", command = note_C)
button1.pack(side = LEFT)

# key D
button2 = Button(frame1, padx = 16, pady = 16, height=6, bd = 8, text = "D", fg = "black", command = note_D)
button2.pack(side = LEFT)

# key E
button3 = Button(frame1, padx = 16, pady = 16, height=6, bd = 8, text = "E", fg = "black", command = note_E)
button3.pack(side = LEFT)

# key F
button4 = Button(frame1, padx = 16, pady = 16, height=6, bd = 8, text = "F", fg = "black", command = note_F)
button4.pack(side = LEFT)

# key G
button5 = Button(frame1, padx = 16, pady = 16, height=6, bd = 8, text = "G", fg = "black", command = note_G)
button5.pack(side = LEFT)

# key A
button6 = Button(frame1, padx = 16, pady = 16, height=6, bd = 8, text = "A", fg = "black", command = note_A)
button6.pack(side = LEFT)

# key B
button7 = Button(frame1, padx = 16, pady = 16, height=6, bd = 8, text = "B", fg = "black", command = note_B)
button7.pack(side = LEFT)

# key C1
button8 = Button(frame1, padx = 16, pady = 16, height=6, bd = 8, text = "C1", fg = "black", command = note_C1)
button8.pack(side = LEFT)

# key D1
button9 = Button(frame1, padx = 16, pady = 16, height=6, bd = 8, text = "D1", fg = "black", command = note_D1)
button9.pack(side = LEFT)

# key E1
button10 = Button(frame1, padx = 16, pady = 16, height=6, bd = 8, text = "E1", fg = "black", command = note_E1)
button10.pack(side = LEFT)

# key F1
button11 = Button(frame1, padx = 16, pady = 16, height=6, bd = 8, text = "F1", fg = "black", command = note_F1)
button11.pack(side = LEFT)



window.mainloop()
