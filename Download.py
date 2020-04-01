Laimport youtube_dl
import os
from tkinter import *
from tkinter import Tk, StringVar, Label, Entry, Button
from functools import partial
def down(url, Format):
	url = url.get()
	Format = Format.get()
	if Format == "mp3":

		ydl_opts = {
			'format': 'bestaudio/best',
			'postprocessors': [
				{'key': 'FFmpegExtractAudio','preferredcodec': Format,
			'preferredquality': '390',
			},
			{'key': 'FFmpegMetadata'},
			],
			}
	elif Format != "mp3":
		ydl_opts = {
			'postprocessors': [
				{'key': 'FFmpegVideoConvertor','preferedformat': Format,
			},
			{'key': 'FFmpegMetadata'},
			],
			}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])
	a = 0
	dir  = os.listdir('.')

	for x in dir:
		pr = dir[a]
		a = a+1
		print(pr)
		if pr != "Download.py" and pr !="Done" and pr !="source":
			os.rename(""+str(pr)+"", "Done\\"+str(pr)+"")

root = Tk()
root.title("Amdl")
root.geometry("1920x1080")
root.minsize(400, 300)
root.config(background='#260A85')
frame = Frame(root, bg = "#260A85")
framebis =  Frame(root, bg = "#260A85")
title = Label(root, text = "Welcome in Amdl", font = ("Arial", 25), bg = "#260A85", fg = "#FFFFFF")
title.pack()
text = StringVar(root)
doss = StringVar(root)
url = Entry(framebis, text = "url",textvariable = doss,font = ("Arial", 25), bg = "#FFFFFF", fg = "#260A85" )
url.pack()
ur = Entry(framebis, text = "url",textvariable = text,font = ("Arial", 25), bg = "#FFFFFF", fg = "#260A85" )
ur.pack()
lunch = Button(frame, text = "download",font = ("Arial", 25), bg = "#FFFFFF", fg = "#260A85", command = partial(down, doss,text))
lunch.pack()
frame.pack(side = BOTTOM)
turl = Label(framebis, text = "url", font = ("Arial", 25), bg = "#260A85", fg = "#FFFFFF")
turl.pack()
framebis.pack(expand = YES)
root.mainloop()
