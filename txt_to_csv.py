import pandas as pd
import os
import re

def convert_txt_to_csv(txt_file_path, csv_file_path):
    with open(txt_file_path, 'r') as file:
        content = file.read()
    
    first_line = content.split('\n')[0]
    first_line = re.sub(r'\t', ',', first_line)
    
    content = content.split('\n')[1:]
    content = '\n'.join(content)
    content = re.sub(r'[ \t]+', ',', content)
    
    content = first_line + '\n' + content
    
    with open(csv_file_path, 'w') as file:
        file.write(content)


for file in os.listdir('datalogs'):
    if file.endswith('.txt'):
        convert_txt_to_csv(f'datalogs/{file}', f'datalogs_csv/{file.replace(".txt", ".csv")}')