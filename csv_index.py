import os

header = "X (mg);Y (mg);Z (mg)\n"

for folder in os.listdir('dataset'):
    
    folder_path = os.path.join('dataset', folder)
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            if file.endswith('.csv'):
                file_path = os.path.join(folder_path, file)
                
                print(f'Editing file {file_path}')
                
                # Leggi il contenuto del file
                with open(file_path, 'r') as f:
                    content = f.read()
                
                # Aggiungi l'header all'inizio del contenuto
                content = header + content
                
                # Scrivi il contenuto modificato nel file
                with open(file_path, 'w') as f:
                    f.write(content)