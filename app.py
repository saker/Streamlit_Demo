import streamlit as st
import pandas as pd

st.title('Getting Started Streamlit')
st.write('Test')

st.markdown('## My Markdown')

code = ""
run_btn = st.button('Run!')

if run_btn:
    st.markdown('Button has already clicked!')

cols = st.columns(2)

with cols[0]:
    age = st.number_input('Input your age')
    st.markdown(f'Your age is {age}')

with cols[1]:
    text_in = st.text_input('Input Text')
    word_tokenize = '|'.join(text_in.split())
    st.markdown(f'{word_tokenize}')


df = pd.DataFrame({
    'First': [1,2,3,4],
    'Second': [10,20,89,440]
})

st.dataframe(df)

st.line_chart(df, x='First', y='Second')