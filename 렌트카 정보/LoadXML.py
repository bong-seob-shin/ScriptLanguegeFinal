from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse
from urllib.parse import unquote
def LoadXmlData():
    Date = None
    saveName = "전국렌터카.xml"
    url = "http://api.data.go.kr/openapi/tn_pubr_public_car_rental_api"
    key = "KbscxuSrKaJv3eDHa0LY6t5pT9rBDWfdZMs74YbaI5uHHJz2ifYzhe5wwm2qy8RxFLPEsJGvgc1MokHNFz943g%3D%3D"
    API_key = unquote(key)
    url = url + "ServiceKey=" + API_key + "&type=xml&pageNo=1&numOfRows=10&flag=Y"
    data = urllib.request.urlopen(url).read()
    text = data.decode('utf-8')

    req.urlretrieve(url, saveName)

    xml = open(saveName, "r", encoding="utf-8").read()
    Data = BeautifulSoup(xml, "html.parser")

    return Data

xmldata = LoadXmlData()

print(xmldata)