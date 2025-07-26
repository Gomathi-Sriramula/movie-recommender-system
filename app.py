import os
import pickle
import pandas as pd
import streamlit as st
import urllib.request

similarity_path = "similarity.pkl"
if not os.path.exists(similarity_path):
    print("Downloading similarity.pkl from Google Drive...")
    url = "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_HERE"
    urllib.request.urlretrieve(url, similarity_path)
st.title('Movie Recommender System 🎬')

similarity = pickle.load(open(similarity_path, 'rb'))

import pickle
movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)



selected_movie_name= st.selectbox(
    "How would you like to be contacted?",
    (movies['title'].values),
)
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=5cbfe7d6ff1e0833d689bf62b1c49693'.format(movie_id))
    data=response.json()
    #st.text(data)
    #st.text('https://api.themoviedb.org/3/movie/{}?api_key=5cbfe7d6ff1e0833d689bf62b1c49693'.format(movie_id))
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]


    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        #fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster


#similarity=pickle.load(open('similarity.pkl','rb'))

if st.button("Recommend"):
    names,posters=recommend(selected_movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])



