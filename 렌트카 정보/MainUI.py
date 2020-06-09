from tkinter import *
from tkinter import font
import tkinter.messagebox



pwindow = Tk("Korea Lent Car Info")
pwindow.geometry("400x600+750+200")
DataList = []

def initTopText():
    TempFont = font.Font(pwindow , size=20, weight='bold', family='Conslas')
    MainText = Label(pwindow, font = TempFont, text = "[전국 렌터카 업체 정보]")
    MainText.pack()
    MainText.place(x=50)

initTopText()
pwindow.mainloop()




