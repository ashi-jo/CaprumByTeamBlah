import pandas as pd
import numpy as nm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as cs
import csv


def get_title_from_index(index):
  return movies_file[movies_file.index == index]['title'].values[0]


def get_index_from_title(title):
  return movies_file[movies_file.title == title]['movieId'].values[0]

movies_file = pd.read_csv('movies-wpu.csv', engine='python')
movie_user_likes = "Toy Story (1995)"#input('>  ')
req_row_list_1 = []
#filehandle = pd.read_csv('scores.csv', names=list(range(8719)),engine='python')
with open('scores.csv') as scores:
  movie_index = get_index_from_title(movie_user_likes)
  rows = csv.reader(scores)
  for row in enumerate(rows):
    if row[0] == movie_index:
      for i in row[1]:
        i = (float(i.split(',')[0].split('(')[1]),float(i.split(',')[1].split(')')[0]))
        req_row_list_1.append(i)
      #sort the required list in major list to get descending order of similar movies
      sorted_similar_movie = sorted(req_row_list_1, key=lambda x:x[1], reverse = True)

  #req_row = filehandle.iloc[movie_index - 1]

  #req_row_list = list(req_row.replace(nm.nan, ' ', regex=True))

  #req_row_list_1 = []
  #while ' ' in req_row_list:
  #  req_row_list.remove(req_row_list[-1])
  #print(req_row_list)
  


for movies in sorted_similar_movie:
  print(get_title_from_index(movies[0]))



