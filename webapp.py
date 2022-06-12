
import numpy as np
import pandas as pd
import pickle
import cloudpickle
import streamlit as st
from PIL import Image

img=Image.open('logo.png')

# loading the saved model
loaded_model = cloudpickle.load(open('findsim.sav', 'rb'))


# creating a function for Prediction

def finalpred(input_data,seq):


    

    # changing the input_data to numpy array
    df = pd.read_pickle('df.pkl')
    # reshape the array as we are predicting for one instance
    titles=df['original_title']
    titles=titles.values.tolist()
    i=titles.index(input_data)

    prediction = loaded_model(df,i,del_sequels = seq, verbose = False)
    #print(prediction)

    return prediction
  
    
  
def main():
    
    st.set_page_config(page_title='What should I watch Next',page_icon=img)
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    with st.sidebar:
        image = Image.open('wswn.jpg')
        st.image(image)
        st.subheader('Type in the name of the movie you last watched and get 5 suggestions you might like!!')
        st.write('A popularity+content based recommender which suggests movies similar to the user’s favourite one using keywords of movies’ genre, era, plot, cast and more.')
        st.write("Notebook for creating Model: [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")
    # giving a title
    st.title('What should I watch Next?')
    st.markdown("<h5 style='text-align: right; color: red;'>Created by Charan K R</h1>", unsafe_allow_html=True)
    #st.subheader('-created by Charan K R')
    
    
    # getting the input data from the user
    
    
    Movie = st.text_input('Name of Movie')

    
    
    # code for Prediction
    pred = ''
    
    
    # creating a button for Prediction
    seq=False

    if st.checkbox('Dont Recommend Sequels'):
        seq=True

    if st.button('You might like...'):
        pred = finalpred(Movie,seq)
        moviepred=[]
        for i in range(len(pred)):
            moviepred.append(pred[i][0])
        for j in range(5):
            st.write(moviepred[j])

    
    #st.success(pred[0][0])
    
    
    
    
    
if __name__ == '__main__':
    main()