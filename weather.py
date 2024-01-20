from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=ded12bda4b8b3d10edb39013350a914b").json()
    W_label1.config(text=data["weather"][0]["main"])
    Wb_label1.config(text=data["weather"][0]["description"])
    T_label1.config(text=str(int(data["main"]["temp"] - 273.15)))
    P_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("weather Report")
win.config(bg="cyan")
win.geometry("500x570")

name_label = Label(win, text="Weather Forecasting", font=("Times New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()
list_name = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune", "Ahmedabad", "Jaipur",
             "Lucknow"]
com = ttk.Combobox(win, text="Weather Forecasting", values=list_name, font=("Times New Roman", 23, "bold"),
                   textvariable=city_name)

com.place(x=25, y=120, height=50, width=450)

W_label = Label(win, text="Weather Climate", font=("Times New Roman", 16))
W_label.place(x=25, y=260, height=50, width=210)

W_label1 = Label(win, text="", font=("Times New Roman", 16))
W_label1.place(x=250, y=260, height=50, width=210)

Wb_label = Label(win, text="Weather Description", font=("Times New Roman", 16))
Wb_label.place(x=25, y=330, height=50, width=210)

Wb_label1 = Label(win, text="", font=("Times New Roman", 16))
Wb_label1.place(x=250, y=330, height=50, width=210)

T_label = Label(win, text="Temperature", font=("Times New Roman", 16))
T_label.place(x=25, y=400, height=50, width=210)

T_label1 = Label(win, text="", font=("Times New Roman", 16))
T_label1.place(x=250, y=400, height=50, width=210)

P_label = Label(win, text="Pressure", font=("Times New Roman", 16))
P_label.place(x=25, y=470, height=50, width=210)

P_label1 = Label(win, text="", font=("Times New Roman", 16))
P_label1.place(x=250, y=470, height=50, width=210)

done_button = Button(win, text="Done", font=("Time New Roman", 20, "bold"),command=data_get)
done_button.place(y=190, height=50, width=100, x=200)

win.mainloop()
