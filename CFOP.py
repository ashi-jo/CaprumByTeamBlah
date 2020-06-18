import pandas as pd
movies=pd.read_csv("movies.csv")
K=pd.read_csv('opdata.csv')
#print(K)
df_list=K.values.tolist()
#print(df_list)
a=input('enter movie id')
a=int(a)
ldf=(K.loc[(K['movie']==a)])
mi_list=ldf.values.tolist()
#print(mi_list)
for item in mi_list:
   pilist=item
for item in pilist:
    ldf=((movies.loc[(movies['movieId']==item)])['title'])
    ldf.to_csv('lol.csv', mode='a', header=False)
odf=pd.read_csv('lol.csv')
odf.columns=['srno','moviename']
clist=odf.values.tolist()
print(clist)

