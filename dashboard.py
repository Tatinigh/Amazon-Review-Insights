import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import plotly.express as px

st.markdown("""
<style>
 .heading{
            
    font-family: Verdana;
    font-weight: bold;
    font-size: 2rem!important;
    color:  #6DA5C0!important;
    text-align: justify;
   
}

.kpicard{
   font-family:sans-serif;
   font-size:1.5rem!important;
   color:#0F969C!important;
   text-align:left;
}
.wordcloudp{
   font-family:sans-serif;
   font-size:1.5rem!important;
   color:#0F969C!important;
   text-align:left;
}
.pie{
   font-family:sans-serif;
   font-size:1.5rem!important;
   color:#0F969C!important;
   text-align:left;
}
.bar{
   font-family:sans-serif;
   font-size:1.5rem!important;
   color:#0F969C!important;
   text-align:left;
}
.impact{
   font-family:sans-serif;
   font-size:1.5rem!important;
   color:#0F969C!important;
   text-align:left;
}
.overview{
   font-family:sans-serif;
   font-size:1.5rem!important;
   color:#0F969C!important;
   text-align:left;
}
</style>
""",unsafe_allow_html=True)
st.markdown("<h1 class='heading'>Amazon Reviews : Sentiment Analysis</h1>",unsafe_allow_html=True)
st.markdown("<h2 class='kpicard'>KPI Cards</h2>",unsafe_allow_html=True)
df=pd.read_csv(r"D:\python\amazon reviews\Amazon Review Data Web Scrapping - Amazon Review Data Web Scrapping.csv")
col1,col2,col3,col4=st.columns(4)
total_reviews=len(df)
with col1:
    st.metric("Total Reviews", f"{total_reviews:,}")
positive_reviews=(len(df[df['Own_Rating']=='Positive'])/total_reviews)*100
with col2:
    st.metric("Positive Sentiment",f"{positive_reviews:.1f}%")
neutral_reviews=(len(df[df['Own_Rating']=='Neutral'])/total_reviews)*100
with col3:
    st.metric("Neutral Sentiment",f"{neutral_reviews:.1f}%")
negative_reviews=(len(df[df['Own_Rating']=='Negative'])/total_reviews)*100
with col4:
    st.metric("Negative Sentiment",f"{negative_reviews:.1f}%")
st.divider()
st.markdown("<h2 class='wordcloudp'>Most Frequently Used Words</h2>",unsafe_allow_html=True)
all_words=''.join(df['Review_text'].fillna("")).lower()
wordcloud=WordCloud(width=1200, height=300, background_color='black', colormap='Pastel2',relative_scaling=0.5 ).generate(all_words)
fig_wc,ax=plt.subplots(figsize=(14.8,3))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig_wc)
st.divider()
col1,col2=st.columns(2)
with col1:
    st.markdown("<h2 class='pie'>Sentiment Distribution</h2>",unsafe_allow_html=True)
    count = df['Own_Rating'].value_counts()
    count.index = count.index.str.strip()
    fig_pie=px.pie(values=count.values,
                   names=count.index,
                   color_discrete_map={'Positive':"#064248",'Neutral':"#A37A6D",'Negative':"#43080F"},
                   hole=0.4)
    st.plotly_chart(fig_pie)
with col2:
    st.markdown("<h2 class='bar'>Rating Distribution</h2>",unsafe_allow_html=True)
    count1=df['Rating'].value_counts().sort_index()
    fig_bar=px.bar(x=count1.index,
                   y=count1.values,
                   labels={'x':'Rating','y':'Count'},
                   color_discrete_sequence=["#138994"])
    st.plotly_chart(fig_bar)
st.divider()
st.markdown("<h2 class='impact'>Review Length Impact</h2>",unsafe_allow_html=True)
df['review_length']=df['Review_text'].str.len()
df['bin']=pd.cut(df['review_length'],bins=[0,100,150,200,250,300,350,500],
                 labels=['50', '100', '150', '200', '250', '300','350+'])
length_sentiment=df.groupby(['bin','Own_Rating']).size().unstack(fill_value=0)
fig_rev=px.bar(length_sentiment,
               labels={'value':'Review Count','bin':'Words'},
               color_discrete_map={'Positive':"#064248",'Neutral':"#A37A6D",'Negative':"#43080F"}
              )     
st.plotly_chart(fig_rev)
st.divider()
st.markdown("<h2 class='overview'>Summary Statistics</h2>",unsafe_allow_html=True)
col1,col2,col3=st.columns(3)
with col1:
    avg=df['review_length'].mean()
    st.metric("Average Review Length",f"{avg:.0f} words")
with col2:
    most=df['Rating'].mode()[0]
    st.metric("Most Common Rating",f"{most}★")
with col3:
    pol=(positive_reviews-(100-positive_reviews-neutral_reviews))/100
    st.metric("Sentiment Polarity",f"{pol:.2f}")