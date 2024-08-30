import streamlit as st
st.set_page_config(layout ="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("images/meenal.jpg", width= 300)
with col2:
    st.title("Meenal T H")
    content = """"
    Hi I am Meenal T H, an Engineer with programming experience and Founder of Mindspick Digital. 
    I graduated in 2006 from University of Mumbai and have more than 5 Years of Experience in Data Science. 
    Before Data Engineering, I was a part of Design and Digital Marketing for a few organizations in the UAE.  """""
    st.info(content)
