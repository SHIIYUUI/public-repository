import streamlit as st
st.subheader("画像の表示")
checked = st.checkbox("チェックして画像を表示")
if checked==True:
 st.image("https://upload.wikimedia.org/wikipedia/commons/d/d6/ニホンリス.jpg",
 caption="ニホンリス", use_column_width=True)