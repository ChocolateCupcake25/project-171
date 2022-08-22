# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 14:13:28 2022

@author: Fierce Bird//Ziyah Virani
"""

from tkinter import*
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root = Tk()
root.title("Global time")
root.geometry("600x600")
root.configure(bg="green yellow")
India_image = ImageTk.PhotoImage(Image.open("India.png"))
Angola_image = ImageTk.PhotoImage(Image.open("Angola.png"))
Canada_image = ImageTk.PhotoImage(Image.open("Canada.jpg"))
Australia_image = ImageTk.PhotoImage(Image.open("Australia.jpg"))

#--India--
india_label=Label(root,text="India")
india_label.place(relx=0.2,rely=0.05,anchor=CENTER)

india_image=Label(root)
india_image["image"]=India_image
india_image.place(relx=0.2,rely=0.35,anchor=CENTER)

india_time = Label(root,text="Time - ")
india_time.place(relx=0.2,rely=0.65,anchor=CENTER)

#--Angola--
angola_label=Label(root,text="Angola")
angola_label.place(relx=0.7,rely=0.05,anchor=CENTER)

angola_image=Label(root)
angola_image["image"]=Angola_image
angola_image.place(relx=0.7,rely=0.35,anchor=CENTER)

angola_time = Label(root,text="Time - ")
angola_time.place(relx=0.7,rely=0.65,anchor=CENTER)

#--Canada--
Canada_label=Label(root,text="Canada")
Canada_label.place(relx=0.4,rely=0.05,anchor=CENTER)

Canada_image=Label(root)
Canada_image["image"]=Canada_image
Canada_image.place(relx=0.4,rely=0.35,anchor=CENTER)

Canada_time = Label(root,text="Time - ")
Canada_time.place(relx=0.4,rely=0.65,anchor=CENTER)

#--Australia--
Australia_label=Label(root,text="Australia")
Australia_label.place(relx=0.9,rely=0.05,anchor=CENTER)

Australia_image=Label(root)
Australia_image["image"]=Australia_image
Australia_image.place(relx=0.9,rely=0.35,anchor=CENTER)

Australia_time = Label(root,text="Time - ")
Australia_time.place(relx=0.9, rely=0.65, anchor=CENTER)

#----Code---Classes---------
class India():
    def time(self):
        home=pytz.timezone("Asia/Kolkata")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H : %M : %S")
        india_time["text"]="Time = " + current_time
        india_time.after(100,self.time)
class Angola():
    def time(self):
        home=pytz.timezone("Africa/Luanda")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H : %M : %S")
        angola_time["text"]="Time = " + current_time
        angola_time.after(100,self.time)
class Canada():
    def time(self):
        home=pytz.timezone("America/Vancouver")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H : %M : %S")
        Canada_time["text"]="Time = " + current_time
        Canada_time.after(100,self.time)
class Australia():
    def time(self):
        home=pytz.timezone("Australia/ACT")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H : %M : %S")
        Australia_time["text"]="Time = " + current_time
        Australia_time.after(100,self.time)

India_obj = India()
Angola_obj = Angola()
Canada_obj = Canada()
Australia_obj = Australia()

India_btn=Button(root,text="India Time",command=India_obj.time)
India_btn.place(relx=0.2,rely=0.8,anchor=CENTER)

Angola_btn=Button(root,text="Angola Time",command=Angola_obj.time)
Angola_btn.place(relx=0.7,rely=0.8,anchor=CENTER)

Canada_btn=Button(root,text="Canada Time",command=Canada_obj.time)
Canada_btn.place(relx=0.4,rely=0.8,anchor=CENTER)

Australia_btn=Button(root,text="Australia Time",command=Australia_obj.time)
Australia_btn.place(relx=0.9,rely=0.8,anchor=CENTER)


root.mainloop()










