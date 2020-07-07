import sys
from tkinter import *
import tkinter as tk
import time

def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200,tick)


root = tk.Tk()
root.configure(background='black')
root.title("MY WATCH")
name=tk.Label(text="Emyounoone Coded Me",fg="red",bg="black",font=("8514oem"))
name.pack(side="bottom")
clock=tk.Label(root,font=("8514oem",42,"bold"), bg ="black",fg="green")
clock.pack()
tick()
root.mainloop()
