try:
	import os
	import tkinter as tk
	from tkinter import *
	import time
	import pytube
except:
	os.system('pip install pytube')
	os.system('pip3 install pytube')



root = tk.Tk()
root.title('youtube to mp4 video')
root.config(bg='#12171C')

def click():

	if var1.get() == 1:
		main_download_video_open()
	elif var1.get() == 0:
		main_download_video()




def main_download_video():
		try:
			download_button.config(text='this wont take too long...',fg='#758A9B')
			root.update()
			url = str(link_entry.get())

			pytube.YouTube(url).streams.get_highest_resolution().download()
			download_button.config(text='download',fg='#758A9B')
			root.update()

		except Exception as e:
			print(e)
			download_button.config(text='ERROR',fg='red')
			root.update()
			time.sleep(1)
			download_button.config(text='download',fg='#758A9B')







def main_download_video_open():
	try:
		download_button.config(text='this wont take too long...',fg='#758A9B')
		root.update()
		url = str(link_entry.get())

		pytube.YouTube(url).streams.get_highest_resolution().download()
		download_button.config(text='download',fg='#758A9B')
		root.update()
		abc = os.getcwd()
		os.system('explorer '+ abc)
	except Exception as e:
		print(e)
		download_button.config(text='ERROR',fg='red')
		root.update()
		time.sleep(1)
		download_button.config(text='download',fg='#758A9B')
	


var1 = tk.IntVar(value=1)

 

##############
title = Label(root, text='youtube to mp4 converter', font='verdena 35',bg='#12171C',fg='#758A9B')
title.pack()



link_entry = Entry(root,bg='#12171C',fg='#758A9B',font='verdena 16',width=50)
link_entry.pack()


download_button = Button(root, text='download', command=click ,bg='#12171C',fg='#758A9B', font='verdena 20')
download_button.pack()





checkbox = tk.Checkbutton(root, text='open file explorer after download?', variable=var1, onvalue=1, offvalue=0,bg='#12171C',fg='#758A9B', font='verdena 12')
checkbox.pack(side='right')
root.mainloop()
######################
#MADE BY ADAM