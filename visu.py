from asyncore import file_dispatcher
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
from chomage import get_chomeurs

data_chomage = get_chomeurs()

fig = plt.figure()

plt.plot(data_chomage['Value'])
#plt.xlim(2008, 2022)

st.pyplot(fig)

