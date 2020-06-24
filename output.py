import pandas as pd
import numpy as nm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as cs
import csv

def get_title_from_index(index,mf):
  return mf[mf.index == index]['title'].values[0]


def get_index_from_title(title,mf):
  return mf[mf.title == title]['movieId'].values[0]


def get_genre_from_title(title,mf):
  return mf[mf.title == title]['genres'].values[0]


def get_imageurl_from_title(title,mf):
  return mf[mf.title == title]['imageUrl'].values[0]


def get_plot_from_title(title,mf):
  return mf[mf.title == title]['plot'].values[0]



def output(name):
  
  movies_file = pd.read_csv('movies-wpu.csv', engine='python')
  index = get_index_from_title(name,movies_file)
  #movie_user_likes = "Jumanji (1995)"#input('>  ')
  req_row_list_1 = []
  movie_index = int(index) - 1
  with open('scores.csv') as scores:
    #movie_index = get_index_from_title(movie_user_likes)
    rows = csv.reader(scores)
    for row in enumerate(rows):
      if row[0] == movie_index:
        for i in row[1]:
          i = (float(i.split(',')[0].split('(')[1]),float(i.split(',')[1].split(')')[0]))
          req_row_list_1.append(i)
        #sort the required list in major list to get descending order of similar movies
        sorted_similar_movie = sorted(req_row_list_1, key=lambda x:x[1], reverse = True)
  final_list=[]  
  counter = 0
  for movies in sorted_similar_movie:
    counter += 1
    movie_name = get_title_from_index(movies[0],movies_file)
    if counter > 15:
      return final_list
    f_list = {"name":movie_name, "genre":get_genre_from_title(movie_name,movies_file),"imageurl":get_imageurl_from_title(movie_name,movies_file),"plot":get_plot_from_title(movie_name,movies_file)}
    final_list.append(f_list) 



