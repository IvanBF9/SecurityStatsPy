import pandas as pd
from criminalite import get_criminalite, get_criminalite_by_dept
import streamlit as st
import matplotlib.pyplot as plt
from chomage import get_chomeurs
from population import get_population
from concat import ratio_crime_population, chomeurs_crimes, corr_crime_chomage

# Import of datas
data_chomage = get_chomeurs()
data_criminalite = get_criminalite()
population = get_population()
concat = ratio_crime_population()
crime_by_dept = get_criminalite_by_dept()
corr_crimes = corr_crime_chomage()

# Crimes population ratio
st.title('Ratio crimes / population par année')
concat.index = concat.index.map(str)
chart_data = pd.DataFrame(
    concat,
    columns=['ratio'])

st.area_chart(chart_data)
