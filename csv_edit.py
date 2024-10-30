import pandas as pd
import os

for folder in os.listdir('dataset'):
    
    df_activity = pd.DataFrame()
    
    if os.path.isdir(f'dataset/{folder}'):
        for file in os.listdir(f'dataset/{folder}'):
            if file.endswith('.csv'):
                
                df = pd.read_csv(f'dataset/{folder}/{file}', sep=';')
                df_activity = pd.concat([df_activity, df])
            
        df_activity.to_csv(f'dataset/{folder}.csv', index=False, sep=';')