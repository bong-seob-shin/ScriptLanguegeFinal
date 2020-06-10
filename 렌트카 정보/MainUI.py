from tkinter import *
from tkinter import font
import tkinter.messagebox


def SearchIn():
    global listbox,ILabel

    #index =listbox.get(0 ,"end").index(ILabel.get())
    #listbox.activate(index)
    pass


def SearchGangWondo():
    global listbox,ILabel
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=20, weight='bold', family='Conslas')
    TopLabel = Label(windowGW, font=TempFont, text="[강원도 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)

    listbox = tkinter.Listbox(frame, font=TempFont,width=10, height=10, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    for line in range(1, 1001):
        listbox.insert(line, "김"+str(line))
    listbox.pack(side=LEFT, fill = Y)
    RenderTextScrollbar.config(command= listbox.yview)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)
    listbox.activate(0)

    frame.pack()
    frame.place(x= 20, y = 70)

    ILabelFont = font.Font(windowGW, size=10, weight='bold', family = 'Consolas')
    ILabel = Entry(windowGW, font = ILabelFont, width = 18, borderwidth = 3, relief = 'ridge')
    ILabel.pack()
    ILabel.place(x = 215, y = 70)


    IButton = Button(windowGW, font = ILabelFont, text = "검색",command =  SearchIn)
    IButton.pack()
    IButton.place(x= 350, y = 70)

pwindow = Tk("Korea Lent Car Info")
pwindow.geometry("400x450")
DataList = []
mapImage = PhotoImage(file='Resorce/대한민국 지도.gif')
MainImage = Label(pwindow, image=mapImage)
MainImage.pack()
MainImage.place(x= 50, y = 50)
TempFont = font.Font(pwindow, size = 8, weight ='bold' , family ='Conslas')
searchGanWonButton = Button(pwindow, font = TempFont, text ="강원도", command = SearchGangWondo)
searchGanWonButton.pack()
searchGanWonButton.place(x = 205, y=70)

searchGyeonggidoButton = Button(pwindow, font = TempFont, text ="경기도", command = SearchGangWondo)
searchGyeonggidoButton.pack()
searchGyeonggidoButton.place(x = 135, y=130)

searchChoongNamButton = Button(pwindow, font = TempFont, text ="충청남도", command = SearchGangWondo)
searchChoongNamButton.pack()
searchChoongNamButton.place(x = 105, y=170)

searchDaejeonButton = Button(pwindow, font = TempFont, text ="대전", command = SearchGangWondo)
searchDaejeonButton.pack()
searchDaejeonButton.place(x = 150, y=200)

searchJeonRaBukButton = Button(pwindow, font = TempFont, text ="전라북도", command = SearchGangWondo)
searchJeonRaBukButton.pack()
searchJeonRaBukButton.place(x = 120, y=250)

searchGwangjuButton = Button(pwindow, font = TempFont, text =" 광주 ", command = SearchGangWondo)
searchGwangjuButton.pack()
searchGwangjuButton.place(x = 135, y=300)

searchJeonRaNamButton = Button(pwindow, font = TempFont, text ="전라남도", command = SearchGangWondo)
searchJeonRaNamButton.pack()
searchJeonRaNamButton.place(x = 115, y=330)

searchGyeongSangBukButton = Button(pwindow, font = TempFont, text ="경상북도", command = SearchGangWondo)
searchGyeongSangBukButton.pack()
searchGyeongSangBukButton.place(x = 220, y=190)

searchDaeguButton = Button(pwindow, font = TempFont, text =" 대구 ", command = SearchGangWondo)
searchDaeguButton.pack()
searchDaeguButton.place(x = 235, y=240)

searchUlSanButton = Button(pwindow, font = TempFont, text ="울산", command = SearchGangWondo)
searchUlSanButton.pack()
searchUlSanButton.place(x = 285, y=275)

searchBuSanButton = Button(pwindow, font = TempFont, text =" 부산 ", command = SearchGangWondo)
searchBuSanButton.pack()
searchBuSanButton.place(x = 265, y=305)

searchGyeongSangNamButton = Button(pwindow, font = TempFont, text ="경상남도", command = SearchGangWondo)
searchGyeongSangNamButton.pack()
searchGyeongSangNamButton.place(x = 205, y=280)

searchChoongBukButton = Button(pwindow, font = TempFont, text ="충청북도", command = SearchGangWondo)
searchChoongBukButton.pack()
searchChoongBukButton.place(x = 180, y=140)

searchSeoulIncheonButton = Button(pwindow, font = TempFont, text ="인천, 서울 특별시", command = SearchGangWondo)
searchSeoulIncheonButton.pack()
searchSeoulIncheonButton.place(x = 90, y=90)

def initTopText():
    TempFont = font.Font(pwindow , size=20, weight='bold', family='Conslas')
    MainText = Label(pwindow, font = TempFont, text = "[전국 렌터카 업체 정보]")
    MainText.pack()
    MainText.place(x=50)


initTopText()
pwindow.mainloop()




