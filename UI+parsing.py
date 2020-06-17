import ClassCar
import sendEmail
from xml.etree.ElementTree import parse
from tkinter import *
from tkinter import font
import tkinter.messagebox
import folium
import webbrowser

Data = parse('전국렌터카.xml')
root = Data.getroot()
global SendAllText

detailList = []
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
    detailList.clear()
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")
    windowGW.configure(bg='ghost white')

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, bg='ghost white',text="[강원도 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50, y = 10)
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
                detailList.append(carDataList.index(data))
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

    IButton = Button(windowGW, font = ILabelFont, text = "검색", bg = 'snow2',command =  SearchIn1)
    IButton.pack()
    IButton.place(x= 355, y = 68)

    DetailButton = Button(windowGW, width=18, height=2, bg = 'mint cream',font=ILabelFont, text="세부 사항", command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg = 'light yellow', text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg = 'lightSteelBlue1', text="이름 정렬", command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont,bg ='RosyBrown1', text="주소 정렬", command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchKyeongKiDo():
    global listbox,ILabel
    detailList.clear()
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")
    windowGW.configure(bg='ghost white')

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, bg='ghost white',text="[경기도 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50, y = 10)
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
                detailList.append(carDataList.index(data))
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

    IButton = Button(windowGW, font=ILabelFont, text="검색", bg='snow2', command=SearchIn2)
    IButton.pack()
    IButton.place(x=355, y=68)

    DetailButton = Button(windowGW, width=18, height=2, bg='mint cream', font=ILabelFont, text="세부 사항",
                          command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='light yellow', text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='lightSteelBlue1', text="이름 정렬",
                            command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='RosyBrown1', text="주소 정렬",
                               command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchChungNam():
    global listbox,ILabel
    detailList.clear()
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")
    windowGW.configure(bg='ghost white')

    frame = tkinter.Frame(windowGW)
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TopLabel = Label(windowGW, font=TempFont1, bg='ghost white',text="[충청남도 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50, y = 10)
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
                detailList.append(carDataList.index(data))
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

    IButton = Button(windowGW, font=ILabelFont, text="검색", bg='snow2', command=SearchIn3)
    IButton.pack()
    IButton.place(x=355, y=68)

    DetailButton = Button(windowGW, width=18, height=2, bg='mint cream', font=ILabelFont, text="세부 사항",
                          command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='light yellow', text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='lightSteelBlue1', text="이름 정렬",
                            command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='RosyBrown1', text="주소 정렬",
                               command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchDaeJeon():
    global listbox,ILabel
    detailList.clear()
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")
    windowGW.configure(bg='ghost white')

    frame = tkinter.Frame(windowGW)
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TopLabel = Label(windowGW, font=TempFont1, bg='ghost white',text="[대전 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50, y = 10)
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
                detailList.append(carDataList.index(data))
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

    IButton = Button(windowGW, font=ILabelFont, text="검색", bg='snow2', command=SearchIn4)
    IButton.pack()
    IButton.place(x=355, y=68)

    DetailButton = Button(windowGW, width=18, height=2, bg='mint cream', font=ILabelFont, text="세부 사항",
                          command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='light yellow', text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='lightSteelBlue1', text="이름 정렬",
                            command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='RosyBrown1', text="주소 정렬",
                               command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchJeonBuk():
    global listbox,ILabel
    detailList.clear()
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")
    windowGW.configure(bg='ghost white')

    frame = tkinter.Frame(windowGW)
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TopLabel = Label(windowGW, font=TempFont1, bg='ghost white',text="[전라북도 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50, y = 10)
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
                detailList.append(carDataList.index(data))
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

    IButton = Button(windowGW, font=ILabelFont, text="검색", bg='snow2', command=SearchIn5)
    IButton.pack()
    IButton.place(x=355, y=68)

    DetailButton = Button(windowGW, width=18, height=2, bg='mint cream', font=ILabelFont, text="세부 사항",
                          command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='light yellow', text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='lightSteelBlue1', text="이름 정렬",
                            command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='RosyBrown1', text="주소 정렬",
                               command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchGwangJu():
    global listbox,ILabel
    detailList.clear()
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")
    windowGW.configure(bg='ghost white')

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1,bg='ghost white', text="[광주 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50, y = 10)
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
                detailList.append(carDataList.index(data))
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

    IButton = Button(windowGW, font = ILabelFont, text = "검색",  bg='snow2',command =  SearchIn6)
    IButton.pack()
    IButton.place(x= 355, y = 68)

    DetailButton = Button(windowGW, width=18, height=2, bg='mint cream', font=ILabelFont, text="세부 사항",
                          command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='light yellow', text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='lightSteelBlue1', text="이름 정렬",
                            command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='RosyBrown1', text="주소 정렬",
                               command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchJeonNam():
    global listbox,ILabel
    detailList.clear()
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")
    windowGW.configure(bg='ghost white')

    frame = tkinter.Frame(windowGW)
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TopLabel = Label(windowGW, font=TempFont1, bg='ghost white',text="[전라남도 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50, y = 10)
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
                detailList.append(carDataList.index(data))
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

    IButton = Button(windowGW, font = ILabelFont, text = "검색", bg='snow2',command =  SearchIn7)
    IButton.pack()
    IButton.place(x= 355, y = 68)

    DetailButton = Button(windowGW, width=18, height=2, bg='mint cream', font=ILabelFont, text="세부 사항",
                          command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='light yellow', text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='lightSteelBlue1', text="이름 정렬",
                            command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='RosyBrown1', text="주소 정렬",
                               command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchGyeongBuk():
    global listbox,ILabel
    detailList.clear()
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")
    windowGW.configure(bg='ghost white')

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1,bg='ghost white', text="[경상북도 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50, y = 10)
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
                detailList.append(carDataList.index(data))
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

    IButton = Button(windowGW, font = ILabelFont, text = "검색",bg='snow2',command =  SearchIn8)
    IButton.pack()
    IButton.place(x= 355, y = 68)

    DetailButton = Button(windowGW, width=18, height=2, bg='mint cream', font=ILabelFont, text="세부 사항",
                          command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='light yellow', text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='lightSteelBlue1', text="이름 정렬",
                            command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='RosyBrown1', text="주소 정렬",
                               command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchDaegu():
    global listbox,ILabel
    detailList.clear()
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")
    windowGW.configure(bg='ghost white')

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1,bg='ghost white', text="[대구 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50, y = 10)
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
                detailList.append(carDataList.index(data))
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

    IButton = Button(windowGW, font = ILabelFont, text = "검색",bg='snow2',command =  SearchIn9)
    IButton.pack()
    IButton.place(x= 355, y = 68)

    DetailButton = Button(windowGW, width=18, height=2, bg='mint cream', font=ILabelFont, text="세부 사항",
                          command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='light yellow', text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='lightSteelBlue1', text="이름 정렬",
                            command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='RosyBrown1', text="주소 정렬",
                               command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchBusan():
    global listbox,ILabel
    detailList.clear()
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")
    windowGW.configure(bg='ghost white')

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, bg='ghost white',text="[부산 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50, y = 10)
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
                detailList.append(carDataList.index(data))
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

    IButton = Button(windowGW, font = ILabelFont, text = "검색",bg='snow2',command =  SearchIn10)
    IButton.pack()
    IButton.place(x= 355, y = 68)

    DetailButton = Button(windowGW, width=18, height=2, bg='mint cream', font=ILabelFont, text="세부 사항",
                          command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='light yellow', text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='lightSteelBlue1', text="이름 정렬",
                            command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='RosyBrown1', text="주소 정렬",
                               command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchGyeongNam():
    global listbox,ILabel
    detailList.clear()
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")
    windowGW.configure(bg='ghost white')

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, bg='ghost white',text="[경상남도 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50, y = 10)
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

    IButton = Button(windowGW, font = ILabelFont, text = "검색",bg='snow2',command =  SearchIn11)
    IButton.pack()
    IButton.place(x= 355, y = 68)

    DetailButton = Button(windowGW, width=18, height=2, bg='mint cream', font=ILabelFont, text="세부 사항",
                          command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='light yellow', text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='lightSteelBlue1', text="이름 정렬",
                            command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='RosyBrown1', text="주소 정렬",
                               command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchChungBuk():
    global listbox,ILabel
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")
    windowGW.configure(bg='ghost white')

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, bg='ghost white',text="[충청북도 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50, y = 10)
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
                detailList.append(carDataList.index(data))
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

    IButton = Button(windowGW, font = ILabelFont, text = "검색",bg='snow2',command =  SearchIn12)
    IButton.pack()
    IButton.place(x= 355, y = 68)

    DetailButton = Button(windowGW, width=18, height=2, bg='mint cream', font=ILabelFont, text="세부 사항",
                          command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='light yellow', text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='lightSteelBlue1', text="이름 정렬",
                            command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='RosyBrown1', text="주소 정렬",
                               command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchUlSan():
    global listbox,ILabel
    detailList.clear()
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")
    windowGW.configure(bg='ghost white')

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, bg='ghost white',text="[울산 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50, y = 10)
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
                detailList.append(carDataList.index(data))
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

    IButton = Button(windowGW, font = ILabelFont, text = "검색",bg='snow2',command =  SearchIn13)
    IButton.pack()
    IButton.place(x= 355, y = 68)

    DetailButton = Button(windowGW, width=18, height=2, bg='mint cream', font=ILabelFont, text="세부 사항",
                          command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='light yellow', text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='lightSteelBlue1', text="이름 정렬",
                            command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='RosyBrown1', text="주소 정렬",
                               command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchIncheon():
    global listbox, ILabel
    detailList.clear()
    listvari = [] * 1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")
    windowGW.configure(bg='ghost white')

    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, bg='ghost white',text="[인천 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50, y = 10)
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
                detailList.append(carDataList.index(data))
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

    IButton = Button(windowGW, font=ILabelFont, text="검색",bg='snow2', command=SearchIn15)
    IButton.pack()
    IButton.place(x= 355, y = 68)

    DetailButton = Button(windowGW, width=18, height=2, bg='mint cream', font=ILabelFont, text="세부 사항",
                          command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='light yellow', text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='lightSteelBlue1', text="이름 정렬",
                            command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='RosyBrown1', text="주소 정렬",
                               command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchSeoul():
    global listbox,ILabel
    detailList.clear()
    listvari =[]*1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")
    windowGW.configure(bg='ghost white')

    frame = tkinter.Frame(windowGW)
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, bg='ghost white',text="[서울 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50, y = 10)
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
                detailList.append(carDataList.index(data))
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

    IButton = Button(windowGW, font = ILabelFont, text = "검색",bg='snow2',command =  SearchIn14)
    IButton.pack()
    IButton.place(x= 355, y = 68)

    DetailButton = Button(windowGW, width=18, height=2, bg='mint cream', font=ILabelFont, text="세부 사항",
                          command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='light yellow', text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='lightSteelBlue1', text="이름 정렬",
                            command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='RosyBrown1', text="주소 정렬",
                               command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchJejoo():
    global listbox, ILabel
    detailList.clear()
    listvari = [] * 1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")
    windowGW.configure(bg='ghost white')

    frame = tkinter.Frame(windowGW)
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, bg='ghost white',text="[제주도 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50, y = 10)
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
                detailList.append(carDataList.index(data))
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

    IButton = Button(windowGW, font=ILabelFont, text="검색", bg='snow2',command=SearchIn16)
    IButton.pack()
    IButton.place(x= 355, y = 68)

    DetailButton = Button(windowGW, width=18, height=2, bg='mint cream', font=ILabelFont, text="세부 사항",
                          command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='light yellow', text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='lightSteelBlue1', text="이름 정렬",
                            command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='RosyBrown1', text="주소 정렬",
                               command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def SearchAll():
    global listbox, ILabel
    detailList.clear()
    listvari = [] * 1000
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")
    windowGW.configure(bg='ghost white')

    frame = tkinter.Frame(windowGW)
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, bg='ghost white',text="[전국 렌터카 업체 정보]")
    TopLabel.pack()
    TopLabel.place(x=50, y = 10)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side=RIGHT, expand=True, fill=Y)
    RenderTextHorizonbar = Scrollbar(frame, orient=HORIZONTAL)
    RenderTextHorizonbar.pack(side=BOTTOM, fill=X, expand=True)

    listbox = tkinter.Listbox(frame, font=TempFont, width=20, height=19, borderwidth=12, relief='ridge',
                              yscrollcommand=RenderTextScrollbar.set, xscrollcommand=RenderTextHorizonbar.set)


    for data in carDataList:
        text = str(data.address) + "[" + data.name + "]"
        listbox.insert(END, text)
        detailList.append(carDataList.index(data))

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

    IButton = Button(windowGW, font=ILabelFont, text="검색", bg='snow2',command=SearchInAll)
    IButton.pack()
    IButton.place(x= 355, y = 68)

    DetailButton = Button(windowGW, width=18, height=2, bg='mint cream', font=ILabelFont, text="세부 사항",
                          command=DetailText1)
    DetailButton.pack()
    DetailButton.place(x=215, y=130)

    MapButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='light yellow', text="맵 보기", command=MapImage1)
    MapButton.pack()
    MapButton.place(x=215, y=210)

    SortNameButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='lightSteelBlue1', text="이름 정렬",
                            command=SortNameList)
    SortNameButton.pack()
    SortNameButton.place(x=215, y=290)

    SortAddressButton = Button(windowGW, width=18, height=2, font=ILabelFont, bg='RosyBrown1', text="주소 정렬",
                               command=SortAddressList)
    SortAddressButton.pack()
    SortAddressButton.place(x=215, y=370)

def DetailText1():
    windowGW = Tk("GangWon")
    windowGW.geometry("400x450")
    windowGW.configure(bg='ghost white')


    frame = tkinter.Frame(windowGW)
    TempFont = font.Font(windowGW, size=10, weight='bold', family='Conslas')
    TempFont1 = font.Font(windowGW, size=20, weight='bold', family='Conslas')

    TopLabel = Label(windowGW, font=TempFont1, bg='ghost white',text="[세부 사항]")
    TopLabel.pack()
    TopLabel.place(x=135, y = 10)
    RenderTextScrollbar = Scrollbar(frame)
    RenderTextScrollbar.pack(side=RIGHT, expand=True, fill=Y)
    RenderTextHorizonbar = Scrollbar(frame, orient=HORIZONTAL)
    RenderTextHorizonbar.pack(side=BOTTOM, fill=X, expand=True)

    detailListbox = tkinter.Listbox(frame, font=TempFont, width=44, height=15, borderwidth=12, relief='ridge',
                              yscrollcommand=RenderTextScrollbar.set, xscrollcommand=RenderTextHorizonbar.set)

    detailListbox.pack(side=LEFT, fill=Y)
    RenderTextScrollbar.config(command=detailListbox.yview)
    RenderTextScrollbar.pack(side=RIGHT, expand=True, fill=Y)
    RenderTextHorizonbar.config(command=detailListbox.xview)
    RenderTextHorizonbar.pack(side=BOTTOM, expand=True, fill=X)
    detailListbox.activate(0)

    frame.pack()
    frame.place(x=20, y=70)

    global mailEntry
    mailFont = font.Font(windowGW, size=15, weight='bold', family='Consolas')
    mailEntry = Entry(windowGW, font=mailFont, width=24, borderwidth=3, relief='ridge')
    mailEntry.pack()
    mailEntry.place(x=20, y=390)

    EButton = Button(windowGW, font=TempFont,width = 8 , height = 2, text="메일 보내기", bg = 'PaleTurquoise', command= SendMail)
    EButton.pack()
    EButton.place(x=310, y=385)

    #searchAddress,searchName = str(listbox.get(ACTIVE)).split("[")
    num = detailList[listbox.curselection()[0]]

    if carDataList[num].address !=None:
        text1 = "주소: " +carDataList[num].address
        detailListbox.insert(END,text1)
        global Sendtext1
        Sendtext1 = "주소: " +carDataList[num].address
    else:
        Sendtext1 =""
    if carDataList[num].name != None:
        text2 = "업체명: " +carDataList[num].name
        detailListbox.insert(END,text2)
        global Sendtext2
        Sendtext2 = "업체명: " +carDataList[num].name
    else:
        Sendtext2 =""
    if carDataList[num].TotalCar != None:
        text3 = "자동차보유대수: "+carDataList[num].TotalCar
        detailListbox.insert(END,text3)
        global Sendtext3
        Sendtext3 = "자동차보유대수: "+carDataList[num].TotalCar
    else:
        Sendtext3 =""
    if carDataList[num].s_car != None:
        text4 = "승용차보유대수: "+carDataList[num].s_car
        detailListbox.insert(END,text4)
        global Sendtext4
        Sendtext4 = "승용차보유대수: "+carDataList[num].s_car
    else:
        Sendtext4 =""
    if carDataList[num].b_car != None:
        text5 = "승합차보유대수: "+carDataList[num].b_car
        detailListbox.insert(END,text5)
        global Sendtext5
        Sendtext5 = "승합차보유대수: "+carDataList[num].b_car
    else:
        Sendtext5 =""
    if carDataList[num].telephone != None:
        text6= "전화번호: "+carDataList[num].telephone
        detailListbox.insert(END,text6)
        global Sendtext6
        Sendtext6 = "전화번호: "+carDataList[num].telephone
    else:
        Sendtext6 =""
    if carDataList[num].weekday_start != None:
        text7 = "평일운영시작시각: "+carDataList[num].weekday_start
        detailListbox.insert(END,text7)
        global Sendtext7
        Sendtext7 = "평일운영시작시각: "+carDataList[num].weekday_start
    else:
        Sendtext7 =""
    if carDataList[num].weekday_end != None:
        text8 = "평일운영종료시각: "+carDataList[num].weekday_end
        detailListbox.insert(END,text8)
        global Sendtext8
        Sendtext8 = "평일운영종료시각: "+carDataList[num].weekday_end
    else:
        Sendtext8 =""
    if carDataList[num].weekend_start != None:
        text9 = "주말운영시작시각: "+carDataList[num].weekend_start
        detailListbox.insert(END,text9)
        global Sendtext9
        Sendtext9 = "주말운영시작시각: "+carDataList[num].weekend_start
    else:
        Sendtext9 = ""
    if carDataList[num].weekend_end != None:
        text10 ="주말운영종료시각: "+carDataList[num].weekend_end
        detailListbox.insert(END,text10)
        global Sendtext10
        Sendtext10 ="주말운영종료시각: "+carDataList[num].weekend_end
    else:
        Sendtext10=""
    if carDataList[num].personal_day != None:
        text11 = "휴무일: "+carDataList[num].personal_day
        detailListbox.insert(END,text11)
        global Sendtext11
        Sendtext11 = "휴무일: "+carDataList[num].personal_day
    else:
        Sendtext11 = ""
    if carDataList[num].homepage != None:
        text12 = "홈페이지주소: "+carDataList[num].homepage
        detailListbox.insert(END,text12)
        global Sendtext12
        Sendtext12 = "홈페이지주소: "+carDataList[num].homepage
    else:
        Sendtext12= ""

    global SendAllText
    SendAllText = Sendtext1 + "\n" + Sendtext2 + "\n" +Sendtext3 + "\n" + Sendtext4 + "\n" + Sendtext5 + "\n" + Sendtext6 + "\n" + Sendtext7 + "\n" + Sendtext8 + "\n" + Sendtext9 + "\n" + Sendtext10 + "\n" + Sendtext11 + "\n" +Sendtext12
    #print(SendAllText)

def SendMail():
    #print(str(mailEntry.get()))
    EmailAddress = str(mailEntry.get())
    SendText = SendAllText
    sendEmail.SendEmail(EmailAddress,SendText)

def MapImage1():
    num = detailList[listbox.curselection()[0]]

    map_osm = folium.Map(location=[float(carDataList[num].latitude), float(carDataList[num].longitude)], zoom_start=15 )
    folium.Marker([carDataList[num].latitude, carDataList[num].longitude], popup=carDataList[num].name,
                  icon=folium.Icon(color ='red', icon='info-sign')).add_to(map_osm)

    filepath = "Map.html"
    map_osm.save(filepath)
    webbrowser.open_new_tab(filepath)

def AllMap():
    map_osm = folium.Map(location=[37.3402849,126.7313189], zoom_start=15)
    i=0
    for data in carDataList:
        folium.Marker([data.latitude,data.longitude], popup=str(i),
                      icon=folium.Icon(color='red', icon='info-sign')).add_to(map_osm)
        i += 1

    map_osm.save("Map.html")


def SortNameList():
   pass

def SortAddressList():
   pass

def SearchIn1():
    detailList.clear()
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("강원도")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                    detailList.append(carDataList.index(data))
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn2():
    detailList.clear()
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("경기도")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                    detailList.append(carDataList.index(data))
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn3():
    detailList.clear()
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("충청남도")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                    detailList.append(carDataList.index(data))
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn4():
    detailList.clear()
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("대전광역시")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                    detailList.append(carDataList.index(data))
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn5():
    detailList.clear()
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("전라북도")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                    detailList.append(carDataList.index(data))
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn6():
    detailList.clear()
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("광주광역시")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                    detailList.append(carDataList.index(data))
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn7():
    detailList.clear()
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("전라남도")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                    detailList.append(carDataList.index(data))
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn8():
    detailList.clear()
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("경상북도")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                    detailList.append(carDataList.index(data))
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn9():
    detailList.clear()
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("대구광역시")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                    detailList.append(carDataList.index(data))
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn10():
    detailList.clear()
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("부산광역시")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                    detailList.append(carDataList.index(data))
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn11():
    detailList.clear()
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("경상남도")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                    detailList.append(carDataList.index(data))
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn12():
    detailList.clear()
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("충청북도")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                    detailList.append(carDataList.index(data))
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn13():
    detailList.clear()
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("울산광역시")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                    detailList.append(carDataList.index(data))
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn14():
    detailList.clear()
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("서울특별")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                    detailList.append(carDataList.index(data))
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn15():
    detailList.clear()
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("인천광역시")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                    detailList.append(carDataList.index(data))
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchIn16():
    detailList.clear()
    listbox.delete(0,5000)
    searchTemp= str(ILabel.get())
    city = str("제주특별")
    for data in carDataList:
        if city in str(data.address):
            if searchTemp in str(data.address) or searchTemp in str(data.name):
                try:
                    text = data.address+" ["+data.name+"]"
                    detailList.append(carDataList.index(data))
                except:
                    print("error")
                    # if data.address == None:
                    #     text = data.address+" ["+data.name+"]"

                listbox.insert(END,text)

def SearchInAll():                                 # 전체 검색
    detailList.clear()
    listbox.delete(0,50000)
    searchTemp= str(ILabel.get())
    for data in carDataList:
        if searchTemp in str(data.address) or searchTemp in str(data.name):
            try:
                text = "["+data.address+"] "+data.name
                detailList.append(carDataList.index(data))
            except:
                print("error")
                if data.address == None:
                    break
            listbox.insert(END,text)

pwindow = Tk("Korea Lent Car Info")
pwindow.geometry("400x450")
pwindow.configure(bg='ghost white')
DataList = []
mapImage = PhotoImage(file='Resorce/대한민국 지도.gif')

MainImage = Label(pwindow, image=mapImage)
MainImage.pack()
MainImage.place(x= 50, y = 50)
TempFont = font.Font(pwindow, size = 8, weight ='bold' , family ='Conslas')

searchGanWonButton = Button(pwindow, font = TempFont, text ="강원도", bg = 'DarkSeaGreen2', command = SearchGangWondo)
searchGanWonButton.pack()
searchGanWonButton.place(x = 205, y=70)

searchGyeonggidoButton = Button(pwindow, font = TempFont, text ="경기도",bg = 'lemon chiffon', command = SearchKyeongKiDo)
searchGyeonggidoButton.pack()
searchGyeonggidoButton.place(x = 135, y=130)

searchChoongNamButton = Button(pwindow, font = TempFont, text ="충청남도", bg = 'yellow', command = SearchChungNam)
searchChoongNamButton.pack()
searchChoongNamButton.place(x = 105, y=170)

searchDaejeonButton = Button(pwindow, font = TempFont, text ="대전", bg = 'royal blue', command = SearchDaeJeon)
searchDaejeonButton.pack()
searchDaejeonButton.place(x = 150, y=200)

searchJeonRaBukButton = Button(pwindow, font = TempFont, text ="전라북도", bg = 'yellow green', command = SearchJeonBuk)
searchJeonRaBukButton.pack()
searchJeonRaBukButton.place(x = 120, y=250)

searchGwangjuButton = Button(pwindow, font = TempFont, text =" 광주 ", bg = 'yellow2', command = SearchGwangJu)
searchGwangjuButton.pack()
searchGwangjuButton.place(x = 135, y=300)

searchJeonRaNamButton = Button(pwindow, font = TempFont, text ="전라남도", bg = 'pale violet red',command = SearchJeonNam)
searchJeonRaNamButton.pack()
searchJeonRaNamButton.place(x = 115, y=330)

searchGyeongSangBukButton = Button(pwindow, font = TempFont, text ="경상북도", bg = 'orchid1',command = SearchGyeongBuk)
searchGyeongSangBukButton.pack()
searchGyeongSangBukButton.place(x = 220, y=190)

searchDaeguButton = Button(pwindow, font = TempFont, text =" 대구 ",bg ='sienna1', command = SearchDaegu)
searchDaeguButton.pack()
searchDaeguButton.place(x = 235, y=240)

searchUlSanButton = Button(pwindow, font = TempFont, text ="울산",bg = 'cornflower blue', command = SearchUlSan)
searchUlSanButton.pack()
searchUlSanButton.place(x = 285, y=275)

searchBuSanButton = Button(pwindow, font = TempFont, text =" 부산 ",bg ='light goldenrod', command = SearchBusan)
searchBuSanButton.pack()
searchBuSanButton.place(x = 265, y=305)

searchJeJooButton = Button(pwindow, font = TempFont, text =" 제주도 ",bg = 'tan1', command = SearchJejoo)
searchJeJooButton.pack()
searchJeJooButton.place(x = 255, y=365)


searchGyeongSangNamButton = Button(pwindow, font = TempFont, text ="경상남도",bg ='PaleTurquoise2', command = SearchGyeongNam)
searchGyeongSangNamButton.pack()
searchGyeongSangNamButton.place(x = 205, y=280)

searchChoongBukButton = Button(pwindow, font = TempFont, text ="충청북도", bg ='PeachPuff2', command = SearchChungBuk)
searchChoongBukButton.pack()
searchChoongBukButton.place(x = 180, y=140)

searchIncheonButton = Button(pwindow, font = TempFont, text =" 인천 ",bg ='salmon1', command = SearchIncheon)
searchIncheonButton.pack()
searchIncheonButton.place(x = 100, y=90)

searchSeoulButton = Button(pwindow, font = TempFont, text =" 서울 ",bg ='lightPink1', command = SearchSeoul)
searchSeoulButton.pack()
searchSeoulButton.place(x = 145, y=90)

searchAllButton = Button(pwindow, font = TempFont, bg = 'papaya whip' ,text =" 전국 ", command = SearchAll)
searchAllButton.pack()
searchAllButton.place(x = 275, y=60)

def initTopText():
    TempFont = font.Font(pwindow , size=20, weight='bold', family='Conslas')
    MainText = Label(pwindow, font = TempFont, bg='ghost white',text = "[전국 렌터카 업체 정보]")
    MainText.pack()
    MainText.place(x=50)

initTopText()
pwindow.mainloop()
#AllMap()



