import pandas as pd
import os

df_completo = pd.DataFrame()

for file in os.listdir('datalogs_csv'):
    if file.endswith('.csv'):
        df = pd.read_csv(f'datalogs_csv/{file}')

        df['Y'] = file.replace('.csv', '')
        
        df_completo = pd.concat([df_completo, df])

df_completo.to_csv('datalog.csv', sep=';', index=False)
