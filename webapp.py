
import numpy as np
import pandas as pd
import pickle
import cloudpickle
import streamlit as st


# loading the saved model
loaded_model = cloudpickle.load(open('findsim.sav', 'rb'))


# creating a function for Prediction

def finalpred(input_data):


    

    # changing the input_data to numpy array
    df = pd.read_pickle('df.pkl')
    # reshape the array as we are predicting for one instance
    titles=df['original_title']
    titles=titles.values.tolist()
    i=titles.index(input_data)

    prediction = loaded_model(df,i,del_sequels = True, verbose = True)
    #print(prediction)

    return prediction
  
    
  
def main():
    
    
    # giving a title
    st.title('What should I watch Next')
    
    
    # getting the input data from the user
    
    
    Movie = st.text_input('Name of Movie')

    
    
    # code for Prediction
    pred = ''
    
    
    # creating a button for Prediction
    
    if st.button('You might like...'):
        pred = finalpred(Movie)
        moviepred=[]
        for i in range(len(pred)):
            moviepred.append(pred[i][0])
        st.write(moviepred)
    
    #st.success(pred[0][0])
    
    
    
    
    
if __name__ == '__main__':
    main()