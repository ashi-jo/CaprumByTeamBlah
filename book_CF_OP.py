import pandas as pd
movies=pd.read_csv("books.csv")
K=pd.read_csv('OP_books.csv')
print(K)
df_list=K.values.tolist()
print(df_list)
a=8109
ldf=(K.loc[(K['book_id']==a)])
mi_list=ldf.values.tolist()
print(mi_list)
for item in mi_list:
   pilist=item
for item in pilist:
    ldf=((movies.loc[(movies['book_id']==item)])['title'])
    ldf.to_csv('booktemp.csv', mode='a', header=False)
odf=pd.read_csv('booktemp.csv')
#odf.columns=['srno','moviename']
clist=odf.values.tolist()
print(clist)



