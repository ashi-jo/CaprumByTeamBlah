import pandas as pd
import sqlite3
movies = pd.read_csv("netflix_titles.csv")
con=sqlite3.connect('TVscores22.sqlite')
c=con.cursor()
c.execute("SELECT * FROM TVscores1")
data=c.fetchall()
#print(data)
a=15
meow=[]
for row in data:
     l=list(row)
     m=l[0]
     m=int(m)
     if m==a:
        mi_list=l[1:]
        print(mi_list)
        break
for item in mi_list:
         q = (int(item.split(',')[0].split('(')[1]))
         # print(q)
         ldf = (movies.loc[(movies['TV_id'] == q)])
         # print(ldf)
         mdict = ldf.to_dict()

         meow.append(mdict)
print(meow)