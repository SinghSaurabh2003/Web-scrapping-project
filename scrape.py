import requests
import pandas as pd
from bs4 import BeautifulSoup
url="https://www.worldometers.info/coronavirus/country/india/"
r=requests.get(url)
j=r.content
soup=BeautifulSoup(j,'html.parser')
print(soup.prettify())
case=soup.find_all('div',class_='maincounter-number')
print(case)
list=[]
for i in case:
    span=i.find('span')
    list.append(span.string)
print(list)
df=pd.DataFrame({"coronavirus": list})
df.index=['total cases','death','recovered']
df.to_csv('corona_virus.csv')



