# MotionAI Machine Learning

Questa repository contiene il codice per un progetto di Machine Learning che utilizza un modello di Random Forest per classificare diverse attività motorie come biking, driving, jogging, stationary e walking. Oltre all'addestramento esegue anche una parte di preprocessing dei dati.

## Contenuto della repository

- `csv_join.py`: Script per unire più file CSV contenenti dati di log in un unico file `datalog.csv`.
- `random_forest.py`: Script per addestrare un modello di Random Forest utilizzando i dati uniti e per valutare le prestazioni del modello.
- `datalog.csv`: File CSV generato contenente i dati di log uniti.
- `random_forest.pkl`: Modello di Random Forest addestrato e salvato.

## Funzionalità

1. **Unione dei file CSV**: Lo script `csv_join.py` legge tutti i file CSV nella cartella `datalogs_csv`, li unisce in un unico DataFrame e salva il risultato in `datalog.csv`.
2. **Addestramento del modello**: Lo script `random_forest.py` carica il file `datalog.csv`, separa le feature dal target, divide i dati in set di addestramento e test, addestra un modello di Random Forest e valuta le sue prestazioni.
3. **Valutazione del modello**: Lo script calcola l'accuratezza del modello, stampa un report di classificazione e visualizza una matrice di confusione per le diverse classi di attività.

## Requisiti

- Python 3.x
- pandas
- scikit-learn
- matplotlib
- seaborn

## Esecuzione

1. Esegui `csv_join.py` per generare il file `datalog.csv`.
2. Esegui `random_forest.py` per addestrare il modello di Random Forest e valutare le sue prestazioni.