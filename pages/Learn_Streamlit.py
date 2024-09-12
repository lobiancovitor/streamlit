import requests
import streamlit as st
import pandas as pd

if 'total' not in st.session_state:
    st.session_state.total=0
if st.button('+'):
    st.session_state.total+=1
st.write(st.session_state.total)

st.expander("expand")

note=st.text_input("Enter a note")
if note:
    with open("notes.txt", "a+") as file:
        file.write(f"{note}\n")

with open("notes.txt", "r+") as file:
        st.text(file.read())

col1, col2 = st.columns([2,2])
col1.text_input('Thinner Column')
col2.text_input('Thicker Column')
tab1, tab2 = st.tabs(['TAB 1','TAB 2'])
tab1.text_area('text in tab 1')
tab2.date_input('date in tab 2')
st.expander('Expander')
st.container()

placeholder = st.empty()
placeholder.text('Hide this placeholder container')
if st.button('Hide'): 
    placeholder.empty()
st.progress(35)
st.spinner('Spinner')
if st.checkbox('Balloons', False):
    st.balloons()
if st.checkbox('Snow', False):
    st.snow()
    
st.error('Error')
st.warning('Warning')
st.info('Info')
st.success('Success')
st.exception(RuntimeError('This is a fake error.'))

import numpy as np
df=pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)