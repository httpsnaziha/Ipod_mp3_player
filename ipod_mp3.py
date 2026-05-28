import pygame as pg
import tkinter as tk
from PIL import Image, ImageTk

# --------------------------colors----------------------
gray = "#e9f0fa"
pink = "#fbe2ed"
black = "#000000"
white = "#ffffff"

pg.mixer.init()

window = tk.Tk()
window.title("iPod Music Player")
window.geometry("600x250")
window.resizable(False, False)
window.configure(bg=gray)

#---------------------------icons----------------------
next_icon = Image.open("next.png")
next_icon = next_icon.resize((30, 30), Image.LANCZOS)
next_icon = ImageTk.PhotoImage(next_icon)

prev_icon = Image.open("previous.png")
prev_icon = prev_icon.resize((30, 30), Image.LANCZOS)
prev_icon = ImageTk.PhotoImage(prev_icon)

pause_icon = Image.open("pause.png")
pause_icon = pause_icon.resize((30, 30), Image.LANCZOS)
pause_icon = ImageTk.PhotoImage(pause_icon)

# -------------------------music choices screen----------------------
frame = tk.Frame(window, width=300, height=200, bg=pink,
                 highlightbackground=black, highlightthickness=5)
frame.place(relx=0.05, rely=0.1)


# -------------------------buttons---------------------------------
canvas = tk.Canvas(window, width=300, height=300, bg=gray, bd=0,highlightthickness=0)
canvas.pack()
#main circle
canvas.create_oval(50, 50, 240, 240, fill=white, outline="#BBBEC3", width=1)

# Inner gray circle 
inner_circle = canvas.create_oval(105, 105, 185, 185, fill=gray, outline=gray, width=1)

#play button on the inner circle
def on_inner_click():
     resume_music()

def on_hover_enter(event):
    canvas.itemconfig(inner_circle, fill="#d3dce8")
    canvas.config(cursor="hand2")

def on_hover_leave(event):
    canvas.itemconfig(inner_circle, fill=gray)
    canvas.config(cursor="")

canvas.tag_bind(inner_circle, "<Button-1>", lambda e: play_pause())
canvas.tag_bind(inner_circle, "<Enter>", on_hover_enter)
canvas.tag_bind(inner_circle, "<Leave>", on_hover_leave)
canvas.tag_bind(inner_circle, "<Button-1>", lambda e: on_inner_click())
#menu button
menu_button = tk.Button(canvas, text="MENU", fg="#BBBEC3", font=("Ivy 10", 15),bg=white, bd=0, highlightthickness=0)
canvas.create_window(145, 82, window=menu_button)

# Pause button 
play_pause_button = tk.Button(canvas, image=pause_icon, bg=white, bd=0, highlightthickness=0)
canvas.create_window(145, 212, window=play_pause_button)

# Previous button — left side of circle
prev_button = tk.Button(canvas, image=prev_icon, bg=white, bd=0, highlightthickness=0)
canvas.create_window(75, 145, window=prev_button)

# Next button — right side of circle
next_button = tk.Button(canvas, image=next_icon, bg=white, bd=0, highlightthickness=0)
canvas.create_window(215, 145, window=next_button)

canvas.place(relx=0.55, rely=-0.08)
# --------------------------------------------------------------------

#--------functions---------
def play_music():
    pg.mixer.music.load("song.mp3")
    pg.mixer.music.play()

def pause_music():
    pg.mixer.music.pause()

def resume_music():
    pg.mixer.music.unpause()

window.mainloop()