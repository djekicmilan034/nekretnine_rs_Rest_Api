import requests
from bs4 import BeautifulSoup
from baza import *

#Web Scraper
def algo(url):
    neks=[]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    lists = soup.find_all('div', class_="row offer")

    for list in lists:
        location = list.find('p', class_="offer-location").text.replace('\n', '').replace(" ",'')
        flex = list.find('p', class_="offer-price offer-price--invert").text.replace('\n', '').replace(" ",'')
        adresa = list.find('div', class_="offer-adress").text.replace('\n', '').replace(" ", '')
        cena=list.find('p', class_="offer-price").text.replace('\n', '').replace(" ", '')

        #Sredjivanje
        adresaFinal=adresa.split("|")
        lokacija= location.split(",")
        vrsta=adresaFinal[2]
        transakcija=adresaFinal[1]
        flex=flex[:-2]

        #Sredjivanje podataka o ceni nekretnina.
        if 'upit' in cena:
            cenaNek=0.0
        elif 'dogovoru' in cena:
            cenaNek=0
        elif 'Informacija' in cena:
            cenaNek=0
        else:
            index=cena.index('E')
            cenaNek=float(cena[:index])

        # Sredjivanje podataka o kvadraturi nekretnina.
        if '--- m²'==flex:
            flex=0.0
        else:
            flex


        # Sredjivanje podataka o lokaciji nekretnina.
        if len(lokacija)>2:
            naselje = lokacija[0]
            grad = lokacija[1]
        else:
            naselje=''
            grad=''

        oglas=[transakcija,vrsta,cenaNek,float(flex),grad,naselje]
        data = Oglas(transakcija=transakcija, vrsta=vrsta, cenaNek=cenaNek, kvadratura=flex,grad=grad, naselje=naselje)
        session.add(data) #Dodavanje nekretnine u bazu podataka.
        session.commit()
        neks.append(oglas)

    for nekretnina in neks:
        print(nekretnina) #Prikaz svake nekretnine koje je Web Scraper obradio.
    return neks



for i in range(1,51):
    print("------------------------------------------------------------------------------------")
    print("Strana:",i)
    algo("https://www.nekretnine.rs/stambeni-objekti/stanovi/izdavanje-prodaja/izdavanje/lista/po-stranici/10/stranica/{}/".format(i))
    print("------------------------------------------------------------------------------------")


#url = "https://www.nekretnine.rs/stambeni-objekti/stanovi/izdavanje-prodaja/izdavanje/lista/po-stranici/10/stranica/1/"
#algo(url)