import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import  cosine_similarity
movies=pd.read_csv("lmovie.csv")
ratings=pd.read_csv('lrating.csv')
M=ratings.pivot_table(index=['userId'],columns=['movieId'],values='rating')

M=M.fillna(0)
def standardize(row):
    new_row=(row-row.mean())/(row.max()-row.min())
    return new_row
M_std=M.apply(standardize)
#print(M_std)
item_similarity=cosine_similarity(M_std.T)
#print(item_similarity)
item_similarity_df = pd.DataFrame(item_similarity,index=M.columns,columns=M.columns)
#print(item_similarity_df)
def get_similar_movies(movieId,user_rating):
    similar_score =item_similarity_df[movieId]*user_rating
    similar_score=similar_score.sort_values(ascending=False)
    return similar_score
P = get_similar_movies(13,4)
print(P[:15])





