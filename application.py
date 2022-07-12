import streamlit as st
import pickle
import pandas as pd


import requests


def recommend(movie):

  index = movies[movies['title'] == movie].index[0]
  similarity_vec = simi[index]
  m = sorted(list(enumerate(similarity_vec)) , reverse = True , key = lambda x:x[1])[1 : 6]

  recommended_movies = []
  for i in m:
    recommended_movies.append(movies['title'].iloc[i[0]])

  return recommended_movies

movie_list = pickle.load(open('movieslist.pkl','rb'))
movies = pd.DataFrame(movie_list)

simi = pickle.load(open('similarity_vector.pkl','rb'))



st.title('Amazon Prime Movie Recommender System')

selected_movie = st.selectbox(
     'How would you like to be contacted?',
     movies['title'].values)

if st.button('Recommend from Amazon Prime'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)
