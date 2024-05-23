from tkinter import*
from tkinter import ttk
import requests


def data_get():
  city = city_name.get()
  data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=20a01944eda34a13f4a4dcecfff77197").json()
  w_label1.config(text=data["weather"][0]["main"])
  wb_label1.config(text=data["weather"][0]["description"])
  temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
  per_label1.config(text=data["main"]["pressure"])

win =Tk()
win.title(" Weather App ")
win.config(bg="blue")
win.geometry("500x570")

name_label = Label(win,text="Python Weather App",font=("Time New Roman",33,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Python Weather App",values=list_name,font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)


check_button = Button(win,text="Check",font=("Time New Roman",20,"bold"),command=data_get)
check_button.place(y=190,height=50,width=100,x=200)


w_label = Label(win,text="Weather Climate",font=("Time New Roman",20,"bold"))
w_label.place(x=25,y=260,height=50,width=220)

w_label1 = Label(win,text="",font=("Time New Roman",20,"bold"))
w_label1.place(x=260,y=260,height=50,width=220)


wb_label = Label(win,text="Weather Description",font=("Time New Roman",16,"bold"))
wb_label.place(x=25,y=330,height=50,width=220)

wb_label1 = Label(win,text="",font=("Time New Roman",20,"bold"))
wb_label1.place(x=260,y=330,height=50,width=220)

temp_label = Label(win,text="Temperature",font=("Time New Roman",22,"bold"))
temp_label.place(x=25,y=400,height=50,width=220)

temp_label1 = Label(win,text="",font=("Time New Roman",22,"bold"))
temp_label1.place(x=260,y=400,height=50,width=220)


per_label = Label(win,text="Pressure",font=("Time New Roman",20,"bold"))
per_label.place(x=25,y=470,height=50,width=220)

per_label1 = Label(win,text="",font=("Time New Roman",20,"bold"))
per_label1.place(x=260,y=470,height=50,width=220)

win.mainloop()