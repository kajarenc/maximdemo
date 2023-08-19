import streamlit as st
import numpy as np
import pandas as pd
import plotly.figure_factory as ff


@st.cache_data
def load_data():
    return pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list("ABCD"))


my_data = load_data()

st.data_editor(my_data)

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ["Group 1", "Group 2", "Group 3"]

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.1, 0.25, 0.5])

# Plot!
st.plotly_chart(fig, use_container_width=True)
