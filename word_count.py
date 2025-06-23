import streamlit as st

st.title('Word Count App')
st.write('Made By: Siddhant Thombare ')

words = st.text_input('Enter sentence ')
length = len(words.split())

st.write('The Word Count :',length)
