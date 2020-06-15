import ClassCar
import folium

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

for data in carDataList:
    print(str(data.homepage))

# for i in root.findall('records'):
#     for j in i.findall('record'):
#         name = j.find('사업장구분').text
#         print(name)
#
# for i in root.findall('records'):
#     for j in i.findall('record'):
#         name = j.find('소재지도로명주소').text
#         print(name)
#
# for i in root.findall('records'):
#     for j in i.findall('record'):
#         name = j.find('소재지지번주소').text
#         print(name)
#
# for i in root.findall('records'):
#     for j in i.findall('record'):
#         name = j.find('위도').text
#         print(name)
#
# for i in root.findall('records'):
#     for j in i.findall('record'):
#         name = j.find('경도').text
#         print(name)
#
# for i in root.findall('records'):
#     for j in i.findall('record'):
#         name = j.find('차고지도로명주소').text
#         print(name)
#
# for i in root.findall('records'):
#     for j in i.findall('record'):
#         name = j.find('차고지지번주소').text
#         print(name)
#
# for i in root.findall('records'):
#     for j in i.findall('record'):
#         name = j.find('보유차고지수용능력').text
#         print(name)
#
# for i in root.findall('records'):
#     for j in i.findall('record'):
#         name = j.find('자동차총보유대수').text
#         print(name)
#
# for i in root.findall('records'):
#     for j in i.findall('record'):
#         name = j.find('승용차보유대수').text
#         print(name)
# for i in root.findall('records'):
#     for j in i.findall('record'):
#         name = j.find('승합차보유대수').text
#         print(name)