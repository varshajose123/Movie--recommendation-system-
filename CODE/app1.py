#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 01:00:27 2024

@author: Varsha Mariya Jose
"""

#streamlit run "/Users/varshajose/Desktop/dsmlproject/app1.py"

import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
  movie_index=movies[movies['title']==movie].index[0]
  distances=similarity[movie_index]
  movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
  
  recommended_movies=[]

  for i in movies_list:
    recommended_movies.append(movies.iloc[i[0]].title)
  return recommended_movies  



movies_dict=pickle.load(open('/Users/varshajose/Desktop/dsmlproject/movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('/Users/varshajose/Desktop/dsmlproject/similarity.pkl','rb'))

st.title('Movie Recommendation System')
selected_movie_name=st.selectbox("How would you like to be contacted?", movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)