import pandas as pd
from criminalite import get_criminalite
import streamlit as st
import matplotlib.pyplot as plt
from chomage import get_chomeurs

data_chomage = get_chomeurs()

fig = plt.figure()

plt.plot(data_chomage['Value']) 
#plt.xlim(2008, 2022)

st.pyplot(fig)

st.title('Taux de criminalité en France par année')

st.write('Source : OpenData')

data_criminalite = get_criminalite()

st.dataframe(data_criminalite)