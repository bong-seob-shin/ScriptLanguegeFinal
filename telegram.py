import ClassCar
from xml.etree.ElementTree import parse

Data = parse('전국렌터카.xml')
root = Data.getroot()

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

Datas1 = []
Datas2 = []
Datas3 = []
Datas4 = []
Datas5 = []
Datas6 = []
Datas7 = []
Datas8 = []
Datas9 = []
Datas10 = []
Datas11 = []
Datas12 = []
Datas13 = []
Datas14 = []
Datas15 = []
Datas16 = []
Datas17 = []
Datas18 = []
Datas19 = []
Datas20 = []
Datas21 = []
Datas22 = []
Datas23 = []
Datas24 = []
Datas25 = []
Datas26 = []
Datas27 = []
Datas28 = []
Datas29 = []
Datas30 = []
Datas31 = []
Datas32 = []
Datas33 = []
Datas34 = []
Datas35 = []
Datas36 = []
Datas37 = []
Datas38 = []
Datas39 = []
Datas40 = []
Datas41 = []
Datas42 = []
Datas43 = []
Datas44 = []
Datas45 = []
Datas46 = []
Datas47 = []
Datas48 = []
Datas49 = []
Datas50 = []
Datas51 = []
Datas52 = []
Datas53 = []
Datas54 = []
Datas55 = []
Datas56 = []
Datas57 = []
Datas58 = []
Datas59 = []
Datas60 = []
Datas61 = []
Datas62 = []
Datas63 = []
Datas64 = []
Datas65 = []
Datas66 = []
Datas67 = []
Datas68 = []
Datas69 = []
Datas70 = []
Datas71 = []
Datas72 = []
Datas73 = []
Datas74 = []
Datas75 = []
Datas76 = []
Datas77 = []
Datas78 = []
Datas79 = []
Datas80 = []
Datas81 = []
Datas82 = []
Datas83 = []
Datas84 = []
Datas85 = []
Datas86 = []
Datas87 = []
Datas88 = []
Datas89 = []
Datas90 = []
Datas91 = []
Datas92 = []
Datas93 = []
Datas94 = []
Datas95 = []
Datas96 = []
Datas97 = []
Datas98 = []
Datas99 = []
Datas100 = []
Datas101 = []
Datas102 = []
Datas103 = []
Datas104 = []
Datas105 = []
Datas106 = []
Datas107 = []
Datas108 = []
Datas109 = []
Datas110 = []
Datas111 = []
Datas112 = []
Datas113 = []
Datas114 = []
Datas115 = []
Datas116 = []
Datas117 = []
Datas118 = []
Datas119 = []
Datas120 = []
Datas121 = []
Datas122 = []
Datas123 = []
Datas124 = []
Datas125 = []
Datas126 = []
Datas127 = []
Datas128 = []
Datas129 = []
Datas130 = []
Datas131 = []
Datas132 = []
Datas133 = []
Datas134 = []
Datas135 = []
Datas136 = []
Datas137 = []
Datas138 = []
Datas139 = []
Datas140 = []
Datas141 = []
Datas142 = []
Datas143 = []
Datas144 = []
Datas145 = []
Datas146 = []
Datas147 = []
Datas148 = []
Datas149 = []
Datas150 = []
Datas151 = []
Datas152 = []
Datas153 = []
Datas154 = []
Datas155 = []
Datas156 = []
Datas157 = []
Datas158 = []
Datas159 = []
Datas160 = []
Datas161 = []
Datas162 = []
Datas163 = []
Datas164 = []
Datas165 = []
Datas166 = []
Datas167 = []
Datas168 = []
Datas169 = []
Datas170 = []
Datas171 = []
Datas172 = []
Datas173 = []
Datas174 = []
Datas175 = []
Datas176 = []
Datas177 = []
Datas178 = []
Datas179 = []
Datas180 = []
Datas181 = []
Datas182 = []
Datas183 = []
Datas184 = []
Datas185 = []
Datas186 = []
Datas187 = []
Datas188 = []
Datas189 = []
Datas190 = []
Datas191 = []
Datas192 = []
Datas193 = []
Datas194 = []
Datas195 = []
Datas196 = []
Datas197 = []
Datas198 = []
Datas199 = []
Datas200 = []

city1 = str("인천광역시 미추홀구")
for data in carDataList:
    if city1 in str(data.address):
        Datas1.append(data.address)
        Datas1.append(data.name)
        Datas1.append(data.telephone)
        a1 = '\n'.join(Datas1)

city2 = str("인천광역시 서구")
for data in carDataList:
    if city2 in str(data.address):
        Datas2.append(data.address)
        Datas2.append(data.name)
        Datas2.append(data.telephone)
        a2 = '\n'.join(Datas2)
city3 = str("인천광역시 남동구")
for data in carDataList:
    if city3 in str(data.address):
        Datas3.append(data.address)
        Datas3.append(data.name)
        Datas3.append(data.telephone)
        a3 = '\n'.join(Datas3)

city4 = str("인천광역시 연수구")
for data in carDataList:
    if city4 in str(data.address):
        Datas4.append(data.address)
        Datas4.append(data.name)
        Datas4.append(data.telephone)
        a4 = '\n'.join(Datas4)

city5 = str("인천광역시 계양구")
for data in carDataList:
    if city5 in str(data.address):
        Datas5.append(data.address)
        Datas5.append(data.name)
        Datas5.append(data.telephone)
        a5 = '\n'.join(Datas5)

city6 = str("인천광역시 부평구")
for data in carDataList:
    if city6 in str(data.address):
        Datas6.append(data.address)
        Datas6.append(data.name)
        Datas6.append(data.telephone)
        a6 = '\n'.join(Datas6)
city7 = str("인천광역시 중구")
for data in carDataList:
    if city7 in str(data.address):
        Datas7.append(data.address)
        Datas7.append(data.name)
        Datas7.append(data.telephone)
        a7 = '\n'.join(Datas7)
city8 = str("인천광역시 동구")
for data in carDataList:
    if city8 in str(data.address):
        Datas8.append(data.address)
        Datas8.append(data.name)
        Datas8.append(data.telephone)
        a8 = '\n'.join(Datas8)
city9 = str("인천광역시 옹진군")
for data in carDataList:
    if city9 in str(data.address):
        Datas9.append(data.address)
        Datas9.append(data.name)
        Datas9.append(data.telephone)
        a9 = '\n'.join(Datas9)
city10 = str("인천광역시 부평구")
for data in carDataList:
    if city10 in str(data.address):
        Datas10.append(data.address)
        Datas10.append(data.name)
        Datas10.append(data.telephone)
        a10 = '\n'.join(Datas10)

city11 = str("서울특별시 중구")
for data in carDataList:
    if city11 in str(data.address):
        Datas11.append(data.address)
        Datas11.append(data.name)
        Datas11.append(data.telephone)
        a11 = '\n'.join(Datas11)
city12 = str("서울특별시  서대문구")
for data in carDataList:
    if city12 in str(data.address):
        Datas12.append(data.address)
        Datas12.append(data.name)
        Datas12.append(data.telephone)
        a12 = '\n'.join(Datas12)
city13 = str("서울특별시 노원구")
for data in carDataList:
    if city13 in str(data.address):
        Datas13.append(data.address)
        Datas13.append(data.name)
        Datas13.append(data.telephone)
        a13 = '\n'.join(Datas13)
city14 = str("서울특별시 서초구")
for data in carDataList:
    if city14 in str(data.address):
        Datas14.append(data.address)
        Datas14.append(data.name)
        Datas14.append(data.telephone)
        a14 = '\n'.join(Datas14)
city15 = str("서울특별시 강북구")
for data in carDataList:
    if city15 in str(data.address):
        Datas15.append(data.address)
        Datas15.append(data.name)
        Datas15.append(data.telephone)
        a15 = '\n'.join(Datas15)
city16 = str("서울특별시 송파구")
for data in carDataList:
    if city16 in str(data.address):
        Datas16.append(data.address)
        Datas16.append(data.name)
        Datas16.append(data.telephone)
        a16 = '\n'.join(Datas16)
city17 = str("서울특별시 중랑구")
for data in carDataList:
    if city17 in str(data.address):
        Datas17.append(data.address)
        Datas17.append(data.name)
        Datas17.append(data.telephone)
        a17 = '\n'.join(Datas17)
city18 = str("서울특별시 광진구")
for data in carDataList:
    if city18 in str(data.address):
        Datas18.append(data.address)
        Datas18.append(data.name)
        Datas18.append(data.telephone)
        a18 = '\n'.join(Datas18)
city19 = str("서울특별시 강남구")
for data in carDataList:
    if city19 in str(data.address):
        Datas19.append(data.address)
        Datas19.append(data.name)
        Datas19.append(data.telephone)
        a19 = '\n'.join(Datas19)
city20 = str("서울특별시 관악구")
for data in carDataList:
    if city20 in str(data.address):
        Datas20.append(data.address)
        Datas20.append(data.name)
        Datas20.append(data.telephone)
        a20 = '\n'.join(Datas20)
city21 = str("서울특별시 은평구")
for data in carDataList:
    if city21 in str(data.address):
        Datas21.append(data.address)
        Datas21.append(data.name)
        Datas21.append(data.telephone)
        a21 = '\n'.join(Datas21)
city22 = str("서울특별시 구로구")
for data in carDataList:
    if city22 in str(data.address):
        Datas22.append(data.address)
        Datas22.append(data.name)
        Datas22.append(data.telephone)
        a22 = '\n'.join(Datas22)
city23 = str("서울특별시 영등포구")
for data in carDataList:
    if city23 in str(data.address):
        Datas23.append(data.address)
        Datas23.append(data.name)
        Datas23.append(data.telephone)
        a23 = '\n'.join(Datas23)
city24 = str("서울특별시 양천구")
for data in carDataList:
    if city24 in str(data.address):
        Datas24.append(data.address)
        Datas24.append(data.name)
        Datas24.append(data.telephone)
        a24 = '\n'.join(Datas24)
city25 = str("서울특별시 강동구")
for data in carDataList:
    if city25 in str(data.address):
        Datas25.append(data.address)
        Datas25.append(data.name)
        Datas25.append(data.telephone)
        a25 = '\n'.join(Datas25)
city26 = str("서울특별시 도봉구")
for data in carDataList:
    if city26 in str(data.address):
        Datas26.append(data.address)
        Datas26.append(data.name)
        Datas26.append(data.telephone)
        a26 = '\n'.join(Datas26)
city27 = str("서울특별시 강서구")
for data in carDataList:
    if city27 in str(data.address):
        Datas27.append(data.address)
        Datas27.append(data.name)
        Datas27.append(data.telephone)
        a27 = '\n'.join(Datas27)
city28 = str("서울특별시 동대문구")
for data in carDataList:
    if city28 in str(data.address):
        Datas28.append(data.address)
        Datas28.append(data.name)
        Datas28.append(data.telephone)
        a28 = '\n'.join(Datas28)
city29 = str("서울특별시 금천구")
for data in carDataList:
    if city29 in str(data.address):
        Datas29.append(data.address)
        Datas29.append(data.name)
        Datas29.append(data.telephone)
        a29 = '\n'.join(Datas29)
city30 = str("서울특별시 성동구")
for data in carDataList:
    if city30 in str(data.address):
        Datas30.append(data.address)
        Datas30.append(data.name)
        Datas30.append(data.telephone)
        a30 = '\n'.join(Datas30)
city31 = str("서울특별시 종로구")
for data in carDataList:
    if city31 in str(data.address):
        Datas31.append(data.address)
        Datas31.append(data.name)
        Datas31.append(data.telephone)
        a31 = '\n'.join(Datas31)
city32 = str("서울특별시 성북구")
for data in carDataList:
    if city32 in str(data.address):
        Datas32.append(data.address)
        Datas32.append(data.name)
        Datas32.append(data.telephone)
        a32 = '\n'.join(Datas32)
city33 = str("서울특별시 용산구")
for data in carDataList:
    if city33 in str(data.address):
        Datas33.append(data.address)
        Datas33.append(data.name)
        Datas33.append(data.telephone)
        a33 = '\n'.join(Datas33)
city34 = str("서울특별시 동대문구")
for data in carDataList:
    if city34 in str(data.address):
        Datas34.append(data.address)
        Datas34.append(data.name)
        Datas34.append(data.telephone)
        a34 = '\n'.join(Datas34)
city35 = str("서울특별시 마포구")
for data in carDataList:
    if city35 in str(data.address):
        Datas35.append(data.address)
        Datas35.append(data.name)
        Datas35.append(data.telephone)
        a35 = '\n'.join(Datas35)
city36 = str("강원도 태백시")
for data in carDataList:
    if city36 in str(data.address):
        Datas36.append(data.address)
        Datas36.append(data.name)
        Datas36.append(data.telephone)
        a36 = '\n'.join(Datas36)
city37 = str("강원도 강릉시")
for data in carDataList:
    if city37 in str(data.address):
        Datas37.append(data.address)
        Datas37.append(data.name)
        Datas37.append(data.telephone)
        a37 = '\n'.join(Datas37)
city38 = str("강원도 동해시")
for data in carDataList:
    if city38 in str(data.address):
        Datas38.append(data.address)
        Datas38.append(data.name)
        Datas38.append(data.telephone)
        a38 = '\n'.join(Datas38)
city39 = str("강원도 홍천군")
for data in carDataList:
    if city39 in str(data.address):
        Datas39.append(data.address)
        Datas39.append(data.name)
        Datas39.append(data.telephone)
        a39 = '\n'.join(Datas39)
city40 = str("강원도 강릉시")
for data in carDataList:
    if city40 in str(data.address):
        Datas40.append(data.address)
        Datas40.append(data.name)
        Datas40.append(data.telephone)
        a40 = '\n'.join(Datas40)
city41 = str("강원도 춘천시")
for data in carDataList:
    if city41 in str(data.address):
        Datas41.append(data.address)
        Datas41.append(data.name)
        Datas41.append(data.telephone)
        a41 = '\n'.join(Datas2)
city42 = str("강원도 평창군")
for data in carDataList:
    if city42 in str(data.address):
        Datas42.append(data.address)
        Datas42.append(data.name)
        Datas42.append(data.telephone)
        a42 = '\n'.join(Datas42)
city43 = str("강원도 원주시")
for data in carDataList:
    if city43 in str(data.address):
        Datas43.append(data.address)
        Datas43.append(data.name)
        Datas43.append(data.telephone)
        a43 = '\n'.join(Datas43)
city44 = str("강원도 인제군")
for data in carDataList:
    if city44 in str(data.address):
        Datas44.append(data.address)
        Datas44.append(data.name)
        Datas44.append(data.telephone)
        a44 = '\n'.join(Datas44)
city45 = str("강원도 횡성군")
for data in carDataList:
    if city45 in str(data.address):
        Datas45.append(data.address)
        Datas45.append(data.name)
        Datas45.append(data.telephone)
        a45 = '\n'.join(Datas45)
city46 = str("강원도 영월군")
for data in carDataList:
    if city46 in str(data.address):
        Datas46.append(data.address)
        Datas46.append(data.name)
        Datas46.append(data.telephone)
        a46 = '\n'.join(Datas46)
city47 = str("강원도 속초시")
for data in carDataList:
    if city47 in str(data.address):
        Datas47.append(data.address)
        Datas47.append(data.name)
        Datas47.append(data.telephone)
        a47 = '\n'.join(Datas47)
city48 = str("강원도 철원군")
for data in carDataList:
    if city48 in str(data.address):
        Datas48.append(data.address)
        Datas48.append(data.name)
        Datas48.append(data.telephone)
        a48 = '\n'.join(Datas48)
city49 = str("강원도 양양군")
for data in carDataList:
    if city49 in str(data.address):
        Datas49.append(data.address)
        Datas49.append(data.name)
        Datas49.append(data.telephone)
        a49 = '\n'.join(Datas49)
city50 = str("강원도 양구군")
for data in carDataList:
    if city50 in str(data.address):
        Datas50.append(data.address)
        Datas50.append(data.name)
        Datas50.append(data.telephone)
        a50 = '\n'.join(Datas50)

city51 = str("경기도 부천시")
for data in carDataList:
    if city51 in str(data.address):
        Datas51.append(data.address)
        Datas51.append(data.name)
        Datas51.append(data.telephone)
        a51 = '\n'.join(Datas51)

city52 = str("경기도 하남시")
for data in carDataList:
    if city52 in str(data.address):
        Datas52.append(data.address)
        Datas52.append(data.name)
        Datas52.append(data.telephone)
        a52 = '\n'.join(Datas52)

city53 = str("경기도 성남시")
for data in carDataList:
    if city53 in str(data.address):
        Datas53.append(data.address)
        Datas53.append(data.name)
        Datas53.append(data.telephone)
        a53 = '\n'.join(Datas53)
city54 = str("경기도 수원시")
for data in carDataList:
    if city54 in str(data.address):
        Datas54.append(data.address)
        Datas54.append(data.name)
        Datas54.append(data.telephone)
        a54 = '\n'.join(Datas54)

city55 = str("경기도 화성시")
for data in carDataList:
    if city55 in str(data.address):
        Datas55.append(data.address)
        Datas55.append(data.name)
        Datas55.append(data.telephone)
        a55 = '\n'.join(Datas55)
city56 = str("경기도 군포시")
for data in carDataList:
    if city56 in str(data.address):
        Datas56.append(data.address)
        Datas56.append(data.name)
        Datas56.append(data.telephone)
        a56 = '\n'.join(Datas56)

city57 = str("경기도 평택시")
for data in carDataList:
    if city57 in str(data.address):
        Datas57.append(data.address)
        Datas57.append(data.name)
        Datas57.append(data.telephone)
        a57 = '\n'.join(Datas57)
city58 = str("경기도 김포시")
for data in carDataList:
    if city58 in str(data.address):
        Datas58.append(data.address)
        Datas58.append(data.name)
        Datas58.append(data.telephone)
        a58 = '\n'.join(Datas58)

city59 = str("경기도 시흥시")
for data in carDataList:
    if city59 in str(data.address):
        Datas59.append(data.address)
        Datas59.append(data.name)
        Datas59.append(data.telephone)
        a59 = '\n'.join(Datas59)

city61 = str("경기도 용인시")
for data in carDataList:
    if city61 in str(data.address):
        Datas61.append(data.address)
        Datas61.append(data.name)
        Datas61.append(data.telephone)
        a61 = '\n'.join(Datas61)

city62 = str("경기도 양평군")
for data in carDataList:
    if city62 in str(data.address):
        Datas62.append(data.address)
        Datas62.append(data.name)
        Datas62.append(data.telephone)
        a62 = '\n'.join(Datas63)
city63 = str("경기도 남양주시")
for data in carDataList:
    if city63 in str(data.address):
        Datas63.append(data.address)
        Datas63.append(data.name)
        Datas63.append(data.telephone)
        a63 = '\n'.join(Datas63)

city64 = str("경기도 양주시")
for data in carDataList:
    if city64 in str(data.address):
        Datas64.append(data.address)
        Datas64.append(data.name)
        Datas64.append(data.telephone)
        a64 = '\n'.join(Datas64)
city65 = str("경기도 고양시")
for data in carDataList:
    if city65 in str(data.address):
        Datas65.append(data.address)
        Datas65.append(data.name)
        Datas65.append(data.telephone)
        a65 = '\n'.join(Datas65)

city66 = str("경기도 과천시")
for data in carDataList:
    if city66 in str(data.address):
        Datas66.append(data.address)
        Datas66.append(data.name)
        Datas66.append(data.telephone)
        a66 = '\n'.join(Datas66)
city67 = str("경기도 이천시")
for data in carDataList:
    if city67 in str(data.address):
        Datas67.append(data.address)
        Datas67.append(data.name)
        Datas67.append(data.telephone)
        a67 = '\n'.join(Datas67)

city68 = str("경기도 오산시")
for data in carDataList:
    if city68 in str(data.address):
        Datas68.append(data.address)
        Datas68.append(data.name)
        Datas68.append(data.telephone)
        a68 = '\n'.join(Datas68)
city69 = str("경기도 광주시")
for data in carDataList:
    if city69 in str(data.address):
        Datas69.append(data.address)
        Datas69.append(data.name)
        Datas69.append(data.telephone)
        a69 = '\n'.join(Datas69)

city70 = str("경기도 의왕시")
for data in carDataList:
    if city70 in str(data.address):
        Datas70.append(data.address)
        Datas70.append(data.name)
        Datas70.append(data.telephone)
        a70 = '\n'.join(Datas70)
city71 = str("경기도 안산시")
for data in carDataList:
    if city71 in str(data.address):
        Datas71.append(data.address)
        Datas71.append(data.name)
        Datas71.append(data.telephone)
        a71 = '\n'.join(Datas71)

city72 = str("경기도 구리시")
for data in carDataList:
    if city72 in str(data.address):
        Datas72.append(data.address)
        Datas72.append(data.name)
        Datas72.append(data.telephone)
        a72 = '\n'.join(Datas72)
city73 = str("경기도 동두천시")
for data in carDataList:
    if city73 in str(data.address):
        Datas73.append(data.address)
        Datas73.append(data.name)
        Datas73.append(data.telephone)
        a73 = '\n'.join(Datas73)

city74 = str("경기도 연천군")
for data in carDataList:
    if city74 in str(data.address):
        Datas74.append(data.address)
        Datas74.append(data.name)
        Datas74.append(data.telephone)
        a74 = '\n'.join(Datas74)
city75 = str("경기도 파주시")
for data in carDataList:
    if city75 in str(data.address):
        Datas75.append(data.address)
        Datas75.append(data.name)
        Datas75.append(data.telephone)
        a75 = '\n'.join(Datas75)

city76 = str("경기도 포천시")
for data in carDataList:
    if city76 in str(data.address):
        Datas76.append(data.address)
        Datas76.append(data.name)
        Datas76.append(data.telephone)
        a76 = '\n'.join(Datas76)
city77 = str("경기도 안양시")
for data in carDataList:
    if city77 in str(data.address):
        Datas77.append(data.address)
        Datas77.append(data.name)
        Datas77.append(data.telephone)
        a77 = '\n'.join(Datas77)

city78 = str("경기도 의정부시")
for data in carDataList:
    if city78 in str(data.address):
        Datas78.append(data.address)
        Datas78.append(data.name)
        Datas78.append(data.telephone)
        a78 = '\n'.join(Datas78)
city79 = str("경기도 안성시")
for data in carDataList:
    if city79 in str(data.address):
        Datas79.append(data.address)
        Datas79.append(data.name)
        Datas79.append(data.telephone)
        a79 = '\n'.join(Datas79)

city80 = str("경기도 여주시")
for data in carDataList:
    if city80 in str(data.address):
        Datas80.append(data.address)
        Datas80.append(data.name)
        Datas80.append(data.telephone)
        a80 = '\n'.join(Datas80)
city81 = str("경기도 가평군")
for data in carDataList:
    if city81 in str(data.address):
        Datas81.append(data.address)
        Datas81.append(data.name)
        Datas81.append(data.telephone)
        a81 = '\n'.join(Datas81)

city82 = str("경기도 광명시")
for data in carDataList:
    if city82 in str(data.address):
        Datas82.append(data.address)
        Datas82.append(data.name)
        Datas82.append(data.telephone)
        a82 = '\n'.join(Datas82)

city83 = str("충청북도 청주시")
for data in carDataList:
    if city83 in str(data.address):
        Datas83.append(data.address)
        Datas83.append(data.name)
        Datas83.append(data.telephone)
        a83 = '\n'.join(Datas83)
city84 = str("충청북도 진천군")
for data in carDataList:
    if city84 in str(data.address):
        Datas84.append(data.address)
        Datas84.append(data.name)
        Datas84.append(data.telephone)
        a84 = '\n'.join(Datas84)
city85 = str("충청북도 괴산군")
for data in carDataList:
    if city85 in str(data.address):
        Datas85.append(data.address)
        Datas85.append(data.name)
        Datas85.append(data.telephone)
        a85 = '\n'.join(Datas85)
city86 = str("충청북도 충주시")
for data in carDataList:
    if city86 in str(data.address):
        Datas86.append(data.address)
        Datas86.append(data.name)
        Datas86.append(data.telephone)
        a86 = '\n'.join(Datas86)
city87 = str("충청북도 제천시")
for data in carDataList:
    if city87 in str(data.address):
        Datas87.append(data.address)
        Datas87.append(data.name)
        Datas87.append(data.telephone)
        a87 = '\n'.join(Datas87)
city88 = str("충청북도 충주시")
for data in carDataList:
    if city88 in str(data.address):
        Datas88.append(data.address)
        Datas88.append(data.name)
        Datas88.append(data.telephone)
        a88 = '\n'.join(Datas88)
city89 = str("충청북도 단양군")
for data in carDataList:
    if city89 in str(data.address):
        Datas89.append(data.address)
        Datas89.append(data.name)
        Datas89.append(data.telephone)
        a89 = '\n'.join(Datas89)
city90 = str("충청남도 천안시")
for data in carDataList:
    if city90 in str(data.address):
        Datas90.append(data.address)
        Datas90.append(data.name)
        Datas90.append(data.telephone)
        a90 = '\n'.join(Datas90)
city91 = str("충청남도 서산시")
for data in carDataList:
    if city91 in str(data.address):
        Datas91.append(data.address)
        Datas91.append(data.name)
        Datas91.append(data.telephone)
        a91 = '\n'.join(Datas91)
city92 = str("충청남도 홍성군")
for data in carDataList:
    if city92 in str(data.address):
        Datas92.append(data.address)
        Datas92.append(data.name)
        Datas92.append(data.telephone)
        a92 = '\n'.join(Datas92)
city93 = str("충청남도 보령시")
for data in carDataList:
    if city93 in str(data.address):
        Datas93.append(data.address)
        Datas93.append(data.name)
        Datas93.append(data.telephone)
        a93 = '\n'.join(Datas93)
city94 = str("충청남도 논산시")
for data in carDataList:
    if city94 in str(data.address):
        Datas94.append(data.address)
        Datas94.append(data.name)
        Datas94.append(data.telephone)
        a94 = '\n'.join(Datas94)
city95 = str("충청남도 공주시")
for data in carDataList:
    if city95 in str(data.address):
        Datas95.append(data.address)
        Datas95.append(data.name)
        Datas95.append(data.telephone)
        a95 = '\n'.join(Datas95)
city96 = str("충청남도 청양군")
for data in carDataList:
    if city96 in str(data.address):
        Datas96.append(data.address)
        Datas96.append(data.name)
        Datas96.append(data.telephone)
        a96 = '\n'.join(Datas96)

city97 = str("대전광역시 유성구")
for data in carDataList:
    if city97 in str(data.address):
        Datas97.append(data.address)
        Datas97.append(data.name)
        Datas97.append(data.telephone)
        a97 = '\n'.join(Datas97)
city98 = str("대전광역시 서구")
for data in carDataList:
    if city98 in str(data.address):
        Datas98.append(data.address)
        Datas98.append(data.name)
        Datas98.append(data.telephone)
        a98 = '\n'.join(Datas98)
city99 = str("대전광역시 중구")
for data in carDataList:
    if city99 in str(data.address):
        Datas99.append(data.address)
        Datas99.append(data.name)
        Datas99.append(data.telephone)
        a99 = '\n'.join(Datas99)
city100 = str("대전광역시 동구")
for data in carDataList:
    if city100 in str(data.address):
        Datas100.append(data.address)
        Datas100.append(data.name)
        Datas100.append(data.telephone)
        a100 = '\n'.join(Datas100)
city101 = str("대전광역시 대덕구")
for data in carDataList:
    if city101 in str(data.address):
        Datas101.append(data.address)
        Datas101.append(data.name)
        Datas101.append(data.telephone)
        a101 = '\n'.join(Datas101)

city102 = str("경상북도 포항시")
for data in carDataList:
    if city102 in str(data.address):
        Datas102.append(data.address)
        Datas102.append(data.name)
        Datas102.append(data.telephone)
        a102 = '\n'.join(Datas102)

city103 = str("경상북도 칠곡군")
for data in carDataList:
    if city103 in str(data.address):
        Datas103.append(data.address)
        Datas103.append(data.name)
        Datas103.append(data.telephone)
        a103 = '\n'.join(Datas103)

city104 = str("경상북도 경산시")
for data in carDataList:
    if city104 in str(data.address):
        Datas104.append(data.address)
        Datas104.append(data.name)
        Datas104.append(data.telephone)
        a104 = '\n'.join(Datas104)

city105 = str("경상북도 봉화군")
for data in carDataList:
    if city105 in str(data.address):
        Datas105.append(data.address)
        Datas105.append(data.name)
        Datas105.append(data.telephone)
        a105 = '\n'.join(Datas105)

city106 = str("경상북도 경주시")
for data in carDataList:
    if city106 in str(data.address):
        Datas106.append(data.address)
        Datas106.append(data.name)
        Datas106.append(data.telephone)
        a106 = '\n'.join(Datas106)

city107 = str("경상북도 의성군")
for data in carDataList:
    if city107 in str(data.address):
        Datas107.append(data.address)
        Datas107.append(data.name)
        Datas107.append(data.telephone)
        a107 = '\n'.join(Datas107)

city108 = str("경상북도 울진군")
for data in carDataList:
    if city108 in str(data.address):
        Datas108.append(data.address)
        Datas108.append(data.name)
        Datas108.append(data.telephone)
        a108 = '\n'.join(Datas108)

city109 = str("경상북도 청도군")
for data in carDataList:
    if city109 in str(data.address):
        Datas109.append(data.address)
        Datas109.append(data.name)
        Datas109.append(data.telephone)
        a109 = '\n'.join(Datas109)

city110 = str("경상북도 예천군")
for data in carDataList:
    if city110 in str(data.address):
        Datas110.append(data.address)
        Datas110.append(data.name)
        Datas110.append(data.telephone)
        a110 = '\n'.join(Datas110)

city111 = str("경상북도 문경시")
for data in carDataList:
    if city111 in str(data.address):
        Datas111.append(data.address)
        Datas111.append(data.name)
        Datas111.append(data.telephone)
        a111 = '\n'.join(Datas111)

city112 = str("경상북도 영천시")
for data in carDataList:
    if city112 in str(data.address):
        Datas112.append(data.address)
        Datas112.append(data.name)
        Datas112.append(data.telephone)
        a112 = '\n'.join(Datas112)

city113 = str("경상북도 구미시")
for data in carDataList:
    if city113 in str(data.address):
        Datas113.append(data.address)
        Datas113.append(data.name)
        Datas113.append(data.telephone)
        a113 = '\n'.join(Datas113)

city114 = str("경상북도 상주시")
for data in carDataList:
    if city114 in str(data.address):
        Datas114.append(data.address)
        Datas114.append(data.name)
        Datas114.append(data.telephone)
        a114 = '\n'.join(Datas114)

city115 = str("경상북도 안동시")
for data in carDataList:
    if city115 in str(data.address):
        Datas115.append(data.address)
        Datas115.append(data.name)
        Datas115.append(data.telephone)
        a115 = '\n'.join(Datas115)

city116 = str("경상북도 영주시")
for data in carDataList:
    if city116 in str(data.address):
        Datas116.append(data.address)
        Datas116.append(data.name)
        Datas116.append(data.telephone)
        a116 = '\n'.join(Datas116)

city117 = str("경상북도 울릉군")
for data in carDataList:
    if city117 in str(data.address):
        Datas117.append(data.address)
        Datas117.append(data.name)
        Datas117.append(data.telephone)
        a117 = '\n'.join(Datas117)

city118 = str("경상북도 포항시 남구")
for data in carDataList:
    if city118 in str(data.address):
        Datas118.append(data.address)
        Datas118.append(data.name)
        Datas118.append(data.telephone)
        a118 = '\n'.join(Datas118)

city119 = str("경상북도 포항시 북구")
for data in carDataList:
    if city119 in str(data.address):
        Datas119.append(data.address)
        Datas119.append(data.name)
        Datas119.append(data.telephone)
        a119 = '\n'.join(Datas119)

city120 = str("경상북도 상주시")
for data in carDataList:
    if city120 in str(data.address):
        Datas120.append(data.address)
        Datas120.append(data.name)
        Datas120.append(data.telephone)
        a120 = '\n'.join(Datas120)

city121 = str("경상북도 김천시")
for data in carDataList:
    if city121 in str(data.address):
        Datas121.append(data.address)
        Datas121.append(data.name)
        Datas121.append(data.telephone)
        a121 = '\n'.join(Datas121)

city122 = str("경상북도 영덕군")
for data in carDataList:
    if city122 in str(data.address):
        Datas122.append(data.address)
        Datas122.append(data.name)
        Datas122.append(data.telephone)
        a122 = '\n'.join(Datas122)

city123 = str("전라북도 순창군")
for data in carDataList:
    if city123 in str(data.address):
        Datas123.append(data.address)
        Datas123.append(data.name)
        Datas123.append(data.telephone)
        a123 = '\n'.join(Datas123)

city124 = str("전라북도 남원시")
for data in carDataList:
    if city124 in str(data.address):
        Datas124.append(data.address)
        Datas124.append(data.name)
        Datas124.append(data.telephone)
        a124 = '\n'.join(Datas124)

city125 = str("전라북도 정읍시")
for data in carDataList:
    if city125 in str(data.address):
        Datas125.append(data.address)
        Datas125.append(data.name)
        Datas125.append(data.telephone)
        a125 = '\n'.join(Datas125)

city126 = str("전라북도 전주시")
for data in carDataList:
    if city126 in str(data.address):
        Datas126.append(data.address)
        Datas126.append(data.name)
        Datas126.append(data.telephone)
        a126 = '\n'.join(Datas126)

city127 = str("전라북도 부안군")
for data in carDataList:
    if city127 in str(data.address):
        Datas127.append(data.address)
        Datas127.append(data.name)
        Datas127.append(data.telephone)
        a127 = '\n'.join(Datas127)

city128 = str("전라북도 군산시")
for data in carDataList:
    if city128 in str(data.address):
        Datas128.append(data.address)
        Datas128.append(data.name)
        Datas128.append(data.telephone)
        a128 = '\n'.join(Datas128)

city129 = str("전라북도 전주시")
for data in carDataList:
    if city129 in str(data.address):
        Datas129.append(data.address)
        Datas129.append(data.name)
        Datas129.append(data.telephone)
        a129 = '\n'.join(Datas129)

city130 = str("전라북도 김제시")
for data in carDataList:
    if city130 in str(data.address):
        Datas130.append(data.address)
        Datas130.append(data.name)
        Datas130.append(data.telephone)
        a130 = '\n'.join(Datas130)

city131 = str("전라북도 완주군")
for data in carDataList:
    if city131 in str(data.address):
        Datas131.append(data.address)
        Datas131.append(data.name)
        Datas131.append(data.telephone)
        a131 = '\n'.join(Datas131)

city132 = str("전라북도 고창군")
for data in carDataList:
    if city132 in str(data.address):
        Datas132.append(data.address)
        Datas132.append(data.name)
        Datas132.append(data.telephone)
        a132 = '\n'.join(Datas132)

city133 = str("대구광역시 서구")
for data in carDataList:
    if city133 in str(data.address):
        Datas133.append(data.address)
        Datas133.append(data.name)
        Datas133.append(data.telephone)
        a133 = '\n'.join(Datas133)

city134 = str("대구광역시 북구")
for data in carDataList:
    if city134 in str(data.address):
        Datas134.append(data.address)
        Datas134.append(data.name)
        Datas134.append(data.telephone)
        a134 = '\n'.join(Datas134)

city135 = str("대구광역시 동구")
for data in carDataList:
    if city135 in str(data.address):
        Datas135.append(data.address)
        Datas135.append(data.name)
        Datas135.append(data.telephone)
        a135 = '\n'.join(Datas135)

city136 = str("대구광역시 중구")
for data in carDataList:
    if city136 in str(data.address):
        Datas136.append(data.address)
        Datas136.append(data.name)
        Datas136.append(data.telephone)
        a136 = '\n'.join(Datas136)

city137 = str("대구광역시 수성구")
for data in carDataList:
    if city137 in str(data.address):
        Datas137.append(data.address)
        Datas137.append(data.name)
        Datas137.append(data.telephone)
        a137 = '\n'.join(Datas137)

city138 = str("대구광역시 달서구")
for data in carDataList:
    if city138 in str(data.address):
        Datas138.append(data.address)
        Datas138.append(data.name)
        Datas138.append(data.telephone)
        a138 = '\n'.join(Datas138)

city139 = str("대구광역시 달성군")
for data in carDataList:
    if city139 in str(data.address):
        Datas139.append(data.address)
        Datas139.append(data.name)
        Datas139.append(data.telephone)
        a139 = '\n'.join(Datas139)

city140 = str("광주광역시 동구")
for data in carDataList:
    if city140 in str(data.address):
        Datas140.append(data.address)
        Datas140.append(data.name)
        Datas140.append(data.telephone)
        a140 = '\n'.join(Datas140)

city141 = str("광주광역시 서구")
for data in carDataList:
    if city141 in str(data.address):
        Datas141.append(data.address)
        Datas141.append(data.name)
        Datas141.append(data.telephone)
        a141 = '\n'.join(Datas141)

city142 = str("광주광역시 북구")
for data in carDataList:
    if city142 in str(data.address):
        Datas142.append(data.address)
        Datas142.append(data.name)
        Datas142.append(data.telephone)
        a142 = '\n'.join(Datas142)

city143 = str("광주광역시 광산구")
for data in carDataList:
    if city143 in str(data.address):
        Datas143.append(data.address)
        Datas143.append(data.name)
        Datas143.append(data.telephone)
        a143 = '\n'.join(Datas143)

city144 = str("전라남도 순천시")
for data in carDataList:
    if city144 in str(data.address):
        Datas144.append(data.address)
        Datas144.append(data.name)
        Datas144.append(data.telephone)
        a144 = '\n'.join(Datas144)

city145 = str("전라남도 영암군")
for data in carDataList:
    if city145 in str(data.address):
        Datas145.append(data.address)
        Datas145.append(data.name)
        Datas145.append(data.telephone)
        a145 = '\n'.join(Datas145)

city146 = str("전라남도 장흥군")
for data in carDataList:
    if city146 in str(data.address):
        Datas146.append(data.address)
        Datas146.append(data.name)
        Datas146.append(data.telephone)
        a146 = '\n'.join(Datas146)

city147 = str("전라남도 나주시")
for data in carDataList:
    if city147 in str(data.address):
        Datas147.append(data.address)
        Datas147.append(data.name)
        Datas147.append(data.telephone)
        a147 = '\n'.join(Datas147)

city148 = str("전라남도 구례군")
for data in carDataList:
    if city148 in str(data.address):
        Datas148.append(data.address)
        Datas148.append(data.name)
        Datas148.append(data.telephone)
        a148 = '\n'.join(Datas148)

city149 = str("전라남도 고흥군")
for data in carDataList:
    if city149 in str(data.address):
        Datas149.append(data.address)
        Datas149.append(data.name)
        Datas149.append(data.telephone)
        a149 = '\n'.join(Datas149)

city150 = str("전라남도 장성군")
for data in carDataList:
    if city150 in str(data.address):
        Datas150.append(data.address)
        Datas150.append(data.name)
        Datas150.append(data.telephone)
        a150 = '\n'.join(Datas150)

city151 = str("전라남도 진도군")
for data in carDataList:
    if city151 in str(data.address):
        Datas151.append(data.address)
        Datas151.append(data.name)
        Datas151.append(data.telephone)
        a151 = '\n'.join(Datas151)

city152 = str("전라남도 곡성군")
for data in carDataList:
    if city152 in str(data.address):
        Datas152.append(data.address)
        Datas152.append(data.name)
        Datas152.append(data.telephone)
        a152 = '\n'.join(Datas152)

city153 = str("전라남도 여수시")
for data in carDataList:
    if city153 in str(data.address):
        Datas153.append(data.address)
        Datas153.append(data.name)
        Datas153.append(data.telephone)
        a153 = '\n'.join(Datas153)

city154 = str("전라남도 구례군")
for data in carDataList:
    if city154 in str(data.address):
        Datas154.append(data.address)
        Datas154.append(data.name)
        Datas154.append(data.telephone)
        a154 = '\n'.join(Datas154)

city155 = str("전라남도 목포시")
for data in carDataList:
    if city155 in str(data.address):
        Datas155.append(data.address)
        Datas155.append(data.name)
        Datas155.append(data.telephone)
        a155 = '\n'.join(Datas155)

city156 = str("전라남도 여수시")
for data in carDataList:
    if city156 in str(data.address):
        Datas156.append(data.address)
        Datas156.append(data.name)
        Datas156.append(data.telephone)
        a156 = '\n'.join(Datas156)

city157 = str("전라남도 무안군")
for data in carDataList:
    if city157 in str(data.address):
        Datas157.append(data.address)
        Datas157.append(data.name)
        Datas157.append(data.telephone)
        a157 = '\n'.join(Datas157)

city158 = str("전라남도 완도군")
for data in carDataList:
    if city158 in str(data.address):
        Datas158.append(data.address)
        Datas158.append(data.name)
        Datas158.append(data.telephone)
        a158 = '\n'.join(Datas158)

city159 = str("전라남도 영광군")
for data in carDataList:
    if city159 in str(data.address):
        Datas159.append(data.address)
        Datas159.append(data.name)
        Datas159.append(data.telephone)
        a159 = '\n'.join(Datas159)

city160 = str("전라남도 해남군")
for data in carDataList:
    if city160 in str(data.address):
        Datas160.append(data.address)
        Datas160.append(data.name)
        Datas160.append(data.telephone)
        a160 = '\n'.join(Datas160)

city161 = str("전라남도 신안군")
for data in carDataList:
    if city161 in str(data.address):
        Datas161.append(data.address)
        Datas161.append(data.name)
        Datas161.append(data.telephone)
        a161 = '\n'.join(Datas161)

city162 = str("전라남도 함평군")
for data in carDataList:
    if city162 in str(data.address):
        Datas162.append(data.address)
        Datas162.append(data.name)
        Datas162.append(data.telephone)
        a162 = '\n'.join(Datas162)

city163 = str("전라남도 광양시")
for data in carDataList:
    if city163 in str(data.address):
        Datas163.append(data.address)
        Datas163.append(data.name)
        Datas163.append(data.telephone)
        a163 = '\n'.join(Datas163)

city164 = str("전라남도 담양군")
for data in carDataList:
    if city164 in str(data.address):
        Datas164.append(data.address)
        Datas164.append(data.name)
        Datas164.append(data.telephone)
        a164 = '\n'.join(Datas164)

city165 = str("경상남도 창원시")
for data in carDataList:
    if city165 in str(data.address):
        Datas165.append(data.address)
        Datas165.append(data.name)
        Datas165.append(data.telephone)
        a165 = '\n'.join(Datas165)

city166 = str("경상남도 밀양시")
for data in carDataList:
    if city166 in str(data.address):
        Datas166.append(data.address)
        Datas166.append(data.name)
        Datas166.append(data.telephone)
        a166 = '\n'.join(Datas166)

city167 = str("경상남도 창원시")
for data in carDataList:
    if city167 in str(data.address):
        Datas167.append(data.address)
        Datas167.append(data.name)
        Datas167.append(data.telephone)
        a167 = '\n'.join(Datas167)

city168 = str("경상남도 고성군")
for data in carDataList:
    if city168 in str(data.address):
        Datas168.append(data.address)
        Datas168.append(data.name)
        Datas168.append(data.telephone)
        a168 = '\n'.join(Datas168)

city169 = str("경상남도 거제시")
for data in carDataList:
    if city169 in str(data.address):
        Datas169.append(data.address)
        Datas169.append(data.name)
        Datas169.append(data.telephone)
        a169 = '\n'.join(Datas169)

city170 = str("경상남도 남해군")
for data in carDataList:
    if city170 in str(data.address):
        Datas170.append(data.address)
        Datas170.append(data.name)
        Datas170.append(data.telephone)
        a170 = '\n'.join(Datas170)

city171 = str("경상남도 진주시")
for data in carDataList:
    if city171 in str(data.address):
        Datas171.append(data.address)
        Datas171.append(data.name)
        Datas171.append(data.telephone)
        a171 = '\n'.join(Datas171)

city172 = str("경상남도 사천시")
for data in carDataList:
    if city172 in str(data.address):
        Datas172.append(data.address)
        Datas172.append(data.name)
        Datas172.append(data.telephone)
        a172 = '\n'.join(Datas172)

city173 = str("경상남도 거창군")
for data in carDataList:
    if city173 in str(data.address):
        Datas173.append(data.address)
        Datas173.append(data.name)
        Datas173.append(data.telephone)
        a173 = '\n'.join(Datas173)

city174 = str("경상남도 김해시")
for data in carDataList:
    if city174 in str(data.address):
        Datas174.append(data.address)
        Datas174.append(data.name)
        Datas174.append(data.telephone)
        a174 = '\n'.join(Datas174)

city175 = str("경상남도 통영시")
for data in carDataList:
    if city175 in str(data.address):
        Datas175.append(data.address)
        Datas175.append(data.name)
        Datas175.append(data.telephone)
        a175 = '\n'.join(Datas175)

city176 = str("경상남도 함양군")
for data in carDataList:
    if city176 in str(data.address):
        Datas176.append(data.address)
        Datas176.append(data.name)
        Datas176.append(data.telephone)
        a176 = '\n'.join(Datas176)

city177 = str("울산광역시 남구")
for data in carDataList:
    if city177 in str(data.address):
        Datas177.append(data.address)
        Datas177.append(data.name)
        Datas177.append(data.telephone)
        a177 = '\n'.join(Datas177)

city178 = str("울산광역시 중구")
for data in carDataList:
    if city178 in str(data.address):
        Datas178.append(data.address)
        Datas178.append(data.name)
        Datas178.append(data.telephone)
        a178 = '\n'.join(Datas178)

city179 = str("울산광역시 북구")
for data in carDataList:
    if city179 in str(data.address):
        Datas179.append(data.address)
        Datas179.append(data.name)
        Datas179.append(data.telephone)
        a179 = '\n'.join(Datas179)

city180 = str("울산광역시 동구")
for data in carDataList:
    if city180 in str(data.address):
        Datas180.append(data.address)
        Datas180.append(data.name)
        Datas180.append(data.telephone)
        a180 = '\n'.join(Datas180)

city181 = str("울산광역시 울주군")
for data in carDataList:
    if city181 in str(data.address):
        Datas181.append(data.address)
        Datas181.append(data.name)
        Datas181.append(data.telephone)
        a181 = '\n'.join(Datas181)

city182 = str("부산광역시 수영구")
for data in carDataList:
    if city182 in str(data.address):
        Datas182.append(data.address)
        Datas182.append(data.name)
        Datas182.append(data.telephone)
        a182 = '\n'.join(Datas181)

city183 = str("부산광역시 사상구")
for data in carDataList:
    if city183 in str(data.address):
        Datas183.append(data.address)
        Datas183.append(data.name)
        Datas183.append(data.telephone)
        a183 = '\n'.join(Datas183)

city184 = str("부산광역시 사하구")
for data in carDataList:
    if city184 in str(data.address):
        Datas184.append(data.address)
        Datas184.append(data.name)
        Datas184.append(data.telephone)
        a184 = '\n'.join(Datas184)

city185 = str("부산광역시 부산진구")
for data in carDataList:
    if city185 in str(data.address):
        Datas185.append(data.address)
        Datas185.append(data.name)
        Datas185.append(data.telephone)
        a185 = '\n'.join(Datas185)

city186 = str("부산광역시 동래구")
for data in carDataList:
    if city186 in str(data.address):
        Datas186.append(data.address)
        Datas186.append(data.name)
        Datas186.append(data.telephone)
        a186 = '\n'.join(Datas186)

city187 = str("부산광역시 남구")
for data in carDataList:
    if city187 in str(data.address):
        Datas187.append(data.address)
        Datas187.append(data.name)
        Datas187.append(data.telephone)
        a187 = '\n'.join(Datas187)

city188 = str("부산광역시 영도군")
for data in carDataList:
    if city188 in str(data.address):
        Datas188.append(data.address)
        Datas188.append(data.name)
        Datas188.append(data.telephone)
        a188 = '\n'.join(Datas188)

city189 = str("부산광역시 강서구")
for data in carDataList:
    if city189 in str(data.address):
        Datas189.append(data.address)
        Datas189.append(data.name)
        Datas189.append(data.telephone)
        a189 = '\n'.join(Datas189)

city190 = str("부산광역시 해운대구")
for data in carDataList:
    if city190 in str(data.address):
        Datas190.append(data.address)
        Datas190.append(data.name)
        Datas190.append(data.telephone)
        a190 = '\n'.join(Datas190)

city191 = str("부산광역시 수영구")
for data in carDataList:
    if city191 in str(data.address):
        Datas191.append(data.address)
        Datas191.append(data.name)
        Datas191.append(data.telephone)
        a191 = '\n'.join(Datas191)

city192 = str("부산광역시 동구")
for data in carDataList:
    if city192 in str(data.address):
        Datas192.append(data.address)
        Datas192.append(data.name)
        Datas192.append(data.telephone)
        a192 = '\n'.join(Datas192)

city193 = str("부산광역시 연제구")
for data in carDataList:
    if city193 in str(data.address):
        Datas193.append(data.address)
        Datas193.append(data.name)
        Datas193.append(data.telephone)
        a193 = '\n'.join(Datas193)

city194 = str("부산광역시 강서구")
for data in carDataList:
    if city194 in str(data.address):
        Datas194.append(data.address)
        Datas194.append(data.name)
        Datas194.append(data.telephone)
        a194 = '\n'.join(Datas194)

city195 = str("부산광역시 북구")
for data in carDataList:
    if city195 in str(data.address):
        Datas195.append(data.address)
        Datas195.append(data.name)
        Datas195.append(data.telephone)
        a195 = '\n'.join(Datas195)

city196 = str("부산광역시 부산진구")
for data in carDataList:
    if city196 in str(data.address):
        Datas196.append(data.address)
        Datas196.append(data.name)
        Datas196.append(data.telephone)
        a196 = '\n'.join(Datas196)

city197 = str("부산광역시 연제구")
for data in carDataList:
    if city197 in str(data.address):
        Datas197.append(data.address)
        Datas197.append(data.name)
        Datas197.append(data.telephone)
        a197 = '\n'.join(Datas197)

city198 = str("부산광역시 금정구")
for data in carDataList:
    if city198 in str(data.address):
        Datas198.append(data.address)
        Datas198.append(data.name)
        Datas198.append(data.telephone)
        a198 = '\n'.join(Datas198)

# city199 = str("제주특별자치도")
# for data in carDataList:
#     if city199 in str(data.address):
#         Datas199.append(data.address)
#         Datas200.append(data.name)
#         a199 = '\n'.join(Datas199)
#
# city200 = str("제주시")
# for data in carDataList:
#     if city200 in str(data.address):
#         Datas200.append(data.address)
#         Datas200.append(data.name)
#         a200 = '\n'.join(Datas200)


import telepot

token = '1227254368:AAGZuYMCa9uS2zzQy6Aqn3hrOQo4oLk8MIo'
id = '1061918307'

bot = telepot.Bot(token)

updates = bot.getUpdates()

def inform():
    bot.sendMessage(chat_id=id, text="전국에 있는 렌터카 업체의 정보를 알려드립니다.\n 원하는 지역의 시,군,구를 입력하세요!")
    bot.sendMessage(chat_id=id, text="ex) 경기도 수원시, 서울특별시 강남구,전라남도 여수시 ...")

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)  # 입력받은 메세지에 대한 정보들을 각각 저장.
    #print('Chat Message:', content_type, chat_type, chat_id) # 메세지에 대한 정보들을 console 창에 print
    if content_type == 'text':
        if msg['text'] == '인천광역시 미추홀구':
            bot.sendMessage(chat_id=id, text=a1)  # 메시지를 보냅니다.
        if msg['text'] == '인천광역시 서구':
            bot.sendMessage(chat_id=id, text=a2)
        if msg['text'] == '인천광역시 남동구':
            bot.sendMessage(chat_id=id, text=a3)  # 메시지를 보냅니다.
        if msg['text'] == '인천광역시 연수구':
            bot.sendMessage(chat_id=id, text=a4)
        if msg['text'] == '인천광역시 계양구':
            bot.sendMessage(chat_id=id, text=a5)  # 메시지를 보냅니다.
        if msg['text'] == '인천광역시 부평구':
            bot.sendMessage(chat_id=id, text=a6)
        if msg['text'] == '인천광역시 중구':
            bot.sendMessage(chat_id=id, text=a7)  # 메시지를 보냅니다.
        if msg['text'] == '인천광역시 동구':
            bot.sendMessage(chat_id=id, text=a8)
        if msg['text'] == '인천광역시 옹진군':
            bot.sendMessage(chat_id=id, text=a9)  # 메시지를 보냅니다.
        if msg['text'] == '인천광역시 부평구':
            bot.sendMessage(chat_id=id, text=a10)
        if msg['text'] == '서울특별시 중구':
            bot.sendMessage(chat_id=id, text=a11)  # 메시지를 보냅니다.
        if msg['text'] == '서울특별시 서대문구':
            bot.sendMessage(chat_id=id, text=a12)
        if msg['text'] == '서울특별시 노원구':
            bot.sendMessage(chat_id=id, text=a13)  # 메시지를 보냅니다.
        if msg['text'] == '서울특별시 서초구':
            bot.sendMessage(chat_id=id, text=a14)  # 메시지를 보냅니다.
        if msg['text'] == '서울특별시 강북구':
            bot.sendMessage(chat_id=id, text=a15)
        if msg['text'] == '서울특별시 송파구':
            bot.sendMessage(chat_id=id, text=a16)  # 메시지를 보냅니다.
        if msg['text'] == '서울특별시 중랑구':
            bot.sendMessage(chat_id=id, text=a17)  # 메시지를 보냅니다.
        if msg['text'] == '서울특별시 광진구':
            bot.sendMessage(chat_id=id, text=a18)
        if msg['text'] == '서울특별시 강남구':
            bot.sendMessage(chat_id=id, text=a19)  # 메시지를 보냅니다.
        if msg['text'] == '서울특별시 관악구':
            bot.sendMessage(chat_id=id, text=a20)  # 메시지를 보냅니다.
        if msg['text'] == '서울특별시 은평구':
            bot.sendMessage(chat_id=id, text=a21)
        if msg['text'] == '서울특별시 구로구':
            bot.sendMessage(chat_id=id, text=a22)  # 메시지를 보냅니다.
        if msg['text'] == '서울특별시 영등포구':
            bot.sendMessage(chat_id=id, text=a23)  # 메시지를 보냅니다.
        if msg['text'] == '서울특별시 양천구':
            bot.sendMessage(chat_id=id, text=a24)
        if msg['text'] == '서울특별시 강동구':
            bot.sendMessage(chat_id=id, text=a25)  # 메시지를 보냅니다.
        if msg['text'] == '서울특별시 도봉구':
            bot.sendMessage(chat_id=id, text=a26)  # 메시지를 보냅니다.
        if msg['text'] == '서울특별시 강서구':
            bot.sendMessage(chat_id=id, text=a27)
        if msg['text'] == '서울특별시 동대문구':
            bot.sendMessage(chat_id=id, text=a28)  # 메시지를 보냅니다.
        if msg['text'] == '서울특별시 금천구':
            bot.sendMessage(chat_id=id, text=a29)  # 메시지를 보냅니다.
        if msg['text'] == '서울특별시 성동구':
            bot.sendMessage(chat_id=id, text=a30)
        if msg['text'] == '서울특별시 종로구':
            bot.sendMessage(chat_id=id, text=a31)  # 메시지를 보냅니다.
        if msg['text'] == '서울특별시 성북구':
            bot.sendMessage(chat_id=id, text=a32)  # 메시지를 보냅니다.
        if msg['text'] == '서울특별시 용산구':
            bot.sendMessage(chat_id=id, text=a33)
        if msg['text'] == '서울특별시 동대문구':
            bot.sendMessage(chat_id=id, text=a34)  # 메시지를 보냅니다.
        if msg['text'] == '서울특별시 마포구':
            bot.sendMessage(chat_id=id, text=a35)  # 메시지를 보냅니다.
        if msg['text'] == '강원도 태백시':
            bot.sendMessage(chat_id=id, text=a36)  # 메시지를 보냅니다.
        if msg['text'] == '강원도 강릉시':
            bot.sendMessage(chat_id=id, text=a37)  # 메시지를 보냅니다.
        if msg['text'] == '강원도 동해시':
            bot.sendMessage(chat_id=id, text=a38)  # 메시지를 보냅니다.
        if msg['text'] == '강원도 홍천군':
            bot.sendMessage(chat_id=id, text=a39)  # 메시지를 보냅니다.
        if msg['text'] == '강원도 강릉시':
            bot.sendMessage(chat_id=id, text=a40)  # 메시지를 보냅니다.
        if msg['text'] == '강원도 춘천시':
            bot.sendMessage(chat_id=id, text=a41)  # 메시지를 보냅니다.
        if msg['text'] == '강원도 평창군':
            bot.sendMessage(chat_id=id, text=a42)  # 메시지를 보냅니다.
        if msg['text'] == '강원도 원주시':
            bot.sendMessage(chat_id=id, text=a43)  # 메시지를 보냅니다.
        if msg['text'] == '강원도 인제군':
            bot.sendMessage(chat_id=id, text=a44)  # 메시지를 보냅니다.
        if msg['text'] == '강원도 횡성군':
            bot.sendMessage(chat_id=id, text=a45)  # 메시지를 보냅니다.
        if msg['text'] == '강원도 영월군':
            bot.sendMessage(chat_id=id, text=a46)  # 메시지를 보냅니다.
        if msg['text'] == '강원도 속초시':
            bot.sendMessage(chat_id=id, text=a47)  # 메시지를 보냅니다.
        if msg['text'] == '강원도 철원군':
            bot.sendMessage(chat_id=id, text=a48)  # 메시지를 보냅니다.
        if msg['text'] == '강원도 양양군':
            bot.sendMessage(chat_id=id, text=a49)  # 메시지를 보냅니다.
        if msg['text'] == '강원도 양구군':
            bot.sendMessage(chat_id=id, text=a50)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 부천시':
            bot.sendMessage(chat_id=id, text=a51)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 하남시':
            bot.sendMessage(chat_id=id, text=a52)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 성남시':
            bot.sendMessage(chat_id=id, text=a53)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 수원시':
            bot.sendMessage(chat_id=id, text=a54)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 화성시':
            bot.sendMessage(chat_id=id, text=a55)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 군포시':
            bot.sendMessage(chat_id=id, text=a56)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 평택시':
            bot.sendMessage(chat_id=id, text=a57)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 김포시':
            bot.sendMessage(chat_id=id, text=a58)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 시흥시':
            bot.sendMessage(chat_id=id, text=a59)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 용인시':
            bot.sendMessage(chat_id=id, text=a61)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 양평군':
            bot.sendMessage(chat_id=id, text=a62)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 남양주시':
            bot.sendMessage(chat_id=id, text=a63)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 양주시':
            bot.sendMessage(chat_id=id, text=a64)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 고양시':
            bot.sendMessage(chat_id=id, text=a65)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 과천시':
            bot.sendMessage(chat_id=id, text=a66)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 이천시':
            bot.sendMessage(chat_id=id, text=a67)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 오산시':
            bot.sendMessage(chat_id=id, text=a68)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 광주시':
            bot.sendMessage(chat_id=id, text=a69)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 의왕시':
            bot.sendMessage(chat_id=id, text=a70)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 안산시':
            bot.sendMessage(chat_id=id, text=a71)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 구리시':
            bot.sendMessage(chat_id=id, text=a72)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 동두천시':
            bot.sendMessage(chat_id=id, text=a73)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 연천군':
            bot.sendMessage(chat_id=id, text=a74)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 파주시':
            bot.sendMessage(chat_id=id, text=a75)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 포천시':
            bot.sendMessage(chat_id=id, text=a76)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 안양시':
            bot.sendMessage(chat_id=id, text=a77)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 의정부시':
            bot.sendMessage(chat_id=id, text=a78)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 안성시':
            bot.sendMessage(chat_id=id, text=a79)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 여주시':
            bot.sendMessage(chat_id=id, text=a80)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 가평군':
            bot.sendMessage(chat_id=id, text=a81)  # 메시지를 보냅니다.
        if msg['text'] == '경기도 광명시':
            bot.sendMessage(chat_id=id, text=a82)  # 메시지를 보냅니다.
        if msg['text'] == '충청북도 청주시':
            bot.sendMessage(chat_id=id, text=a83)  # 메시지를 보냅니다.
        if msg['text'] == '충청북도 진천군':
            bot.sendMessage(chat_id=id, text=a84)  # 메시지를 보냅니다.
        if msg['text'] == '충청북도 괴산군':
            bot.sendMessage(chat_id=id, text=a85)  # 메시지를 보냅니다.
        if msg['text'] == '충청북도 충주시':
            bot.sendMessage(chat_id=id, text=a86)  # 메시지를 보냅니다.
        if msg['text'] == '충청북도 제천시':
            bot.sendMessage(chat_id=id, text=a87)  # 메시지를 보냅니다.
        if msg['text'] == '충청북도 충주시':
            bot.sendMessage(chat_id=id, text=a88)  # 메시지를 보냅니다.
        if msg['text'] == '충청북도 단양군':
            bot.sendMessage(chat_id=id, text=a89)  # 메시지를 보냅니다.
        if msg['text'] == '충청남도 천안시':
            bot.sendMessage(chat_id=id, text=a90)  # 메시지를 보냅니다.
        if msg['text'] == '충청남도 서산시':
            bot.sendMessage(chat_id=id, text=a91)  # 메시지를 보냅니다.
        if msg['text'] == '충청남도 홍성군':
            bot.sendMessage(chat_id=id, text=a92)  # 메시지를 보냅니다.
        if msg['text'] == '충청남도 보령시':
            bot.sendMessage(chat_id=id, text=a93)  # 메시지를 보냅니다.
        if msg['text'] == '충청남도 논산시':
            bot.sendMessage(chat_id=id, text=a94)  # 메시지를 보냅니다.
        if msg['text'] == '충청남도 공주시':
            bot.sendMessage(chat_id=id, text=a95)  # 메시지를 보냅니다.
        if msg['text'] == '충청남도 청양군':
            bot.sendMessage(chat_id=id, text=a96)  # 메시지를 보냅니다.
        if msg['text'] == '대전광역시 유성구':
            bot.sendMessage(chat_id=id, text=a97)  # 메시지를 보냅니다.
        if msg['text'] == '대전광역시 서구':
            bot.sendMessage(chat_id=id, text=a98)  # 메시지를 보냅니다.
        if msg['text'] == '대전광역시 중구':
            bot.sendMessage(chat_id=id, text=a99)  # 메시지를 보냅니다.
        if msg['text'] == '대전광역시 동구':
            bot.sendMessage(chat_id=id, text=a100)  # 메시지를 보냅니다.
        if msg['text'] == '대전광역시 대덕구':
            bot.sendMessage(chat_id=id, text=a101)  # 메시지를 보냅니다.
        if msg['text'] == '경상북도 포항시':
            bot.sendMessage(chat_id=id, text=a102)  # 메시지를 보냅니다.
        if msg['text'] == '경상북도 칠곡군':
            bot.sendMessage(chat_id=id, text=a103)  # 메시지를 보냅니다.
        if msg['text'] == '경상북도 경상시':
            bot.sendMessage(chat_id=id, text=a104)  # 메시지를 보냅니다.
        if msg['text'] == '경상북도 봉화군':
            bot.sendMessage(chat_id=id, text=a105)  # 메시지를 보냅니다.
        if msg['text'] == '경상북도 경주시':
            bot.sendMessage(chat_id=id, text=a106)  # 메시지를 보냅니다.
        if msg['text'] == '경상북도 의성군':
            bot.sendMessage(chat_id=id, text=a107)  # 메시지를 보냅니다.
        if msg['text'] == '경상북도 울진군':
            bot.sendMessage(chat_id=id, text=a108)  # 메시지를 보냅니다.
        if msg['text'] == '경상북도 청도군':
            bot.sendMessage(chat_id=id, text=a109)  # 메시지를 보냅니다.
        if msg['text'] == '경상북도 예천군':
            bot.sendMessage(chat_id=id, text=a110)  # 메시지를 보냅니다.
        if msg['text'] == '경상북도 문경시':
            bot.sendMessage(chat_id=id, text=a111)  # 메시지를 보냅니다.
        if msg['text'] == '경상북도 영천시':
            bot.sendMessage(chat_id=id, text=a112)  # 메시지를 보냅니다.
        if msg['text'] == '경상북도 구미시':
            bot.sendMessage(chat_id=id, text=a113)  # 메시지를 보냅니다.
        if msg['text'] == '경상북도 상주시':
            bot.sendMessage(chat_id=id, text=a114)  # 메시지를 보냅니다.
        if msg['text'] == '경상북도 안동시':
            bot.sendMessage(chat_id=id, text=a115)  # 메시지를 보냅니다.
        if msg['text'] == '경상북도 영주시':
            bot.sendMessage(chat_id=id, text=a116)  # 메시지를 보냅니다.
        if msg['text'] == '경상북도 울릉군':
            bot.sendMessage(chat_id=id, text=a117)  # 메시지를 보냅니다.
        if msg['text'] == '경상북도 포항시 남구':
            bot.sendMessage(chat_id=id, text=a118)  # 메시지를 보냅니다.
        if msg['text'] == '경상북도 포항시 북구':
            bot.sendMessage(chat_id=id, text=a119)  # 메시지를 보냅니다.
        # if msg['text'] == '경상북도 상주시':
        #     bot.sendMessage(chat_id=id, text=a120)  # 메시지를 보냅니다.
        if msg['text'] == '경상북도 김천시':
            bot.sendMessage(chat_id=id, text=a121)  # 메시지를 보냅니다.
        if msg['text'] == '경상북도 영덕군':
            bot.sendMessage(chat_id=id, text=a122)  # 메시지를 보냅니다.
        if msg['text'] == '전라북도 순창군':
            bot.sendMessage(chat_id=id, text=a123)  # 메시지를 보냅니다.
        if msg['text'] == '전라북도 남원시':
            bot.sendMessage(chat_id=id, text=a124)  # 메시지를 보냅니다.
        if msg['text'] == '전라북도 정읍시':
            bot.sendMessage(chat_id=id, text=a125)  # 메시지를 보냅니다.
        if msg['text'] == '전라북도 전주시':
            bot.sendMessage(chat_id=id, text=a126)  # 메시지를 보냅니다.
        if msg['text'] == '전라북도 부안군':
            bot.sendMessage(chat_id=id, text=a127)  # 메시지를 보냅니다.
        if msg['text'] == '전라북도 군산시':
            bot.sendMessage(chat_id=id, text=a128)  # 메시지를 보냅니다.
        if msg['text'] == '전라북도 전주시':
            bot.sendMessage(chat_id=id, text=a129)  # 메시지를 보냅니다.
        if msg['text'] == '전라북도 김제시':
            bot.sendMessage(chat_id=id, text=a130)  # 메시지를 보냅니다.
        if msg['text'] == '전라북도 완주군':
            bot.sendMessage(chat_id=id, text=a131)  # 메시지를 보냅니다.
        if msg['text'] == '전라북도 고창군':
            bot.sendMessage(chat_id=id, text=a132)  # 메시지를 보냅니다.
        if msg['text'] == '대구광역시 서구':
            bot.sendMessage(chat_id=id, text=a133)  # 메시지를 보냅니다.
        if msg['text'] == '대구광역시 북구':
            bot.sendMessage(chat_id=id, text=a134)  # 메시지를 보냅니다.
        if msg['text'] == '대구광역시 동구':
            bot.sendMessage(chat_id=id, text=a135)  # 메시지를 보냅니다.
        if msg['text'] == '대구광역시 중구':
            bot.sendMessage(chat_id=id, text=a136)  # 메시지를 보냅니다.
        if msg['text'] == '대구광역시 수성구':
            bot.sendMessage(chat_id=id, text=a137)  # 메시지를 보냅니다.
        if msg['text'] == '대구광역시 달서구':
            bot.sendMessage(chat_id=id, text=a138)  # 메시지를 보냅니다.
        if msg['text'] == '대구광역시 달성군':
            bot.sendMessage(chat_id=id, text=a139)  # 메시지를 보냅니다.
        if msg['text'] == '광주광역시 동구':
            bot.sendMessage(chat_id=id, text=a140)  # 메시지를 보냅니다.
        if msg['text'] == '광주광역시 서구':
            bot.sendMessage(chat_id=id, text=a141)  # 메시지를 보냅니다.
        if msg['text'] == '광주광역시 북구':
            bot.sendMessage(chat_id=id, text=a142)  # 메시지를 보냅니다.
        if msg['text'] == '광주광역시 광산구':
            bot.sendMessage(chat_id=id, text=a143)  # 메시지를 보냅니다.
        if msg['text'] == '전라남도 순천시':
            bot.sendMessage(chat_id=id, text=a144)  # 메시지를 보냅니다.
        if msg['text'] == '전라남도 영암군':
            bot.sendMessage(chat_id=id, text=a145)  # 메시지를 보냅니다.
        if msg['text'] == '전라남도 장흥군':
            bot.sendMessage(chat_id=id, text=a146)  # 메시지를 보냅니다.
        if msg['text'] == '전라남도 나주시':
            bot.sendMessage(chat_id=id, text=a147)  # 메시지를 보냅니다.
        if msg['text'] == '전라남도 구례군':
            bot.sendMessage(chat_id=id, text=a148)  # 메시지를 보냅니다.
        if msg['text'] == '전라남도 고흥군':
            bot.sendMessage(chat_id=id, text=a149)  # 메시지를 보냅니다.
        if msg['text'] == '전라남도 장성군':
            bot.sendMessage(chat_id=id, text=a150)  # 메시지를 보냅니다.
        if msg['text'] == '전라남도 진도군':
            bot.sendMessage(chat_id=id, text=a151)  # 메시지를 보냅니다.
        if msg['text'] == '전라남도 곡성군':
            bot.sendMessage(chat_id=id, text=a152)  # 메시지를 보냅니다.
        if msg['text'] == '전라남도 여수시':
            bot.sendMessage(chat_id=id, text=a153)  # 메시지를 보냅니다.
        # if msg['text'] == '전라남도 구례군':
        #     bot.sendMessage(chat_id=id, text=a154)  # 메시지를 보냅니다.
        if msg['text'] == '전라남도 목포시':
            bot.sendMessage(chat_id=id, text=a155)  # 메시지를 보냅니다.
        # if msg['text'] == '전라남도 여수시':
        #     bot.sendMessage(chat_id=id, text=a156)  # 메시지를 보냅니다.
        if msg['text'] == '전라남도 무안군':
            bot.sendMessage(chat_id=id, text=a157)  # 메시지를 보냅니다.
        if msg['text'] == '전라남도 완도군':
            bot.sendMessage(chat_id=id, text=a158)  # 메시지를 보냅니다.
        if msg['text'] == '전라남도 영광군':
            bot.sendMessage(chat_id=id, text=a159)  # 메시지를 보냅니다.
        if msg['text'] == '전라남도 해남군':
            bot.sendMessage(chat_id=id, text=a160)  # 메시지를 보냅니다.
        if msg['text'] == '전라남도 신안군':
            bot.sendMessage(chat_id=id, text=a161)  # 메시지를 보냅니다.
        if msg['text'] == '전라남도 함평군':
            bot.sendMessage(chat_id=id, text=a162)  # 메시지를 보냅니다.
        if msg['text'] == '전라남도 광양시':
            bot.sendMessage(chat_id=id, text=a163)  # 메시지를 보냅니다.
        if msg['text'] == '전라남도 담양군':
            bot.sendMessage(chat_id=id, text=a164)  # 메시지를 보냅니다.
        if msg['text'] == '경상남도 창원시':
            bot.sendMessage(chat_id=id, text=a165)  # 메시지를 보냅니다.
        if msg['text'] == '경상남도 밀양시':
            bot.sendMessage(chat_id=id, text=a166)  # 메시지를 보냅니다.
        # if msg['text'] == '경상남도 창원시':
        #     bot.sendMessage(chat_id=id, text=a167)  # 메시지를 보냅니다.
        if msg['text'] == '경상남도 고성군':
            bot.sendMessage(chat_id=id, text=a168)  # 메시지를 보냅니다.
        if msg['text'] == '경상남도 거제시':
            bot.sendMessage(chat_id=id, text=a169)  # 메시지를 보냅니다.
        if msg['text'] == '경상남도 남해군':
            bot.sendMessage(chat_id=id, text=a170)  # 메시지를 보냅니다.
        if msg['text'] == '경상남도 진주시':
            bot.sendMessage(chat_id=id, text=a171)  # 메시지를 보냅니다.
        if msg['text'] == '경상남도 사천시':
            bot.sendMessage(chat_id=id, text=a172)  # 메시지를 보냅니다.
        if msg['text'] == '경상남도 거창군':
            bot.sendMessage(chat_id=id, text=a173)  # 메시지를 보냅니다.
        if msg['text'] == '경상남도 김해시':
            bot.sendMessage(chat_id=id, text=a174)  # 메시지를 보냅니다.
        if msg['text'] == '경상남도 통영시':
            bot.sendMessage(chat_id=id, text=a175)  # 메시지를 보냅니다.
        if msg['text'] == '경상남도 함양군':
            bot.sendMessage(chat_id=id, text=a176)  # 메시지를 보냅니다.
        if msg['text'] == '울산광역시 남구':
            bot.sendMessage(chat_id=id, text=a177)  # 메시지를 보냅니다.
        if msg['text'] == '울산광역시 중구':
            bot.sendMessage(chat_id=id, text=a178)  # 메시지를 보냅니다.
        if msg['text'] == '울산광역시 북구':
            bot.sendMessage(chat_id=id, text=a179)  # 메시지를 보냅니다.
        if msg['text'] == '울산광역시 동구':
            bot.sendMessage(chat_id=id, text=a180)  # 메시지를 보냅니다.
        if msg['text'] == '울산광역시 울주군':
            bot.sendMessage(chat_id=id, text=a181)  # 메시지를 보냅니다.
        if msg['text'] == '부산광역시 수영구':
            bot.sendMessage(chat_id=id, text=a182)  # 메시지를 보냅니다.
        if msg['text'] == '부산광역시 사상구':
            bot.sendMessage(chat_id=id, text=a183)  # 메시지를 보냅니다.
        if msg['text'] == '부산광역시 사하구':
            bot.sendMessage(chat_id=id, text=a184)  # 메시지를 보냅니다.
        if msg['text'] == '부산광역시 부산진구':
            bot.sendMessage(chat_id=id, text=a185)  # 메시지를 보냅니다.
        if msg['text'] == '부산광역시 동래구':
            bot.sendMessage(chat_id=id, text=a186)  # 메시지를 보냅니다.
        if msg['text'] == '부산광역시 남구':
            bot.sendMessage(chat_id=id, text=a187)  # 메시지를 보냅니다.
        if msg['text'] == '부산광역시 영도군':
            bot.sendMessage(chat_id=id, text=a188)  # 메시지를 보냅니다.
        if msg['text'] == '부산광역시 강서구':
            bot.sendMessage(chat_id=id, text=a189)  # 메시지를 보냅니다.
        if msg['text'] == '부산광역시 해운대구':
            bot.sendMessage(chat_id=id, text=a190)  # 메시지를 보냅니다.
        # if msg['text'] == '부산광역시 수영구':
        #     bot.sendMessage(chat_id=id, text=a191)  # 메시지를 보냅니다.
        if msg['text'] == '부산광역시 동구':
            bot.sendMessage(chat_id=id, text=a192)  # 메시지를 보냅니다.
        if msg['text'] == '부산광역시 연제구':
            bot.sendMessage(chat_id=id, text=a193)  # 메시지를 보냅니다.
        # if msg['text'] == '부산광역시 강서구':
        #     bot.sendMessage(chat_id=id, text=a194)  # 메시지를 보냅니다.
        if msg['text'] == '부산광역시 북구':
            bot.sendMessage(chat_id=id, text=a195)  # 메시지를 보냅니다.
        # if msg['text'] == '부산광역시 부산진구':
        #     bot.sendMessage(chat_id=id, text=a196)  # 메시지를 보냅니다.
        if msg['text'] == '부산광역시 연제구':
            bot.sendMessage(chat_id=id, text=a197)  # 메시지를 보냅니다.
        if msg['text'] == '부산광역시 금정구':
            bot.sendMessage(chat_id=id, text=a198)  # 메시지를 보냅니다.
        # if msg['text'] == '제주도':
        #     bot.sendMessage(chat_id=id, text=a199)  # 메시지를 보냅니다.
        # if msg['text'] == '제주시':
        #     bot.sendMessage(chat_id=id, text=a200)  # 메시지를 보냅니다.



    inform()

bot.message_loop({'chat': on_chat_message}, run_forever=True)
