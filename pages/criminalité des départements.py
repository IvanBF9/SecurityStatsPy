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


st.title('Départements les plus criminels notre top 10')
st.write('Source : www.data.gouv.fr')
st.dataframe(crime_by_dept.head(10))
st.title('Le classement complet des départements')
st.dataframe(crime_by_dept)