from tkinter import *
from tkinter import font
import tkinter.messagebox


class MainUI:


    def __init__(self):
        self.initUI()

    def initUI(self):
        self.pwindow = Tk("Korea Lent Car Info")
        self.pwindow.geometry("800x800")
        self.TempFont = font.Font(size = 16, weight = 'bold', family = 'Conslas')
        self.label =[]
        self.entry = []
        self.label.append(Label(self.pwindow, text= "플레이어 명수", font = self.TempFont))
        self.label[0].grid(row=0,column = 0)


        self.pwindow.mainloop()



MainUI()
