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
    df['Month'] = month_split
    #df.drop(['TIME'], axis = 1, inplace = True)
    return df


print(get_chomeurs())