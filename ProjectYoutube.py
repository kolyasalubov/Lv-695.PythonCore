from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("DataFlair-youtube video downloader")

Label(root, text='Youtube Video Downloader', font='arial 20 bold').pack()

##enter link
link = StringVar()

Label(root, text='Paste Link Here:', font='arial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)


# function to download video


def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)


Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2, command=Downloader).place(x=180,
                                                                                                            y=150)

root.mainloop()
# from pytube import YouTube
#
# #ask for the link from user
# link = input("Enter the link of YouTube video you want to download:  ")
# yt = YouTube(link)
#
# #Showing details
# print("Title: ",yt.title)
# print("Number of views: ",yt.views)
# print("Length of video: ",yt.length)
# print("Rating of video: ",yt.rating)
# #Getting the highest resolution possible
# ys = yt.streams.get_highest_resolution()
#
# #Starting download
# print("Downloading...")
# ys.download()
# print("Download completed!!")