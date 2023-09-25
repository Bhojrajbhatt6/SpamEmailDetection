import streamlit as st
import pickle

with open('model.pickle','rb') as file:
    model = pickle.load(file)

email = st.text_input('Enter your email here: ')

if st.button('Classify: '):
    y_pred = model.predict([email])
    st.write(y_pred[0])