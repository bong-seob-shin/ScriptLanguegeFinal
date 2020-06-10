#-*- encoding: utf-8 -*

import dataLoad
import CarClass
from haversine import haversine
from tkinter import *
from tkinter import font
import tkinter.messagebox
import folium
import webbrowser
import tkinter.ttk

carDataList = []

Data = dataLoad.LoadData()

for data in Data.find_all("record"):
    name = str(data.업체명)
    print(name)
    address = data.소재지도로명주소
    latitude = data.위도
    longitude = data.경도
    TotalCar = data.자동차보유대수
    s_car = data.승용차보유대수
    b_car = data.승합차보유대수
    telephone = data.전화번호
    weekday_start = data.평일운영시작시각
    weekday_end = data.평일운영종료시각
    weekend_start = data.주말운영시작시각
    weekend_end = data.주말운영종료시각
    personal_day = data.휴무일
    homepage = data.홈페이지주소

    Car = CarClass.CarData(name,address,latitude,longitude,TotalCar,s_car,b_car,telephone,weekday_start,weekday_end,weekend_start,weekend_end,personal_day,homepage)
    carDataList.append(Car)

