import tkinter as tk
import os
import youtube_dl
import tkinter.font as tkfont
from tkinter import *
from tkinter.ttk import *

# i need dat window
root = tk.Tk()

pic = PhotoImage(file="qqq.pgm")
root.iconphoto(False, pic)

root.title("Youtube DL")
root.geometry("400x400")
root.resizable(width=FALSE, height=FALSE)

# canvas
cvs1 = tk.Canvas(root, height=600, width=600, bg="#263d42")
cvs1.pack()

bold_font = tkfont.Font(family="Arial", size=16, weight="bold")

label1 = tk.Label(root, text="Enter URL", width=12, bg="#FFFFFF")
label1.config(font=bold_font)

cvs1.create_window(200, 100, window=label1)

download_box = tk.Entry(root, width=60)
cvs1.create_window(200, 140, window=download_box)


def yt_dl():
    # get URL
    search_item = download_box.get()
    # format
    ydl_opts = {
        "format": "best",
        "noplaylist": True,
        "extract-audio": True,
    }
    # dest
    os.chdir("c:/ytdl/")
    # dlfile
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_item])


##DL MESSAGE##
bold_font2 = tkfont.Font(family="Arial", size=10, weight="bold")
# label
label2 = tk.Label(root, text="Downloaded", width=20, bg="#FFFFFF")
label2.config(font=bold_font2)
cvs1.create_window(200, 300, window=label2)

dlbutton = tk.Button(text="Download", padx=5, pady=5,
                     fg="white", bg="DeepSkyBlue4", command=yt_dl)
cvs1.create_window(200, 230, window=dlbutton)

root.mainloop()
