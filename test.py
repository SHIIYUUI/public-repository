import streamlit as st

st.title("Streamlit のテスト")

st.radio("１つ選んでください", ("電車", "バス", "徒歩"))

checked = st.checkbox("同意する場合はチェック")
if checked == True:
 st.write("同意しました")

choice = st.selectbox("１つ選んでください", ("ニュース", "ドラマ", "スポーツ"))
if choice == "ニュース":
 st.write("ニュースが選ばれました")
elif choice == "ドラマ":
 st.write("ドラマが選ばれました")
else:
 st.write("スポーツが選ばれました")

st.sidebar.file_uploader("ファイルをアップロード", type="csv")

x_input = st.sidebar.slider("x の値", min_value=0.0, max_value=10.0, value=0.0,
 step=0.1, format="%.1f")
st.write(f"{x_input} の 2 乗 = {x_input**2:.2f}")