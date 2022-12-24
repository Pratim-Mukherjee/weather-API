from tkinter import *
from tkinter import ttk
import requests
def data_get():
  city=city_name.get()
  data =requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b64572d8d8c583fcdb0f6a418287099a").json()
  w_lable1.config(text=data["weather"][0]["main"])
  wd_lable2.config(text=data["weather"][0]["description"])
  wt_lable3.config(text=str(int(data["main"]["temp"]-273.15)))
  wp_lable4.config(text=data["main"]["pressure"])






win = Tk()
win.title("Mukherjee Weather App")
win.config(bg = "teal")
win.geometry("1000x555")

name_lable=Label(win,text="Abohawa Weather App",font=("Times New Roman",35 ))
name_lable.place(x=155,y=65,height=65,width=650)

city_name = StringVar()
list_name= ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com =ttk.Combobox(win,text="Abohawa Weather App",values=list_name,font=("Cambria",17),textvariable=city_name)
com.place(x=155,y=140, height=65, width=650)

w_lable=Label(win,text="Climate:",font=("Times New Roman",20 ))
w_lable.place(x=285,y=300,height=35,width=150)


w_lable1=Label(win,text=" ",font=("Times New Roman",20 ))
w_lable1.place(x=450,y=300,height=35,width=150)



wd_lable=Label(win,text="Description:",font=("Times New Roman",20 ))
wd_lable.place(x=285,y=350,height=35,width=150)

wd_lable2=Label(win,text=" ",font=("Times New Roman",20 ))
wd_lable2.place(x=450,y=350,height=35,width=150)



wt_lable=Label(win,text="Temperature:",font=("Times New Roman",20 ))
wt_lable.place(x=285,y=400,height=35,width=150)


wt_lable3=Label(win,text=" ",font=("Times New Roman",20 ))
wt_lable3.place(x=450,y=400,height=35,width=150)


wp_lable=Label(win,text="Pressure:",font=("Times New Roman",20 ))
wp_lable.place(x=285,y=450,height=35,width=150)


wp_lable4=Label(win,text=" ",font=("Times New Roman",20 ))
wp_lable4.place(x=450,y=450,height=35,width=150)



done_button =Button(win, text="Done",font=("Cambria",17,"bold"),command=data_get)
done_button.place(y=220,height=65, width=100, x=400)


win.mainloop()