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

def get_criminalite_by_dept():
        dept_df = pd.read_csv('./data/Crimes/chiffre_departement_df_clean.csv')
        dept_df = dept_df.groupby('departement').sum()
        dept_df['sum'] = dept_df.iloc[:, 1:].sum(axis=1)
        dept_df.sort_values(by=["sum"], inplace = True, ascending=False)
        dept_df.drop(dept_df.columns.difference(['departement','sum']), 1, inplace=True)
        dept_df = dept_df.astype({'sum':'int'})
        dept_df.rename(columns={'sum': 'crimalite'},inplace=True, errors='raise')
        dept_df['departement'] = dept_df.index.tolist()
        dept_df['index'] = range(1, len(dept_df) + 1)
        dept_df = dept_df.astype({'departement':'str'})
        dept_df = dept_df.astype({'index':'int'})
        dept_df = dept_df.set_index('index')

        return dept_df

print(get_criminalite_by_dept())
