import pandas as pd

def get_chomeurs():
    df = pd.read_csv('./data/chomage/chomage.csv')

    #df.drop(df.columns.difference(['TIME','Value']), 1, inplace=True)
    #df = df.loc[:, df.columns.intersection(['TIME','Value'])]
    df = df[['TIME', 'Value']]

    month_split = []
    year_split = []

    for date_month in df['TIME']:
        year = date_month.split('-')[0]
        month = date_month.split('-')[1]
        year_split.append(year)
        month_split.append(month)

    df['Year'] = year_split
    df = df.groupby('Year').agg({'Value' : ['mean']})['Value']#.sort_index()
    
    new_dataframe = pd.DataFrame(df)
    new_dataframe.sort_index()
    df.rename(columns={'mean': 'Value'}, inplace=True, errors='raise')

    #df['Year'] = pd.to_numeric(df['Year'])
    #df = df.sort_values(by=['Year'])
    #df = df.set_index('Year')
    #df['Month'] = month_split
    #df.drop(['TIME'], axis = 1, inplace = True)
    return new_dataframe


print(get_chomeurs())