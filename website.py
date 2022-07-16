import streamlit as st
import pickle
import pandas as pd


def recommend(Headline):
    Headline_index = news[news['Headline'] == Headline].index[0]
    distances = cosine_sim_mat[Headline_index]
    Headlines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_Headlines = []
    for i in Headlines_list:
        recommended_Headlines.append(news.iloc[i[0]].Headline)
    return recommended_Headlines

news_dict = pickle.load(open('news_dict.pkl', 'rb'))
news = pd.DataFrame(news_dict)

cosine_sim_mat = pickle.load(open('cosine_sim_mat.pkl', 'rb'))


st.title('Recommender System')

selected_headline_name = st.selectbox(
'Recommended News Headlines:',
news['Headline'].values)

if st.button('Recommend'):
     recommendations = recommend(selected_headline_name)
     for i in recommendations:
         st.write(i)
