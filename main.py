from tkinter import *
from tkinter.ttk import *
from time import strftime

main = Tk()
main.title("Digital Clock")

def clock():
    tick = strftime("%H:%M:%S %p")
    clock_label.config(text=tick)
    clock_label.after(1000, clock)

clock_label = Label(main, font=('sans', 60), background='orange', foreground= 'white')

clock_label.pack(anchor='center')

clock()
mainloop()
