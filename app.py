import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse= True, key = lambda x:x[1])[1:6]
    recommend_movies = []

    for i in movie_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

option = st.selectbox("Choose a movie:", movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)
print("prachi")        
