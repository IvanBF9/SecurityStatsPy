import pandas as pd

def get_criminalite():
        df = pd.read_csv('./data/Crimes/france_entiere_df_clean.csv')

        columns_concat = []
        for col in df.columns:
                if col != 'Unnamed: 0':
                        columns_concat.append(col)

        df_sum = pd.DataFrame()

        df_sum['date'] = df['Unnamed: 0']
        df_sum['date'] = pd.to_numeric(df_sum['date'])
        df_sum['value'] = df.iloc[:,-abs(len(df.columns) - 1):].sum(axis=1)
        df_sum = df_sum.sort_values(by=['date'])
        df_sum = df_sum.set_index('date')

        return df_sum

print(get_criminalite())
