import ClassCar
from xml.etree.ElementTree import parse
from tkinter import *
from tkinter import font
import tkinter.messagebox

Data = parse('전국렌터카.xml')
root = Data.getroot()

detailList = list()
carDataList = []

for i in root.findall('records'):
    for j in i.findall('record'):
        name = j.find('업체명').text
        address = j.find('소재지도로명주소').text
        latitude = j.find('위도').text
        longitude = j.find('경도').text
        TotalCar = j.find('자동차총보유대수').text
        s_car = j.find('승용차보유대수').text
        b_car = j.find('승합차보유대수').text
        telephone = j.find('전화번호').text
        weekday_start = j.find('평일운영시작시각').text
        weekday_end = j.find('평일운영종료시각').text
        weekend_start = j.find('주말운영시작시각').text
        weekend_end = j.find('주말운영종료시각').text
        personal_day = j.find('휴무일').text
        homepage = j.find('홈페이지주소').text

        Car = ClassCar.CarData(name,address,latitude,longitude,TotalCar,s_car,b_car,telephone,weekday_start,weekday_end,weekend_start,weekend_end,personal_day,homepage)
        carDataList.append(Car)

def SearchGangWondo():
    global listbox,ILabel
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, text="[강원도 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)

    RenderTextHorizonbar = Scrollbar(frame, orient=HORIZONTAL)
    RenderTextHorizonbar.pack(side=BOTTOM, fill=X, expand=True)

    listbox = tkinter.Listbox(frame, font=TempFont, width=20, height=19, borderwidth=12, relief='ridge',
                              yscrollcommand=RenderTextScrollbar.set, xscrollcommand=RenderTextHorizonbar.set)

    city = str("강원도")
    for data in carDataList:
        if city in str(data.address):
            try:
                text = data.address + "["+data.name+"]"
                listbox.insert(END,text)
            except:
                print("error")

    listbox.pack(side=LEFT, fill = Y)
    RenderTextScrollbar.config(command= listbox.yview)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)
    RenderTextHorizonbar.config(command=listbox.xview)
    RenderTextHorizonbar.pack(side=BOTTOM, expand=True, fill=X)
    listbox.activate(0)

    frame.pack()
    frame.place(x= 20, y = 70)

    global ILabel
    ILabelFont = font.Font(windowGW, size=10, weight='bold', family = 'Consolas')
    ILabel = Entry(windowGW, font = ILabelFont, width = 18, borderwidth = 3, relief = 'ridge')
    ILabel.pack()
    ILabel.place(x = 215, y = 70)

    IButton = Button(windowGW, font = ILabelFont, text = "검색",command =  SearchIn1)
    IButton.pack()
    IButton.place(x= 350, y = 70)

    DetailButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="세부 사항", command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="이름 정렬", command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="주소 정렬", command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchKyeongKiDo():
    global listbox,ILabel
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, text="[경기도 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)

    RenderTextHorizonbar = Scrollbar(frame, orient=HORIZONTAL)
    RenderTextHorizonbar.pack(side=BOTTOM, fill=X, expand=True)

    listbox = tkinter.Listbox(frame, font=TempFont, width=20, height=19, borderwidth=12, relief='ridge',
                              yscrollcommand=RenderTextScrollbar.set, xscrollcommand=RenderTextHorizonbar.set)

    city = str("경기도")
    for data in carDataList:
        if city in str(data.address):
            try:
                text = data.address + "["+data.name+"]"
                listbox.insert(END,text)
            except:
                print("error")

    listbox.pack(side=LEFT, fill = Y)
    RenderTextScrollbar.config(command= listbox.yview)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)
    RenderTextHorizonbar.config(command=listbox.xview)
    RenderTextHorizonbar.pack(side=BOTTOM, expand=True, fill=X)
    listbox.activate(0)

    frame.pack()
    frame.place(x= 20, y = 70)

    global ILabel
    ILabelFont = font.Font(windowGW, size=10, weight='bold', family = 'Consolas')
    ILabel = Entry(windowGW, font = ILabelFont, width = 18, borderwidth = 3, relief = 'ridge')
    ILabel.pack()
    ILabel.place(x = 215, y = 70)

    IButton = Button(windowGW, font = ILabelFont, text = "검색",command =  SearchIn2)
    IButton.pack()
    IButton.place(x= 350, y = 70)

    DetailButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="세부 사항", command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="이름 정렬", command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="주소 정렬", command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchChungNam():
    global listbox,ILabel
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")

    frame = tkinter.Frame(windowGW)
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TopLabel = Label(windowGW, font=TempFont1, text="[충청남도 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=30 ,y= 10)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)

    RenderTextHorizonbar = Scrollbar(frame, orient=HORIZONTAL)
    RenderTextHorizonbar.pack(side=BOTTOM, fill=X, expand=True)

    listbox = tkinter.Listbox(frame, font=TempFont, width=20, height=19, borderwidth=12, relief='ridge',
                              yscrollcommand=RenderTextScrollbar.set, xscrollcommand=RenderTextHorizonbar.set)

    city = str("충청남도")
    for data in carDataList:
        if city in str(data.address):
            try:
                text = data.address + "["+data.name+"]"
                listbox.insert(END,text)
            except:
                print("error")

    listbox.pack(side=LEFT, fill = Y)
    RenderTextScrollbar.config(command= listbox.yview)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)
    RenderTextHorizonbar.config(command=listbox.xview)
    RenderTextHorizonbar.pack(side=BOTTOM, expand=True, fill=X)
    listbox.activate(0)

    frame.pack()
    frame.place(x= 20, y = 70)

    global ILabel
    ILabelFont = font.Font(windowGW, size=10, weight='bold', family = 'Consolas')
    ILabel = Entry(windowGW, font = ILabelFont, width = 18, borderwidth = 3, relief = 'ridge')
    ILabel.pack()
    ILabel.place(x = 215, y = 70)

    IButton = Button(windowGW, font = ILabelFont, text = "검색",command =  SearchIn3)
    IButton.pack()
    IButton.place(x= 350, y = 70)

    DetailButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="세부 사항", command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="이름 정렬", command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="주소 정렬", command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchDaeJeon():
    global listbox,ILabel
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")

    frame = tkinter.Frame(windowGW)
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TopLabel = Label(windowGW, font=TempFont1, text="[대전 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)

    RenderTextHorizonbar = Scrollbar(frame, orient=HORIZONTAL)
    RenderTextHorizonbar.pack(side=BOTTOM, fill=X, expand=True)

    listbox = tkinter.Listbox(frame, font=TempFont, width=20, height=19, borderwidth=12, relief='ridge',
                              yscrollcommand=RenderTextScrollbar.set, xscrollcommand=RenderTextHorizonbar.set)

    city = str("대전광역시")
    for data in carDataList:
        if city in str(data.address):
            try:
                text = data.address + "["+data.name+"]"
                listbox.insert(END,text)
            except:
                print("error")

    listbox.pack(side=LEFT, fill = Y)
    RenderTextScrollbar.config(command= listbox.yview)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)
    RenderTextHorizonbar.config(command=listbox.xview)
    RenderTextHorizonbar.pack(side=BOTTOM, expand=True, fill=X)
    listbox.activate(0)

    frame.pack()
    frame.place(x= 20, y = 70)

    global ILabel
    ILabelFont = font.Font(windowGW, size=10, weight='bold', family = 'Consolas')
    ILabel = Entry(windowGW, font = ILabelFont, width = 18, borderwidth = 3, relief = 'ridge')
    ILabel.pack()
    ILabel.place(x = 215, y = 70)

    IButton = Button(windowGW, font = ILabelFont, text = "검색",command =  SearchIn4)
    IButton.pack()
    IButton.place(x= 350, y = 70)

    DetailButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="세부 사항", command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="이름 정렬", command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="주소 정렬", command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchJeonBuk():
    global listbox,ILabel
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")

    frame = tkinter.Frame(windowGW)
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TopLabel = Label(windowGW, font=TempFont1, text="[전라북도 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)

    RenderTextHorizonbar = Scrollbar(frame, orient=HORIZONTAL)
    RenderTextHorizonbar.pack(side=BOTTOM, fill=X, expand=True)

    listbox = tkinter.Listbox(frame, font=TempFont, width=20, height=19, borderwidth=12, relief='ridge',
                              yscrollcommand=RenderTextScrollbar.set, xscrollcommand=RenderTextHorizonbar.set)

    city = str("전라북도")
    for data in carDataList:
        if city in str(data.address):
            try:
                text = data.address + "["+data.name+"]"
                listbox.insert(END,text)
            except:
                print("error")

    listbox.pack(side=LEFT, fill = Y)
    RenderTextScrollbar.config(command= listbox.yview)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)
    RenderTextHorizonbar.config(command=listbox.xview)
    RenderTextHorizonbar.pack(side=BOTTOM, expand=True, fill=X)
    listbox.activate(0)

    frame.pack()
    frame.place(x= 20, y = 70)

    global ILabel
    ILabelFont = font.Font(windowGW, size=10, weight='bold', family = 'Consolas')
    ILabel = Entry(windowGW, font = ILabelFont, width = 18, borderwidth = 3, relief = 'ridge')
    ILabel.pack()
    ILabel.place(x = 215, y = 70)

    IButton = Button(windowGW, font = ILabelFont, text = "검색",command =  SearchIn5)
    IButton.pack()
    IButton.place(x= 350, y = 70)

    DetailButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="세부 사항", command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="이름 정렬", command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="주소 정렬", command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchGwangJu():
    global listbox,ILabel
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, text="[광주 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)

    RenderTextHorizonbar = Scrollbar(frame, orient=HORIZONTAL)
    RenderTextHorizonbar.pack(side=BOTTOM, fill=X, expand=True)

    listbox = tkinter.Listbox(frame, font=TempFont, width=20, height=19, borderwidth=12, relief='ridge',
                              yscrollcommand=RenderTextScrollbar.set, xscrollcommand=RenderTextHorizonbar.set)

    city = str("광주광역시")
    for data in carDataList:
        if city in str(data.address):
            try:
                text = data.address + "["+data.name+"]"
                listbox.insert(END,text)
            except:
                print("error")

    listbox.pack(side=LEFT, fill = Y)
    RenderTextScrollbar.config(command= listbox.yview)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)
    RenderTextHorizonbar.config(command=listbox.xview)
    RenderTextHorizonbar.pack(side=BOTTOM, expand=True, fill=X)
    listbox.activate(0)

    frame.pack()
    frame.place(x= 20, y = 70)

    global ILabel
    ILabelFont = font.Font(windowGW, size=10, weight='bold', family = 'Consolas')
    ILabel = Entry(windowGW, font = ILabelFont, width = 18, borderwidth = 3, relief = 'ridge')
    ILabel.pack()
    ILabel.place(x = 215, y = 70)

    IButton = Button(windowGW, font = ILabelFont, text = "검색",command =  SearchIn6)
    IButton.pack()
    IButton.place(x= 350, y = 70)

    DetailButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="세부 사항", command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="이름 정렬", command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="주소 정렬", command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchJeonNam():
    global listbox,ILabel
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")

    frame = tkinter.Frame(windowGW)
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TopLabel = Label(windowGW, font=TempFont1, text="[전라남도 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)

    RenderTextHorizonbar = Scrollbar(frame, orient=HORIZONTAL)
    RenderTextHorizonbar.pack(side=BOTTOM, fill=X, expand=True)

    listbox = tkinter.Listbox(frame, font=TempFont, width=20, height=19, borderwidth=12, relief='ridge',
                              yscrollcommand=RenderTextScrollbar.set, xscrollcommand=RenderTextHorizonbar.set)

    city = str("전라남도")
    for data in carDataList:
        if city in str(data.address):
            try:
                text = data.address + "["+data.name+"]"
                listbox.insert(END,text)
            except:
                print("error")

    listbox.pack(side=LEFT, fill = Y)
    RenderTextScrollbar.config(command= listbox.yview)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)
    RenderTextHorizonbar.config(command=listbox.xview)
    RenderTextHorizonbar.pack(side=BOTTOM, expand=True, fill=X)
    listbox.activate(0)

    frame.pack()
    frame.place(x= 20, y = 70)

    global ILabel
    ILabelFont = font.Font(windowGW, size=10, weight='bold', family = 'Consolas')
    ILabel = Entry(windowGW, font = ILabelFont, width = 18, borderwidth = 3, relief = 'ridge')
    ILabel.pack()
    ILabel.place(x = 215, y = 70)

    IButton = Button(windowGW, font = ILabelFont, text = "검색",command =  SearchIn7)
    IButton.pack()
    IButton.place(x= 350, y = 70)

    DetailButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="세부 사항", command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="이름 정렬", command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="주소 정렬", command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchGyeongBuk():
    global listbox,ILabel
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, text="[경상북도 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)

    RenderTextHorizonbar = Scrollbar(frame, orient=HORIZONTAL)
    RenderTextHorizonbar.pack(side=BOTTOM, fill=X, expand=True)

    listbox = tkinter.Listbox(frame, font=TempFont, width=20, height=19, borderwidth=12, relief='ridge',
                              yscrollcommand=RenderTextScrollbar.set, xscrollcommand=RenderTextHorizonbar.set)

    city = str("경상북도")
    for data in carDataList:
        if city in str(data.address):
            try:
                text = data.address + "["+data.name+"]"
                listbox.insert(END,text)
            except:
                print("error")

    listbox.pack(side=LEFT, fill = Y)
    RenderTextScrollbar.config(command= listbox.yview)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)
    RenderTextHorizonbar.config(command=listbox.xview)
    RenderTextHorizonbar.pack(side=BOTTOM, expand=True, fill=X)
    listbox.activate(0)

    frame.pack()
    frame.place(x= 20, y = 70)

    global ILabel
    ILabelFont = font.Font(windowGW, size=10, weight='bold', family = 'Consolas')
    ILabel = Entry(windowGW, font = ILabelFont, width = 18, borderwidth = 3, relief = 'ridge')
    ILabel.pack()
    ILabel.place(x = 215, y = 70)

    IButton = Button(windowGW, font = ILabelFont, text = "검색",command =  SearchIn8)
    IButton.pack()
    IButton.place(x= 350, y = 70)

    DetailButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="세부 사항", command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="이름 정렬", command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="주소 정렬", command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchDaegu():
    global listbox,ILabel
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, text="[대구 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)

    RenderTextHorizonbar = Scrollbar(frame, orient=HORIZONTAL)
    RenderTextHorizonbar.pack(side=BOTTOM, fill=X, expand=True)

    listbox = tkinter.Listbox(frame, font=TempFont, width=20, height=19, borderwidth=12, relief='ridge',
                              yscrollcommand=RenderTextScrollbar.set, xscrollcommand=RenderTextHorizonbar.set)

    city = str("대구광역시")
    for data in carDataList:
        if city in str(data.address):
            try:
                text = data.address + "["+data.name+"]"
                listbox.insert(END,text)
            except:
                print("error")

    listbox.pack(side=LEFT, fill = Y)
    RenderTextScrollbar.config(command= listbox.yview)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)
    RenderTextHorizonbar.config(command=listbox.xview)
    RenderTextHorizonbar.pack(side=BOTTOM, expand=True, fill=X)
    listbox.activate(0)

    frame.pack()
    frame.place(x= 20, y = 70)

    global ILabel
    ILabelFont = font.Font(windowGW, size=10, weight='bold', family = 'Consolas')
    ILabel = Entry(windowGW, font = ILabelFont, width = 18, borderwidth = 3, relief = 'ridge')
    ILabel.pack()
    ILabel.place(x = 215, y = 70)

    IButton = Button(windowGW, font = ILabelFont, text = "검색",command =  SearchIn9)
    IButton.pack()
    IButton.place(x= 350, y = 70)

    DetailButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="세부 사항", command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="이름 정렬", command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="주소 정렬", command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchBusan():
    global listbox,ILabel
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, text="[부산 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)

    RenderTextHorizonbar = Scrollbar(frame, orient=HORIZONTAL)
    RenderTextHorizonbar.pack(side=BOTTOM, fill=X, expand=True)

    listbox = tkinter.Listbox(frame, font=TempFont, width=20, height=19, borderwidth=12, relief='ridge',
                              yscrollcommand=RenderTextScrollbar.set, xscrollcommand=RenderTextHorizonbar.set)

    city = str("부산광역시")
    for data in carDataList:
        if city in str(data.address):
            try:
                text = data.address + "["+data.name+"]"
                listbox.insert(END,text)
            except:
                print("error")

    listbox.pack(side=LEFT, fill = Y)
    RenderTextScrollbar.config(command= listbox.yview)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)
    RenderTextHorizonbar.config(command=listbox.xview)
    RenderTextHorizonbar.pack(side=BOTTOM, expand=True, fill=X)
    listbox.activate(0)

    frame.pack()
    frame.place(x= 20, y = 70)

    global ILabel
    ILabelFont = font.Font(windowGW, size=10, weight='bold', family = 'Consolas')
    ILabel = Entry(windowGW, font = ILabelFont, width = 18, borderwidth = 3, relief = 'ridge')
    ILabel.pack()
    ILabel.place(x = 215, y = 70)

    IButton = Button(windowGW, font = ILabelFont, text = "검색",command =  SearchIn10)
    IButton.pack()
    IButton.place(x= 350, y = 70)

    DetailButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="세부 사항", command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="이름 정렬", command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="주소 정렬", command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchGyeongNam():
    global listbox,ILabel
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, text="[경상남도 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)
    RenderTextHorizonbar = Scrollbar(frame, orient=HORIZONTAL)
    RenderTextHorizonbar.pack(side=BOTTOM, fill=X, expand=True)

    listbox = tkinter.Listbox(frame, font=TempFont, width=20, height=19, borderwidth=12, relief='ridge',
                              yscrollcommand=RenderTextScrollbar.set, xscrollcommand=RenderTextHorizonbar.set)

    city = str("경상남도")
    for data in carDataList:
        if city in str(data.address):
            try:
                text = data.address + "["+data.name+"]"
                listbox.insert(END,text)
            except:
                print("error")

    listbox.pack(side=LEFT, fill = Y)
    RenderTextScrollbar.config(command= listbox.yview)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)
    RenderTextHorizonbar.config(command=listbox.xview)
    RenderTextHorizonbar.pack(side=BOTTOM, expand=True, fill=X)
    listbox.activate(0)

    frame.pack()
    frame.place(x= 20, y = 70)

    global ILabel
    ILabelFont = font.Font(windowGW, size=10, weight='bold', family = 'Consolas')
    ILabel = Entry(windowGW, font = ILabelFont, width = 18, borderwidth = 3, relief = 'ridge')
    ILabel.pack()
    ILabel.place(x = 215, y = 70)

    IButton = Button(windowGW, font = ILabelFont, text = "검색",command =  SearchIn11)
    IButton.pack()
    IButton.place(x= 350, y = 70)

    DetailButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="세부 사항", command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="이름 정렬", command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="주소 정렬", command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchChungBuk():
    global listbox,ILabel
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, text="[충청북도 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)

    RenderTextHorizonbar = Scrollbar(frame, orient=HORIZONTAL)
    RenderTextHorizonbar.pack(side=BOTTOM, fill=X, expand=True)

    listbox = tkinter.Listbox(frame, font=TempFont, width=20, height=19, borderwidth=12, relief='ridge',
                              yscrollcommand=RenderTextScrollbar.set, xscrollcommand=RenderTextHorizonbar.set)

    city = str("충청북도")
    for data in carDataList:
        if city in str(data.address):
            try:
                text = data.address + "["+data.name+"]"
                listbox.insert(END,text)
            except:
                print("error")

    listbox.pack(side=LEFT, fill = Y)
    RenderTextScrollbar.config(command= listbox.yview)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)
    RenderTextHorizonbar.config(command=listbox.xview)
    RenderTextHorizonbar.pack(side=BOTTOM, expand=True, fill=X)
    listbox.activate(0)

    frame.pack()
    frame.place(x= 20, y = 70)

    global ILabel
    ILabelFont = font.Font(windowGW, size=10, weight='bold', family = 'Consolas')
    ILabel = Entry(windowGW, font = ILabelFont, width = 18, borderwidth = 3, relief = 'ridge')
    ILabel.pack()
    ILabel.place(x = 215, y = 70)

    IButton = Button(windowGW, font = ILabelFont, text = "검색",command =  SearchIn12)
    IButton.pack()
    IButton.place(x= 350, y = 70)

    DetailButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="세부 사항", command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="이름 정렬", command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="주소 정렬", command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchUlSan():
    global listbox,ILabel
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, text="[울산 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)

    RenderTextHorizonbar = Scrollbar(frame, orient=HORIZONTAL)
    RenderTextHorizonbar.pack(side=BOTTOM, fill=X, expand=True)

    listbox = tkinter.Listbox(frame, font=TempFont, width=20, height=19, borderwidth=12, relief='ridge',
                              yscrollcommand=RenderTextScrollbar.set, xscrollcommand=RenderTextHorizonbar.set)
    city = str("울산광역시")
    for data in carDataList:
        if city in str(data.address):
            try:
                text = data.address + "["+data.name+"]"
                listbox.insert(END,text)
            except:
                print("error")

    listbox.pack(side=LEFT, fill = Y)
    RenderTextScrollbar.config(command= listbox.yview)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)
    RenderTextHorizonbar.config(command=listbox.xview)
    RenderTextHorizonbar.pack(side=BOTTOM, expand=True, fill=X)
    listbox.activate(0)

    frame.pack()
    frame.place(x= 20, y = 70)

    global ILabel
    ILabelFont = font.Font(windowGW, size=10, weight='bold', family = 'Consolas')
    ILabel = Entry(windowGW, font = ILabelFont, width = 18, borderwidth = 3, relief = 'ridge')
    ILabel.pack()
    ILabel.place(x = 215, y = 70)

    IButton = Button(windowGW, font = ILabelFont, text = "검색",command =  SearchIn13)
    IButton.pack()
    IButton.place(x= 350, y = 70)

    DetailButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="세부 사항", command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="이름 정렬", command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="주소 정렬", command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchIncheon():
    global listbox, ILabel
    listvari = [] * 1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, text="[인천 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side=RIGHT, expand=True, fill=Y)

    RenderTextHorizonbar = Scrollbar(frame, orient=HORIZONTAL)
    RenderTextHorizonbar.pack(side=BOTTOM, fill=X, expand=True)

    listbox = tkinter.Listbox(frame, font=TempFont, width=20, height=19, borderwidth=12, relief='ridge',
                              yscrollcommand=RenderTextScrollbar.set, xscrollcommand=RenderTextHorizonbar.set)

    city = str("인천")
    for data in carDataList:
        if city in str(data.address):
            try:
                text = data.address + "[" + data.name + "]"
                listbox.insert(END, text)
            except:
                print("error")

    listbox.pack(side=LEFT, fill=Y)
    RenderTextScrollbar.config(command=listbox.yview)
    RenderTextScrollbar.pack(side=RIGHT, expand=True, fill=Y)
    RenderTextHorizonbar.config(command=listbox.xview)
    RenderTextHorizonbar.pack(side=BOTTOM, expand=True, fill=X)
    listbox.activate(0)

    frame.pack()
    frame.place(x=20, y=70)

    global ILabel
    ILabelFont = font.Font(windowGW, size=10, weight='bold', family='Consolas')
    ILabel = Entry(windowGW, font=ILabelFont, width=18, borderwidth=3, relief='ridge')
    ILabel.pack()
    ILabel.place(x=215, y=70)

    IButton = Button(windowGW, font=ILabelFont, text="검색", command=SearchIn15)
    IButton.pack()
    IButton.place(x=350, y=70)

    DetailButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="세부 사항", command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="이름 정렬", command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="주소 정렬", command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchSeoul():
    global listbox,ILabel
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")

    frame = tkinter.Frame(windowGW)
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, text="[서울 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)
    RenderTextHorizonbar = Scrollbar(frame, orient=HORIZONTAL )
    RenderTextHorizonbar.pack(side = BOTTOM , fill = X , expand = True)

    listbox = tkinter.Listbox(frame, font=TempFont,width=20, height=19, borderwidth=12, relief='ridge',  yscrollcommand=RenderTextScrollbar.set, xscrollcommand=RenderTextHorizonbar.set)


    city = str("서울특별시")
    for data in carDataList:
        if city in str(data.address):
            try:
                text = data.address + "["+data.name+"]"
                listbox.insert(END,text)
            except:
                print("error")

    listbox.pack(side=LEFT, fill = Y)
    RenderTextScrollbar.config(command= listbox.yview)
    RenderTextScrollbar.pack(side= RIGHT, expand = True, fill =Y)
    RenderTextHorizonbar.config(command = listbox.xview)
    RenderTextHorizonbar.pack(side = BOTTOM, expand = True, fill = X)
    listbox.activate(0)

    frame.pack()
    frame.place(x= 20, y = 70)

    global ILabel
    ILabelFont = font.Font(windowGW, size=10, weight='bold', family = 'Consolas')
    ILabel = Entry(windowGW, font = ILabelFont, width = 18, borderwidth = 3, relief = 'ridge')
    ILabel.pack()
    ILabel.place(x = 215, y = 70)

    IButton = Button(windowGW, font = ILabelFont, text = "검색",command =  SearchIn14)
    IButton.pack()
    IButton.place(x= 350, y = 70)

    DetailButton = Button(windowGW, width = 18, height = 2, font = ILabelFont, text = "세부 사항",command =  DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="이름 정렬", command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="주소 정렬", command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchJejoo():
    global listbox, ILabel
    listvari = [] * 1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")

    frame = tkinter.Frame(windowGW)
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, text="[제주도 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side=RIGHT, expand=True, fill=Y)
    RenderTextHorizonbar = Scrollbar(frame, orient=HORIZONTAL)
    RenderTextHorizonbar.pack(side=BOTTOM, fill=X, expand=True)

    listbox = tkinter.Listbox(frame, font=TempFont, width=20, height=19, borderwidth=12, relief='ridge',
                              yscrollcommand=RenderTextScrollbar.set, xscrollcommand=RenderTextHorizonbar.set)

    city = str("제주특별")
    for data in carDataList:
        if city in str(data.address):
            try:
                text = data.address + "[" + data.name + "]"
                listbox.insert(END, text)
            except:
                print("error")

    listbox.pack(side=LEFT, fill=Y)
    RenderTextScrollbar.config(command=listbox.yview)
    RenderTextScrollbar.pack(side=RIGHT, expand=True, fill=Y)
    RenderTextHorizonbar.config(command=listbox.xview)
    RenderTextHorizonbar.pack(side=BOTTOM, expand=True, fill=X)
    listbox.activate(0)

    frame.pack()
    frame.place(x=20, y=70)

    global ILabel
    ILabelFont = font.Font(windowGW, size=10, weight='bold', family='Consolas')
    ILabel = Entry(windowGW, font=ILabelFont, width=18, borderwidth=3, relief='ridge')
    ILabel.pack()
    ILabel.place(x=215, y=70)

    IButton = Button(windowGW, font=ILabelFont, text="검색", command=SearchIn16)
    IButton.pack()
    IButton.place(x=350, y=70)

    DetailButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="세부 사항", command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="이름 정렬", command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="주소 정렬", command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchAll():
    global listbox, ILabel
    listvari = [] * 1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")

    frame = tkinter.Frame(windowGW)
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, text="[전국 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side=RIGHT, expand=True, fill=Y)
    RenderTextHorizonbar = Scrollbar(frame, orient=HORIZONTAL)
    RenderTextHorizonbar.pack(side=BOTTOM, fill=X, expand=True)

    listbox = tkinter.Listbox(frame, font=TempFont, width=20, height=19, borderwidth=12, relief='ridge',
                              yscrollcommand=RenderTextScrollbar.set, xscrollcommand=RenderTextHorizonbar.set)


    for data in carDataList:
        text = str(data.address) + "[" + data.name + "]"
        listbox.insert(END, text)


    listbox.pack(side=LEFT, fill=Y)
    RenderTextScrollbar.config(command=listbox.yview)
    RenderTextScrollbar.pack(side=RIGHT, expand=True, fill=Y)
    RenderTextHorizonbar.config(command=listbox.xview)
    RenderTextHorizonbar.pack(side=BOTTOM, expand=True, fill=X)
    listbox.activate(0)

    frame.pack()
    frame.place(x=20, y=70)

    global ILabel
    ILabelFont = font.Font(windowGW, size=10, weight='bold', family='Consolas')
    ILabel = Entry(windowGW, font=ILabelFont, width=18, borderwidth=3, relief='ridge')
    ILabel.pack()
    ILabel.place(x=215, y=70)

    IButton = Button(windowGW, font=ILabelFont, text="검색", command=SearchInAll)
    IButton.pack()
    IButton.place(x=350, y=70)

    DetailButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="세부 사항", command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="이름 정렬", command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, text="주소 정렬", command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def DetailText1():

    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, text="[세부 사항]")
    TopLabel.pack()
    TopLabel.place(x=120)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side=RIGHT, expand=True, fill=Y)
    RenderTextHorizonbar = Scrollbar(frame, orient=HORIZONTAL)
    RenderTextHorizonbar.pack(side=BOTTOM, fill=X, expand=True)

    detailListbox = tkinter.Listbox(frame, font=TempFont, width=36, height=19, borderwidth=12, relief='ridge',
                              yscrollcommand=RenderTextScrollbar.set, xscrollcommand=RenderTextHorizonbar.set)

    detailListbox.pack(side=LEFT, fill=Y)
    RenderTextScrollbar.config(command=detailListbox.yview)
    RenderTextScrollbar.pack(side=RIGHT, expand=True, fill=Y)
    RenderTextHorizonbar.config(command=detailListbox.xview)
    RenderTextHorizonbar.pack(side=BOTTOM, expand=True, fill=X)
    detailListbox.activate(0)

    frame.pack()
    frame.place(x=20, y=70)


    EButton = Button(windowGW, font=TempFont,width = 8 , height = 3, text="이메일 전송", command= SendMail)
    EButton.pack()
    EButton.place(x=320, y=370)

    searchAddress,searchName = str(listbox.get(ACTIVE)).split("[")

    for data in carDataList:
        if searchAddress in str(data.address):
            try:
                text1 = "주소: " +data.address
                detailListbox.insert(END,text1)
                text2 = "업체명: " +data.name
                detailListbox.insert(END,text2)
                text3 = "자동차보유대수: "+data.TotalCar
                detailListbox.insert(END,text3)
                text4 = "승용차보유대수: "+data.s_car
                detailListbox.insert(END,text4)
                text5 = "승합차보유대수: "+data.b_car
                detailListbox.insert(END,text5)
                text6= "전화번호: "+data.telephone
                detailListbox.insert(END,text6)
                text7 = "평일운영시작시각: "+data.weekday_start
                detailListbox.insert(END,text7)
                text8 = "평일운영종료시각: "+data.weekday_end
                detailListbox.insert(END,text8)
                text9 = "주말운영시작시각: "+data.weekend_start
                detailListbox.insert(END,text9)
                text10 ="주말운영종료시각: "+data.weekend_end
                detailListbox.insert(END,text10)
                text11 = "휴무일: "+data.personal_day
                detailListbox.insert(END,text11)
                text12 = "홈페이지주소: "+data.homepage
                detailListbox.insert(END,text12)
            except:
                pass

def MapImage1():
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")

def SortNameList():
   pass

def SortAddressList():
   pass

def SendMail():
    pass

def SearchIn1():
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("강원도")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn2():
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("경기도")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn3():
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("충청남도")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn4():
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("대전광역시")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn5():
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("전라북도")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn6():
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("광주광역시")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn7():
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("전라남도")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn8():
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("경상북도")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn9():
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("대구광역시")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn10():
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("부산광역시")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn11():
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("경상남도")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn12():
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("충청북도")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn13():
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("울산광역시")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn14():
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("서울특별")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn15():
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("인천광역시")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn16():
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("제주특별")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchInAll():                                 # 전체 검색
    listbox.delete(0,50000)
    searchTemp= str(ILabel.get())
    for data in carDataList:
        if searchTemp in str(data.address) or searchTemp in str(data.address):
            try:
                text = "["+data.address+"] "+data.name
            except:
                print("error")
                if data.address == None:
                    text = "["+data.address+"] " +data.name
            listbox.insert(END,text)


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

searchGyeonggidoButton = Button(pwindow, font = TempFont, text ="경기도", command = SearchKyeongKiDo)
searchGyeonggidoButton.pack()
searchGyeonggidoButton.place(x = 135, y=130)

searchChoongNamButton = Button(pwindow, font = TempFont, text ="충청남도", command = SearchChungNam)
searchChoongNamButton.pack()
searchChoongNamButton.place(x = 105, y=170)

searchDaejeonButton = Button(pwindow, font = TempFont, text ="대전", command = SearchDaeJeon)
searchDaejeonButton.pack()
searchDaejeonButton.place(x = 150, y=200)

searchJeonRaBukButton = Button(pwindow, font = TempFont, text ="전라북도", command = SearchJeonBuk)
searchJeonRaBukButton.pack()
searchJeonRaBukButton.place(x = 120, y=250)

searchGwangjuButton = Button(pwindow, font = TempFont, text =" 광주 ", command = SearchGwangJu)
searchGwangjuButton.pack()
searchGwangjuButton.place(x = 135, y=300)

searchJeonRaNamButton = Button(pwindow, font = TempFont, text ="전라남도", command = SearchJeonNam)
searchJeonRaNamButton.pack()
searchJeonRaNamButton.place(x = 115, y=330)

searchGyeongSangBukButton = Button(pwindow, font = TempFont, text ="경상북도", command = SearchGyeongBuk)
searchGyeongSangBukButton.pack()
searchGyeongSangBukButton.place(x = 220, y=190)

searchDaeguButton = Button(pwindow, font = TempFont, text =" 대구 ", command = SearchDaegu)
searchDaeguButton.pack()
searchDaeguButton.place(x = 235, y=240)

searchUlSanButton = Button(pwindow, font = TempFont, text ="울산", command = SearchUlSan)
searchUlSanButton.pack()
searchUlSanButton.place(x = 285, y=275)

searchBuSanButton = Button(pwindow, font = TempFont, text =" 부산 ", command = SearchBusan)
searchBuSanButton.pack()
searchBuSanButton.place(x = 265, y=305)

searchJeJooButton = Button(pwindow, font = TempFont, text =" 제주도 ", command = SearchJejoo)
searchJeJooButton.pack()
searchJeJooButton.place(x = 255, y=365)


searchGyeongSangNamButton = Button(pwindow, font = TempFont, text ="경상남도", command = SearchGyeongNam)
searchGyeongSangNamButton.pack()
searchGyeongSangNamButton.place(x = 205, y=280)

searchChoongBukButton = Button(pwindow, font = TempFont, text ="충청북도", command = SearchChungBuk)
searchChoongBukButton.pack()
searchChoongBukButton.place(x = 180, y=140)

searchIncheonButton = Button(pwindow, font = TempFont, text =" 인천 ", command = SearchIncheon)
searchIncheonButton.pack()
searchIncheonButton.place(x = 100, y=90)

searchSeoulButton = Button(pwindow, font = TempFont, text =" 서울 ", command = SearchSeoul)
searchSeoulButton.pack()
searchSeoulButton.place(x = 145, y=90)

searchAllButton = Button(pwindow, font = TempFont, bg = 'green' ,text =" 전국 ", command = SearchAll)
searchAllButton.pack()
searchAllButton.place(x = 275, y=60)

def initTopText():
    TempFont = font.Font(pwindow , size=20, weight='bold', family='Conslas')
    MainText = Label(pwindow, font = TempFont, text = "[전국 렌터카 업체 정보]")
    MainText.pack()
    MainText.place(x=50)

initTopText()
pwindow.mainloop()




