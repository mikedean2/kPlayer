from tkinter import *
import pygame
from pygame import mixer
import random

pygame.init()

window = Tk()
window.geometry('400x400')
window.title("kPlayer")

rs = 1  # USED FOR PLAYLIST-STYLE SKIP

def prints():
    global rs
    if rs == 1:
        photo['file'] = "e072b707a344a7ea2314be417624d446.png"
        mixer.music.load("Alien - Yandhi.mp3")
        mixer.music.play()
        playing['text'] = 'Now Playing: Alien'
        art['text'] = 'By Kanye West, Ant Clemons, and Kid Cudi'
        rs +=1
    elif rs == 2:
        mixer.music.load("New Body - Yandhi.mp3")
        mixer.music.play()
        playing['text'] = 'Now Playing: New Body'
        art['text'] = 'By Kanye West, Ty Dolla $ign, and Nicki Minaj'
        rs += 1
    elif rs == 3:
        mixer.music.load("Sky City - Yandhi.mp3")
        mixer.music.play()
        playing['text'] = 'Now Playing: Sky City'
        art['text'] = 'By Kanye West, Ty Dolla $ign, 070 Shake, Jeremih, Desiigner, and Kid Cudi'
        rs += 1
    elif rs == 4:
        rs += 1
        mixer.music.load("Last Name - Yandhi.mp3")
        mixer.music.play()
        playing['text'] = 'Now Playing: Last Name'
        art['text'] = 'By Kanye West and Ant Clemons'
    elif rs == 5:
        photo['file'] = "dndaimg.png"
        rs += 1
        mixer.music.load("01 TRUE LOVE.mp3")
        mixer.music.play()
        playing['text'] = 'Now Playing: True Love'
        art['text'] = 'By Kanye West and XXXTentacion'
    elif rs == 5:
        rs += 1
        mixer.music.load("02 BROKEN ROAD.mp3")
        mixer.music.play()
        playing['text'] = 'Now Playing: True Love'
        art['text'] = 'By Kanye West and Don Toliver'
    elif rs == 6:
        rs += 1
        mixer.music.load("03 GET LOST.mp3")
        mixer.music.play()
        playing['text'] = 'Now Playing: Get Lost'
        art['text'] = 'By Kanye West'
    elif rs == 7:
        rs += 1
        mixer.music.load("04 TOO EASY.mp3")
        mixer.music.play()
        playing['text'] = 'Now Playing: Too Easy'
        art['text'] = 'By Kanye West'
    elif rs == 8:
        rs += 1
        mixer.music.load("05 FLOWERS.mp3")
        mixer.music.play()
        playing['text'] = 'Now Playing: Flowers'
        art['text'] = 'By Kanye West'
    elif rs == 9:
        rs += 1
        mixer.music.load("06 SECURITY.mp3")
        mixer.music.play()
        playing['text'] = 'Now Playing: Security'
        art['text'] = 'By Kanye West'
    elif rs == 10:
        rs += 1
        mixer.music.load("07 WE DID IT KID.mp3")
        mixer.music.play()
        playing['text'] = 'Now Playing: We Did It Kid'
        art['text'] = 'By Kanye West, Baby Keem, Fivio Foreign, and Migos'
    elif rs == 11:
        rs += 1
        mixer.music.load("08 PABLO.mp3")
        mixer.music.play()
        playing['text'] = 'Now Playing: Pablo'
        art['text'] = 'By Kanye West, Future, and Travis Scott'
    elif rs == 12:
        rs += 1
        mixer.music.load("09 LOUIE BAGS.mp3")
        mixer.music.play()
        playing['text'] = 'Now Playing: Louie Bags'
        art['text'] = 'By Kanye West and Jack Harlow'
    elif rs == 13:
        rs += 1
        mixer.music.load("10 HAPPY.mp3")
        mixer.music.play()
        playing['text'] = 'Now Playing: Happy'
        art['text'] = 'By Kanye West and Future'
    elif rs == 14:
        rs += 1
        mixer.music.load("11 SCI FI.mp3")
        mixer.music.play()
        playing['text'] = 'Now Playing: Sci Fi'
        art['text'] = 'By Kanye West and Sean Leon'
    elif rs == 15:
        rs += 1
        mixer.music.load("12 SELFISH.mp3")
        mixer.music.play()
        playing['text'] = 'Now Playing: Selfish'
        art['text'] = 'By Kanye West and XXXTentacion'
    elif rs == 15:
        rs += 1
        mixer.music.load("13 LORD LIFT ME UP.mp3")
        mixer.music.play()
        playing['text'] = 'Now Playing: Lord Lift Me Up'
        art['text'] = 'By Kanye West and Vory'
    elif rs == 16:
        rs = 1
        mixer.music.load("16 FIRST TIME IN A LONG TIME.mp3")
        mixer.music.play()
        playing['text'] = 'Now Playing: First Time In A Long Time'
        art['text'] = 'By Kanye West and Solja Boy'



def pause():
    mixer.music.load("silence.mp3")
    mixer.music.play()
    window.title("kPlayer")
    playing['text'] = 'Playing Nothing'
    art['text'] = 'By Artist'


title = Label(text="kPlayer v0.8", font="Arial 16")
title.place(anchor='center', relx=.5, rely=.1)
title = Label(text="Please check if you are using the latest version manually")
title.place(anchor='center', relx=.5, rely=.15)

playing = Label(text="Nothing Playing", font="Arial 13")
playing.place(anchor='center', relx=.5, rely=.92)
art = Label(text="By Artist")
art.place(anchor='center', relx=.5, rely=.97)

canvas = Canvas(width=245, height=235, bg='blue')
canvas.place(anchor='center', relx=.5, rely=.6)
photo = PhotoImage(file='e072b707a344a7ea2314be417624d446.png')
canvas.create_image(0, 0, image=photo, anchor=NW)

skip = Button(window, text="Skip/Play", command=prints)
skip.place(anchor='center', relx=.44, rely=.21)
pause = Button(window, text="Stop", command=pause)
pause.place(anchor='center', relx=.57, rely=.21)

window.mainloop()
