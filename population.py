import pandas as pd

def get_population():
        df = pd.read_excel('./data/Population/population.xlsx', skiprows=3)
        df.columns = ['Date', 'Value', 'D', 'E', 'F', 'G', 'H', 'I']


        df.drop([0, 1, 2, 15, 16, 17, 18, 19, 20, 21, 22, 23], axis=0, inplace=True)

        df['Date'] = pd.to_numeric(df['Date'])
        df = df.sort_values(by=['Date'])

        clean_df = pd.DataFrame()
        clean_df['Date'] = df['Date']
        clean_df['Value'] = df['Value']
        clean_df['Value'] = clean_df['Value'] * 1000
        clean_df = clean_df.astype({'Value':'int'})
        clean_df = clean_df.set_index('Date')

        return clean_df


print(get_population())
