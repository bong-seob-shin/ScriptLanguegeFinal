from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse

def LoadData():
    # Date = None
    # saveName = "ss.xml"
    # url = "http://api.data.go.kr/openapi/tn_pubr_public_car_rental_api?"
    # key = "{ quote_plus('ServiceKey') : KbscxuSrKaJv3eDHa0LY6t5pT9rBDWfdZMs74YbaI5uHHJz2ifYzhe5wwm2qy8RxFLPEsJGvgc1MokHNFz943g%3D%3D"
    # url = url + "ServiceKey=" + key #+ "&type=xml&pageNo=1&numOfRows=10&flag=Y"
    # data = urllib.request.urlopen(url).read()
    # text = data.decode('utf-8')
    #
    # req.urlretrieve(url, saveName)

    xml = open("Car.xml", "r", encoding="cp-949").read()
    Data = BeautifulSoup(xml, "html.parser")
    return Data
