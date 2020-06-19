from bs4 import BeautifulSoup
import requests as rq
from urllib.request import urlopen
import re
import csv

with open('movies.csv','r',encoding='utf-8') as movies:
    reader = csv.reader(movies)
    for row in reader:
        
        movie_name =str(row[1])
        movie_name_final = movie_name.replace(' ','+')
        url1 = f'https://www.imdb.com/find?q={movie_name_final}&ref_=nv_sr_sm'
        try:
            html1 = urlopen(url1)
            soup1 = BeautifulSoup(html1,"html.parser")
            x = soup1.findAll('td',{'class':'result_text'})
            url2 = 'https://www.imdb.com' + str(x[0]).split('>')[1].split('"')[1] + '?ref_=fn_al_tt_1'
            html2 = urlopen(url2)
            soup2 = BeautifulSoup(html2,"html.parser")
            y = soup2.findAll('div',{'class':'poster'})
            final_url = str(str(y).split('src')[1].split('"')[1].split('"')[0])
        except:
            final_url = 'no Url'
        with open('demo1.csv', 'a', newline='',encoding='utf-8') as d:
            writer = csv.writer(d)
            writer.writerows([[final_url]])
