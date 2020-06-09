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

searchJeonRaBukButton = Button(pwindow, font = TempFont, text ="전라북도", command = SearchGanWondo)
searchJeonRaBukButton.pack()
searchJeonRaBukButton.place(x = 120, y=250)

searchGwangjuButton = Button(pwindow, font = TempFont, text =" 광주 ", command = SearchGanWondo)
searchGwangjuButton.pack()
searchGwangjuButton.place(x = 135, y=300)

searchJeonRaNamButton = Button(pwindow, font = TempFont, text ="전라남도", command = SearchGanWondo)
searchJeonRaNamButton.pack()
searchJeonRaNamButton.place(x = 115, y=330)

searchGyeongSangBukButton = Button(pwindow, font = TempFont, text ="경상북도", command = SearchGanWondo)
searchGyeongSangBukButton.pack()
searchGyeongSangBukButton.place(x = 220, y=190)

searchDaeguButton = Button(pwindow, font = TempFont, text =" 대구 ", command = SearchGanWondo)
searchDaeguButton.pack()
searchDaeguButton.place(x = 235, y=240)

searchUlSanButton = Button(pwindow, font = TempFont, text ="울산", command = SearchGanWondo)
searchUlSanButton.pack()
searchUlSanButton.place(x = 285, y=275)

searchBuSanButton = Button(pwindow, font = TempFont, text =" 부산 ", command = SearchGanWondo)
searchBuSanButton.pack()
searchBuSanButton.place(x = 265, y=305)

searchGyeongSangNamButton = Button(pwindow, font = TempFont, text ="경상남도", command = SearchGanWondo)
searchGyeongSangNamButton.pack()
searchGyeongSangNamButton.place(x = 205, y=280)

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




