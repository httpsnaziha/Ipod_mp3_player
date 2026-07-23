import pygame as pg
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
# --------------------------colors----------------------
gray = "#bcc6d4"
pink = "#f8dbe8"
black = "#000000"
white = "#ffffff"

pg.mixer.init()
window = tk.Tk()
window.title("iPod Music Player")
window.geometry("600x250")
window.resizable(False, False)
window.configure(bg=gray)
window.iconbitmap("icons//favicon.ico")
# ---------------------------icons----------------------
next_icon = Image.open("icons/next.png")
next_icon = next_icon.resize((30, 30), Image.LANCZOS)
next_icon = ImageTk.PhotoImage(next_icon)

prev_icon = Image.open("icons/previous.png")
prev_icon = prev_icon.resize((30, 30), Image.LANCZOS)
prev_icon = ImageTk.PhotoImage(prev_icon)

pause_icon = Image.open("icons/pause.png")
pause_icon = pause_icon.resize((30, 30), Image.LANCZOS)
pause_icon = ImageTk.PhotoImage(pause_icon)

# -------------------------functions---------------------------------
music = []
current_index = [0]

def play_music(index=0):
    if music:
        pg.mixer.music.load(music[index])
        pg.mixer.music.play()
        current_index[0] = index
        song_name = os.path.basename(music[index])
        now_playing_label.config(text=f">>{song_name}˖ ܁♬⋆")
        
        music_listbox.selection_clear(0, tk.END)
        music_listbox.selection_set(index)
        music_listbox.see(index)

def pause_music():
    pg.mixer.music.pause()

def resume_music():
    pg.mixer.music.unpause()

def resume_pause():
    if pg.mixer.music.get_busy():
        pause_music()
    else:
        resume_music()

def next_song():
    if music:
        play_music((current_index[0] + 1)%len(music))

def prev_song():
    if music:
        play_music((current_index[0] - 1)%len(music))

def add_music():
    directory = filedialog.askdirectory(initialdir=".", title="Select MP3 Directory")
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.lower().endswith(".mp3")]
  
    for full_path in files:
        if full_path not in music:
            music.append(full_path)
    if files:
        show()
        music_screen()

def auto_load():
    if os.path.exists("music"):
        for filename in os.listdir("music"):
            if filename.endswith(".mp3"):
                music.append(os.path.join("music", filename))

def show():
    music_listbox.delete(0, tk.END)
    for i, path in enumerate(music, 1):
        music_listbox.insert(tk.END, f"  {i}. {os.path.basename(path)}")

def show_main_menu():
    music_frame.place_forget()
    settings_frame.place_forget()
    main_frame.place(relx=0.05, rely=0.1)

def music_screen():
    main_frame.place_forget()
    settings_frame.place_forget()
    music_frame.place(relx=0.05, rely=0.1)
    show()

def setting_screen():
    main_frame.place_forget()
    music_frame.place_forget()
    settings_frame.place(relx=0.05, rely=0.1)

def on_listbox_select(event):
    selection = listbox.curselection()
    if not selection:
        return
    choice = listbox.get(selection[0])
    if choice == " > Music":
        music_screen()
    elif choice == " > Settings":
        setting_screen()
    elif choice == " > Files":
        add_music()

def on_music_select(event):
    selection = music_listbox.curselection()
    if not selection:
        return
    play_music(selection[0])

# -------------------------main menu frame----------------------
main_frame = tk.Frame(window, width=300, height=200, bg=pink,
                      highlightbackground=black, highlightthickness=5)
main_frame.place(relx=0.05, rely=0.1)
main_frame.pack_propagate(False)

label_main = tk.Label(main_frame, text="iPod", bg=pink, fg=black, font=("Ivy 10", 14, "bold"))
label_main.pack(pady=(5, 3))

listbox = tk.Listbox(main_frame, height=10, width=30, bg=pink, fg=black,
                     font=("Ivy 10", 13), bd=0, selectbackground="#e8a0c0", activestyle="none")

listbox.pack(fill=tk.BOTH, expand=True)
listbox.insert(tk.END, " > Music")
listbox.insert(tk.END, " > Files")
listbox.insert(tk.END, " > Settings")
listbox.bind("<<ListboxSelect>>", on_listbox_select)


# -------------------------music screen frame----------------------
music_frame = tk.Frame(window, width=300, height=200, bg=pink,
                       highlightbackground=black, highlightthickness=5)
music_frame.pack_propagate(False)

back_btn = tk.Button(music_frame, text="< Back", bg=pink, fg=black,
                     font=("Ivy 10", 10), bd=0, highlightthickness=0,
                     command=show_main_menu, cursor="hand2")
back_btn.pack(anchor="w", padx=5, pady=(3, 0))

now_playing_label = tk.Label(music_frame, text="‧₊ ♪˚⊹NO SONG PLAYING‧₊ ♪˚⊹", bg=pink,
                             fg="#888", font=("Ivy 10", 9), anchor="w")
now_playing_label.pack(fill=tk.X, padx=8)

music_listbox = tk.Listbox(music_frame, height=7, width=30, bg=pink, fg=black,
                           font=("Ivy 10", 11), bd=0, selectbackground="#e8a0c0",
                           activestyle="none")
music_listbox.pack(fill=tk.BOTH, expand=True, padx=4)
music_listbox.bind("<<ListboxSelect>>", on_music_select)
auto_load()
# -------------------------settings screen frame----------------------
settings_frame = tk.Frame(window, width=300, height=200, bg=pink,
                          highlightbackground=black, highlightthickness=5)
settings_frame.pack_propagate(False)

settings_back_btn = tk.Button(settings_frame, text="< Back", bg=pink, fg=black,
                              font=("Ivy 10", 10), bd=0, highlightthickness=0,
                              command=show_main_menu, cursor="hand2")
settings_back_btn.pack(anchor="w", padx=5, pady=(3, 0))

settings_title = tk.Label(settings_frame, text="Settings", bg=pink, fg=black,
                          font=("Ivy 10", 13, "bold"), anchor="w")
settings_title.pack(fill=tk.X, padx=10, pady=(5, 0))

coming_soon_label = tk.Label(settings_frame, text="Coming Soon...", bg=pink, fg="#888",
                             font=("Ivy 10", 11))
coming_soon_label.pack( padx=10, pady=20)


tk.Label(settings_frame, text="────────────────────", bg=pink, fg="#cca0b8",
         font=("Ivy 10", 9)).pack(fill=tk.X, padx=10)


# -------------------------buttons---------------------------------
canvas = tk.Canvas(window, width=300, height=300, bg=gray, bd=0, highlightthickness=0)
canvas.pack()

# main circle
canvas.create_oval(50, 50, 240, 240, fill=white, outline="#BBBEC3", width=1)

# Inner circle
inner_circle = canvas.create_oval(105, 105, 185, 185, fill=gray, outline=gray, width=1)

canvas.tag_bind(inner_circle, "<Button-1>", lambda e: resume_pause())

# menu button
menu_button = tk.Button(canvas, text="MENU", fg="#BBBEC3", font=("Ivy 10", 15),
                        bg=white, bd=0, highlightthickness=0, command=show_main_menu)
canvas.create_window(145, 82, window=menu_button)

# pause button
pause_button = tk.Button(canvas, bd=0,image=pause_icon, bg=white,
                        highlightthickness=0, command=pause_music)
canvas.create_window(145, 212, window=pause_button)

# Previous button
prev_button = tk.Button(canvas, image=prev_icon, bg=white, bd=0,
                        highlightthickness=0, command=prev_song)
canvas.create_window(75, 145, window=prev_button)

# Next button
next_button = tk.Button(canvas, image=next_icon, bg=white, bd=0,
                        highlightthickness=0, command=next_song)
canvas.create_window(215, 145, window=next_button)

canvas.place(relx=0.55, rely=-0.08)

window.mainloop()