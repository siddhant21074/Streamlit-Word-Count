import streamlit as st

st.title('Word Count App')

words = st.text_input('Enter sentence ')
length = len(words.split())

st.write('The Word Count :',length)