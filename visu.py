import pandas as pd
from criminalite import get_criminalite
import streamlit as st
import matplotlib.pyplot as plt
from chomage import get_chomeurs

st.title('Taux de chomage en France par année')
st.write('Source : OpenData')
# Import of datas
data_chomage = get_chomeurs()
data_criminalite = get_criminalite()

fig = plt.figure()
plt.plot(data_chomage['Value']) 
#plt.xlim(2008, 2022

st.pyplot(fig)

st.title('Taux de criminalité en France par année')
st.write('Source : OpenData')
y=data_criminalite['value']

st.bar_chart(y)
#st.pyplot(plt.bar(x, y))
#st.pyplot(fig)
st.dataframe(data_criminalite)