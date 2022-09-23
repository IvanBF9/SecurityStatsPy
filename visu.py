import pandas as pd
from criminalite import get_criminalite, get_criminalite_by_dept
import streamlit as st
import matplotlib.pyplot as plt
from chomage import get_chomeurs
from population import get_population
from concat import ratio_crime_population, chomeurs_crimes

# Import of datas
data_chomage = get_chomeurs()
data_criminalite = get_criminalite()
population = get_population()
concat = ratio_crime_population()
crime_by_dept = get_criminalite_by_dept()

st.title('Nombre de crimes en France par année')
st.write('Source : www.data.gouv.fr')
y=data_criminalite['value']

st.bar_chart(y)
datacrime_list = data_criminalite.T
st.dataframe(datacrime_list)


st.title('Population en France par année')
st.write('Source : www.insee.fr')

st.bar_chart(population['Value'])



st.title('Taux de chomage en France par année')
st.write('Source : www.insee.fr')
chart_data = pd.DataFrame(
    data_chomage,
    columns=['Value'])

st.line_chart(chart_data)

# Crimes population ratio
st.title('Ratio crimes / population par année')
chart_data = pd.DataFrame(
    concat,
    columns=['ratio'])

st.line_chart(chart_data)

st.title('Crimes et chomeurs par année')
chart_data = pd.DataFrame(
    chomeurs_crimes(),
    columns=['chomeurs', 'criminalite'])

st.line_chart(chart_data)

st.title('Départements les plus criminels notre top 10')
st.write('Source : www.data.gouv.fr')
st.dataframe(crime_by_dept.head(10))
st.write('Le classement complet des départements')
st.dataframe(crime_by_dept)