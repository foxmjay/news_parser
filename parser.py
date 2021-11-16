# -*- coding: utf-8 -*-
from __future__ import print_function
import requests
from bs4 import BeautifulSoup


def hespress_parser():
    url = 'http://hespress.com'
    rslt = requests.get(url).text
    html_text = rslt.encode('utf-8')

    #html_text=""
    #with open('tmp.html','r') as f:
    #    html_text=f.read()

    soup = BeautifulSoup(html_text,'html.parser')
    div = soup.find("ul",{"class": "h24"})
    aas = div.find_all('a')
    data=[]
    for aa in aas:
        title = aa.find('h3').text.encode('utf-8')
        href = aa.get('href').encode('utf-8')
        data.append({'title':title,'href':href})
    return data

#for hh in hespress_parser():
#    print(hh['title'],hh['href'])
