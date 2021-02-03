from bs4 import BeautifulSoup
import requests


BUDGET = 15
ACCEPT_LANGUAGE = "en-US,en;q=0.9,it;q=0.8"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"


url = "https://www.amazon.es/SHOPLED-Control-opciones-Habitaci%C3%B3n-Dormitorio/dp/B08G4DFMNN/ref=sr_1_1_sspa?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=led+lights&qid=1612005206&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSzM4REkwMDJWSERBJmVuY3J5cHRlZElkPUEwNjY5MTIwM01USDdLM0JYWDFHWiZlbmNyeXB0ZWRBZElkPUEwMTU2OTgwMzJZNkNMMDA3WEtBVSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="


headers = {
    "Accept-Language": ACCEPT_LANGUAGE,
    "User-Agent": USER_AGENT
}


response = requests.get(url=url, headers=headers)
response.raise_for_status()
data = response.text


soup = BeautifulSoup(data, "html.parser")
price = float(soup.find(name="span", id="priceblock_ourprice").getText().split("\xa0")[0].replace(",", "."))

if price <= BUDGET:
    print("Send email....")