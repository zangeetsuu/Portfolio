import requests as re
import bs4 as bs
import html5lib as html
import webbrowser
phrase = input("Co chcesz kupic?")
url='https://www.olx.pl/oferty/q-'+phrase+'/'
r = re.get(url)
offers = []
soup= bs.BeautifulSoup(r.content,'html.parser')
def strToInt(x):
    for i in x:
        if i.isdecimal() == False:
            x=x.replace(i,"")
    return x
for offer in soup.find_all('div', class_='css-1r93q13'):
        price = offer.find('p', class_='css-uj7mm0').get_text().strip()
        price = strToInt(price)
        price=int(price)
        offers.append(price)

offers.sort()
links=[]
for i in range(3):

    for offer in soup.find_all('div', class_='css-1r93q13'):
        price = offer.find('p', class_='css-uj7mm0').get_text().strip()
        price = strToInt(price)
        if price==str(offers[i]):
            link=offer.find_all('a')
            for y in link:
                links.append(y['href'])
links=set(links)
links=(list(links))
for i in links:
    webbrowser.open('https://www.olx.pl'+ i)




#zrobic do tego interfejs graficzny





