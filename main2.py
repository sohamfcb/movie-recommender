import pickle
import pandas as pd
import requests
from flask import Flask
import jsonify

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies


app=Flask(__name__)

@app.route('/')
def index():
    
    selected_movie_name='Fury'
    if selected_movie_name in movies['title'].values:
        response=recommend(selected_movie_name)

    response={
        'fulfillmentText':'{}, {}, {}, {}, {}'.format(recommend(selected_movie_name)[0],recommend(selected_movie_name)[0],recommend(selected_movie_name)[1],recommend(selected_movie_name)[2],recommend(selected_movie_name)[3],recommend(selected_movie_name)[4])
    }
    return jsonify(response)

if __name__=='__main__':

    movies_dict=pickle.load(open('movie_dict.pkl','rb'))
    movies=pd.DataFrame(movies_dict)

    similarity=pickle.load(open('similarity.pkl','rb'))
    app.run(debug=True)