import pandas as pd
from criminalite import get_criminalite
from chomage import get_chomeurs, get_population_chomage
from population import get_population

population = get_population()
criminalite = get_criminalite()
chomeurs = get_chomeurs()

chomeurs.columns = ['chomage']
criminalite.columns = ['criminalite']
population.columns = ['population']

#chomeurs['chomage'] = pd.to_numeric(chomeurs['chomage'])
criminalite = criminalite.astype({'criminalite':'int'})
#criminalite['criminalite'] = pd.to_numeric(criminalite['criminalite'])
#population = population.astype({'population':'int'})
#population['population'] = pd.to_numeric(population['population'])

concat = criminalite

concat = pd.merge(criminalite, population,  left_index=True, right_index=True)

#concat = pd.merge(concat, chomeurs,  left_index=True, right_index=True)

print(concat)

def ratio_crime_population():

    ratio_df = pd.DataFrame()

    ratio_df['ratio'] = concat['criminalite'] / concat['population'] * 100

    return ratio_df


def chomeurs_crimes():
    
    chomeurs_crimes_df = get_criminalite()

    chomeurs_crimes_df = pd.merge(criminalite,  get_population_chomage(),  left_index=True, right_index=True)
    chomeurs_crimes_df.rename(columns={'Value': 'chomeurs'},inplace=True, errors='raise')

    return chomeurs_crimes_df



print(chomeurs_crimes())
#for date, row in criminalite.iteritems():
#    if chomeurs.loc[chomeurs['Year'] == date] != None :
#        print(chomeurs.loc[chomeurs['Year'] == date])
        #concat.loc[date, 'chomeurs'] = chomeurs.loc[chomeurs['Year'] == date]['Value']