from PIL import Image, ImageTk
import tkinter as Tk
from tkinter import ttk,messagebox,PhotoImage
from pytube import YouTube
import pytube
import pytube.request
import threading

pytube.request.default_range_size = 1048576







class Main():
    
    #Create Root object using tkinter
    def __init__(self):
 
        #Window
        Root = Tk.Tk()
        Root.title("YouTube Downloader")
        RootIcon = PhotoImage(file="C:\\Users\\draco\\Documents\\GitHub\\Portfolio\\Youtube Downloader\\Images\\down+download+downloads+icon-1320196066868908267.png")
        Root.iconphoto(False,RootIcon)
        Root.geometry("250x150")
        Root.resizable(0,0)

        #Background Image
        Img = Image.open("C:\\Users\\draco\\Documents\\GitHub\\Portfolio\\Youtube Downloader\\Images\\Background.jpg")
        Background = Img.resize((894,540))
        BackgroundImg = ImageTk.PhotoImage(Background)

        #Canvas
        Canvas = Tk.Canvas(Root,bg = "blue")
        Canvas.create_image(0,0,anchor = "nw",image = BackgroundImg)
        Canvas.place(relx = .5,rely = .5,anchor = "center",relwidth=1,relheight=1)

        #Label
        Canvas.create_text(125,25,text = "PLEASE ENTER URL",fill="white")

        #Input box
        InputBox = Tk.Entry(Root,textvariable = Tk.StringVar(),)
        InputBox.place(relx = .5,rely = 0.325,relwidth= .9,relheight = .15,anchor = "center")

        #Submit Button
        Submit = Tk.Button(Root,text = "Download",command=self.request)
        Submit.place(relx = .5,rely = 0.55,relwidth= .25,relheight = .15,anchor = "center")

        #Progress Bar
        ProgressBar = ttk.Progressbar(Root,orient = "horizontal",mode = "determinate")
        ProgressBar.place(relx = .5,rely = 0.75,relwidth = .75,relheight = .1,anchor = "center")

        self.Root = Root
        self.Canvas = Canvas
        self.InputBox = InputBox
        self.SubmitBtn = Submit
        self.ProgressBar = ProgressBar
        self.Downloading = False

        Root.mainloop()


    #Request download
    def request(self):

        if self.Downloading == True:

            messagebox.showwarning("High Traffic","A download is already in progress please wait")

            return
        else :
             
             self.Downloading = False
        
        try:
             
             self.DownloadVideo() 

        except:
             messagebox.showerror("Invalid URL","The link you have entered is invalid, please try again with a valid link")

        return

    #Download youtube video
    def DownloadVideo(self):

        URL = self.GetUrl()
        Video = YouTube(URL)
        Video.register_on_progress_callback(self.OnDownloadProgress)
        Video.register_on_complete_callback(self.OnDownloadComplete)
        Stream = Video.streams.get_highest_resolution()
    
        threading.Thread(target = Stream.download).start()

        return

    # Get Link of 
    def GetUrl(self):
        
        Input = self.InputBox.get()
        Link = str(Input)
    
        return Link

    #Download progress update callbacks
    def OnDownloadProgress(self,Stream, Chunk, Remaining):

        Percent = int((Stream.filesize - Remaining) / Stream.filesize * 100)
 
        self.ProgressBar['value'] = Percent

        return

    #Download completion callback
    def OnDownloadComplete(self,Stream, Dir):

        messagebox.showwarning("Complete","Sucecessfully downloaded file")
        
        self.ProgressBar['value'] = 0

        return

 




Root = Main()