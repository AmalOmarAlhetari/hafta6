import requests
from bs4 import BeautifulSoup
from collections import deque
import threading
import time

def abc (aurl):
    r=requests.get(aurl)
    soup=BeautifulSoup(r.content,'html.parser')
    list=soup.find_all("div",{"class":"f-cat f-item"})
    for i in list:
        print('====')
        #print(i)
        for b in i.findAll("ul",{"class":"list underline"}):
            #print(b)
            for link in b.findAll('a'):
                my_link=link.get('href')+"\n"
                print(my_link)
                newlink="www.milligazete.com.tr{}".format(my_link)
                #print(newlink)
               # print(my_link)
            with (open('dgdg.txt','a') as f):
                f.write(newlink)

listem= ['https://www.milligazete.com.tr/arsiv/2025-03-22','https://www.milligazete.com.tr/arsiv/2025-03-23','https://www.milligazete.com.tr/arsiv/2025-03-20','https://www.milligazete.com.tr/arsiv/2025-03-21']
for url in listem:
    abc(url)