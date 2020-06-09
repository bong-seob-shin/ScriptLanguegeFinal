from tkinter import *
from tkinter import font
import tkinter.messagebox


def SearchGanWondo():
    pass


pwindow = Tk("Korea Lent Car Info")
pwindow.geometry("400x450")
DataList = []
mapImage = PhotoImage(file='Resorce/대한민국 지도.gif')
MainImage = Label(pwindow, image=mapImage)
MainImage.pack()
MainImage.place(x= 50, y = 50)
TempFont = font.Font(pwindow, size = 8, weight ='bold' , family ='Conslas')
searchGanWonButton = Button(pwindow, font = TempFont, text ="강원도", command = SearchGanWondo)
searchGanWonButton.pack()
searchGanWonButton.place(x = 205, y=70)

searchGyeonggidoButton = Button(pwindow, font = TempFont, text ="경기도", command = SearchGanWondo)
searchGyeonggidoButton.pack()
searchGyeonggidoButton.place(x = 135, y=130)

searchChoongNamButton = Button(pwindow, font = TempFont, text ="충청남도", command = SearchGanWondo)
searchChoongNamButton.pack()
searchChoongNamButton.place(x = 105, y=170)

searchDaejeonButton = Button(pwindow, font = TempFont, text ="대전", command = SearchGanWondo)
searchDaejeonButton.pack()
searchDaejeonButton.place(x = 150, y=200)

searchGyeongSangBukButton = Button(pwindow, font = TempFont, text ="경상북도", command = SearchGanWondo)
searchGyeongSangBukButton.pack()
searchGyeongSangBukButton.place(x = 220, y=190)

searchChoongBukButton = Button(pwindow, font = TempFont, text ="충청북도", command = SearchGanWondo)
searchChoongBukButton.pack()
searchChoongBukButton.place(x = 180, y=140)

searchSeoulIncheonButton = Button(pwindow, font = TempFont, text ="인천, 서울 특별시", command = SearchGanWondo)
searchSeoulIncheonButton.pack()
searchSeoulIncheonButton.place(x = 90, y=90)

def initTopText():
    TempFont = font.Font(pwindow , size=20, weight='bold', family='Conslas')
    MainText = Label(pwindow, font = TempFont, text = "[전국 렌터카 업체 정보]")
    MainText.pack()
    MainText.place(x=50)


initTopText()
pwindow.mainloop()




