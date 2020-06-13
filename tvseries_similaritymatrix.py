import pandas as pd
import numpy as nm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as cs
import csv

with open('scorestv.csv','a',newline='') as fp:

  a = csv.writer(fp, delimiter=',')

  def get_title_from_index(index):
    return movies_file[movies_file.index == index]['title'].values[0]


  def get_index_from_title(title):
    return movies_file[movies_file.title == title]['show_id'].values[0]

  #change this to a variable later
  movie_user_likes = "We Bare Bears"


  cv = CountVectorizer()
  movies_file = pd.read_csv('netflix_titles.csv')
  movies_file.set_index('show_id', drop = False)
  maj_list = []
  min_list = []
  genre = movies_file['listed_in']
  genre_list = list(genre)
  genre_list_new = []
  #modify the genre column by replacing
  for i in genre_list:
    i = i.replace(',',' ')
    genre_list_new.append(i)

  count_matrix = cv.fit_transform(genre_list_new)
  count_matrix_array = count_matrix.toarray()
  #limits##################################
  init_movieval = 0
  final_movieval = 1960+ 1
  #######################################
  #compare 2 at a time(to increase number of movies that can be used) , use the movie if cs_value > 0.8
  #disrcard others
  for i in range(1,1960):
    for j in range(init_movieval,final_movieval):
      similarity_scores = cs([count_matrix_array[i],count_matrix_array[j]])
      #discard unnecessary movies
      #print(similarity_scores)
      if similarity_scores[0][1] > 0.82:
        tu = (j,similarity_scores[0][1])
        min_list.append(tu)
    maj_list.append(min_list)
    min_list = []
  a.writerows(maj_list)