from tkinter import *
from PIL import ImageTk, Image
import os
from pygame import mixer

#colours
co1 = "#ffffff" #white
co2 = "#3C1DC6" #purple
co3 = "#333333" #black
co4 = "#CFC7F8" #light purple

window = Tk()
window.title("")
window.geometry('352x255')
window.configure(background=co1)
window.resizable(width=FALSE , height=FALSE)

#events
def play_music():
    running = listbox.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def continue_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def next_music():
    playing = running_song['text']
    index= songs.index(playing)
    new_index = index+1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()


    listbox.delete(0, END)
    show()
    listbox.select_set(new_index)
    running_song['text'] = playing


def prev_music():
    playing = running_song['text']
    index= songs.index(playing)
    new_index = index-1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()


    listbox.delete(0, END)
    show()
    listbox.select_set(new_index)
    running_song['text'] = playing
    
    #frames
left_frame = Frame(window , width=150 , height=150 , background=co1)
left_frame.grid(row=0 , column=0 , padx=1 , pady=1)

right_frame = Frame(window , width=250 , height=150 , background=co3)
right_frame.grid(row=0 , column=1 , padx=0)

down_frame = Frame(window , width=400 , height=100 , background=co4)
down_frame.grid(row=1 , column=0 ,columnspan=3, padx=0 , pady=1)

#right frame songs
listbox = Listbox(right_frame , selectmode=SINGLE , font=("Arial 9 bold") , width=22, bg=co3 , fg=co1)
listbox.grid(row=0 , column=0)


w = Scrollbar(right_frame)
w.grid(row=0 , column=1)

listbox.config(yscrollcommand=w.set)
w.config(command=listbox.yview)

#images
image1 = Image.open('Icons/3.png')
image1  = image1.resize((120, 120))
image1 = ImageTk.PhotoImage(image1)
app_image = Label(left_frame , height=130 , image=image1 , padx=10 , bg=co1)
app_image.place(x = 10 , y =15)


#buttons
image2 = Image.open('Icons/5.png')
image2  = image2.resize((30, 30))
image2 = ImageTk.PhotoImage(image2)
play_button = Button(down_frame ,width=40, height=40 , image=image2 , padx=10 , bg=co1, font=("Ivy 10"), command=play_music)
play_button.place(x =56+28 , y =35)

image3 = Image.open('Icons/2.png')
image3  = image3.resize((30, 30))
image3 = ImageTk.PhotoImage(image3)
prev_button = Button(down_frame ,width=40, height=40 , image=image3 , padx=10 , bg=co1, font=("Ivy 10"), command=prev_music)
prev_button.place(x =10+28 , y =35)

image4 = Image.open('Icons/1.png')
image4  = image4.resize((30, 30))
image4 = ImageTk.PhotoImage(image4)
next_button = Button(down_frame ,width=40, height=40 , image=image4 , padx=10 , bg=co1, font=("Ivy 10"), command=next_music)
next_button.place(x = 102+28 , y =35)
 
image5 = Image.open('Icons/7.png')
image5 = image5.resize((30, 30))
image5 = ImageTk.PhotoImage(image5)
pause_button = Button(down_frame ,width=40, height=40 , image=image5 , padx=10 , bg=co1, font=("Ivy 10"), command=pause_music)
pause_button.place(x =148+28 , y =35)

image6 = Image.open('Icons/4.png')
image6  = image6.resize((30, 30))
image6 = ImageTk.PhotoImage(image6)
countinue_button = Button(down_frame ,width=40, height=40 , image=image6 , padx=10 , bg=co1, font=("Ivy 10"), command=continue_music)
countinue_button.place(x =194+28 , y =35)

image7 = Image.open('Icons/6.png')
image7  = image7.resize((30, 30))
image7 = ImageTk.PhotoImage(image7)
stop_button = Button(down_frame ,width=40, height=40 , image=image7 , padx=10 , bg=co1, font=("Ivy 10"), command=stop_music)
stop_button.place(x =240+28 , y =35)



line =  Label(left_frame, height=1 , width=200 , padx=10 , bg=co3)
line.place(x = 0 , y = 1) 

line =  Label(left_frame, height=1 , width=200 , padx=10 , bg=co1)
line.place(x = 0 , y = 3) 

running_song  = Label(down_frame, text = "Choose a song" , width=44 , height=1 , font=("Ivy 10 ") , padx=10 , bg=co1 , fg=co3, anchor=NW)
running_song.place(x = 0 , y = 1)


os.chdir(r'C:\Users\kavya\Dropbox\CodeClause\songs')
songs = os.listdir()
def show():
    for i in songs:
        listbox.insert(END, i)

show()       

mixer.init()
music_state = StringVar()
music_state.set("Choose one!")

 
window.mainloop()