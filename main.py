import streamlit as st
import  pandas
st.set_page_config(layout ="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("images/meenal.jpg", width= 550, )
with col2:
    st.title("Meenal T H")
    content = """   
Hi I am Meenal T H, an Engineer with programming experience and Founder of Mindspick Digital. 
I graduated in 2006 from University of Mumbai and have more than 5 Years of Experience in Data Science. 
Before Data Science, I was a part of Design, Digital Marketing and Data Analytics for a few 
organizations in the UAE.
    """

    content1 = """
    Digital marketing and data analytics are two closely related fields that work together to drive effective marketing strategies. 
    
    Here's a summary of how they complement each other:
    
    Data analytics is a critical component of modern digital marketing. 
    Analytics provides valuable insights into customer behavior, campaign performance, 
    and marketing ROI. These insights help marketers make informed decisions about targeting, 
    messaging, and optimization of digital marketing efforts. 
    
    Data analytics can help digital marketers understand their audience better, identify trends and
    patterns, and measure the effectiveness of their campaigns.
    By leveraging data, marketers can optimize their digital campaigns for better engagement,
    conversion, and return on investment.  
    """

    st.info(content)
    st.write(content1)

content2 ="""
Please have a look at the information about some of the apps that I have built. 
"""

st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

