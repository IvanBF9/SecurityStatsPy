import pandas as pd

def get_criminalite():
        df = pd.read_csv('./data/Crimes/france_entiere_df_clean.csv')

        complain_types = df.groupby(by='', dropna=False).sum()
        complain_types.transpose().sum()

        return df

print(get_criminalite())
