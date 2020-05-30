import pandas as pd
import numpy as nm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as cs

def get_title_from_index(index):
  return movies_file[movies_file.index == index]['title'].values[0]


def get_index_from_title(title):
  return movies_file[movies_file.title == title]['movieId'].values[0]

#change this to a variable later
movie_user_likes = "Toy Story (1995)"  


cv = CountVectorizer()
movies_file = pd.read_csv('movies.csv')
movies_file.set_index('movieId', drop = False)
maj_list = []
min_list = []
genre = movies_file['genres']
genre_list = list(genre)
genre_list_new = []
#modify the genre column by replacing
for i in genre_list:
  i = i.replace('|',' ')
  genre_list_new.append(i)

count_matrix = cv.fit_transform(genre_list_new)
count_matrix_array = count_matrix.toarray()
#limits##################################
init_movieval = 0
final_movieval = 1000 + 1
#######################################
#compare 2 at a time(to increase number of movies that can be used) , use the movie if cs_value > 0.8
#disrcard others 
for i in range(init_movieval,final_movieval):
  for j in range(init_movieval,final_movieval):
    similarity_scores = cs([count_matrix_array[i],count_matrix_array[j]])
    #discard unnecessary movies
    if similarity_scores[0][1] > 0.8:
      tu = (j,similarity_scores[0][1])
      min_list.append(tu)
  maj_list.append(min_list)
  min_list = []
#required movie index
movie_index = get_index_from_title(movie_user_likes)
#sort the required list in major list to get descending order of similar movies
sorted_similar_movie = sorted(maj_list[movie_index], key=lambda x:x[1], reverse=True)
for movies in sorted_similar_movie:
  print(get_title_from_index(movies[0]))

