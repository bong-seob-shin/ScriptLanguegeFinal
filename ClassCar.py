class CarData:
    def __init__(self,name,address,latitude,longitude,TotalCar,s_car,b_car,telephone,
                 weekday_start,weekday_end,weekend_start,weekend_end,personal_day, homepage):
        self.name=name
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.TotalCar=TotalCar
        self.s_car=s_car
        self.b_car=b_car
        self.telephone = telephone
        self.weekday_start = weekday_start
        self.weekday_end = weekday_end
        self.weekend_start = weekend_start
        self.weekend_end = weekend_end
        self.personal_day = personal_day
        self.homepage = homepage
    def getCarDataByAdrress(self,string):
        if string == self.address:
            return CarData


    def showData(self):
        print("업체명: ", self.name)
        print("소재지도로명주소: ", self.address)
        print("위도: ", self.latitude)
        print("경도: ", self.longitude)
        print("자동차보유대수 ", self.TotalCar)
        print("승용차보유대수: ", self.s_car)
        print("승합차보유대수: ", self.b_car)
        print("전화번호: ", self.telephone)
        print("평일운영시작시각: ", self.weekday_start)
        print("평일운영종료시각: ", self.weekday_end)
        print("주말운영시작시각: ", self.weekend_start)
        print("평일운영종료시각: ", self.weekend_end)
        print("휴무일: ", self.personal_day)
        print("홈페이지주소: ",self.homepage)

    def getName(self):
        return self.name

    def getaddress(self):
        return self.address

    def getlatitude(self):
        return self.latitude

    def getlongtitude(self):
        return self.longitude

