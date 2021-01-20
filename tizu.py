import streamlit as st
import pandas as pd
import numpy as np
st.title("名古屋駅周辺の分布")
df = pd.DataFrame(np.random.normal(0,1,(200, 2))/(10,10) + [35.17, 136.88],
 columns=["lat", "lon"])
st.map(df)
