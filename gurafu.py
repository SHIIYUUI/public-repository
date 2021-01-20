import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.header("グラフ $y=\sqrt{x}$")
x = np.linspace(0, 10, 1000)
y = x**0.5
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(x, y)
st.pyplot(fig)
