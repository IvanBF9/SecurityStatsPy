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

st.title('Crimes et chomeurs par année')
st.write('corrélation: ' + str(corr_crimes))
crimes_chom = chomeurs_crimes()
crimes_chom.index = crimes_chom.index.map(str)
chart_data = pd.DataFrame(
    crimes_chom,
    columns=['chomeurs', 'criminalite'])

st.line_chart(chart_data)
