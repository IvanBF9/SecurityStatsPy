import pandas as pd
from population import get_population

def get_chomeurs():
    df = pd.read_csv('./data/chomage/chomage.csv')
    
    df = df[['TIME', 'Value']]

    month_split = []
    year_split = []

    for date_month in df['TIME']:
        year = date_month.split('-')[0]
        month = date_month.split('-')[1]
        year_split.append(year)
        month_split.append(month)

    df['Year'] = year_split
    df['Year'] = pd.to_numeric(df['Year'])
    df = df.groupby('Year').agg({'Value' : ['mean']})['Value']#.sort_index()
    
    new_dataframe = pd.DataFrame(df)
    new_dataframe.sort_index()
    df.rename(columns={'mean': 'Value'}, inplace=True, errors='raise')
    df['Value'] = pd.to_numeric(df['Value'])

    return new_dataframe


def get_population_chomage():
    df_chomage = get_chomeurs()
    df_population = get_population()
    df_population_chomage = pd.merge(df_chomage, df_population, left_index=True, right_index=True)
    df_population_chomage['Value'] = (df_population_chomage['Value_y'] / 100) *  df_population_chomage['Value_x']
    df_population_chomage = df_population_chomage[['Value']]
    df_population_chomage = df_population_chomage.astype({'Value':'int'})
    return df_population_chomage

print(get_population_chomage())