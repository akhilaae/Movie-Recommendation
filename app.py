import streamlit as st
import pickle

movies=pickle.load(open("movies_list.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))
movies_list=movies["title"].values
st.header("Movie Recommender System")
select_val=st.selectbox("Select movie", movies_list)

def recommend(movie):
    index=movies[movies["title"]==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
    recommend_movie=[]
    for i in distance[1:6]:
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie

if st.button("Recommend"):
    recommendations=recommend(select_val)
    mov1,mov2=st.columns(2)
    with mov1:
        st.text(recommendations[0])
    with mov2:
        st.text(recommendations[1])
    mov3,mov4=st.columns(2)
    with mov3:
        st.text(recommendations[2])
    with mov4:
        st.text(recommendations[3])
    st.text(recommendations[4])
