# MotionAI Machine Learning

Questa repository contiene il codice per un progetto di Machine Learning che utilizza un modello di Random Forest per classificare diverse attività motorie come driving, running, stationary e walking. Oltre all'addestramento esegue anche una parte di preprocessing dei dati.

## Contenuto della repository

- `csv_edit.py`: Script per unire più file CSV contenenti dati raccolti dall'accelerometro in 4 file, uno per ogni attività.
tali file sono stati ottenuti dalla repository presente al seguente link: [STMicroelectronics Human activities dataset](https://github.com/STMicroelectronics/stm32ai-wiki/tree/master/AI_resources/HAR/dataset), apparte per i dati di driving che sono stati raccolti personalmente.
- `csv_index.py`: Aggiunge l'header (X (mg);Y (mg); Z (mg)) ai file csv.
- `preprocessing.py`: Raccoglie i dati dell'accelerometro dai file `driving.csv`, `running.csv`, `stationary.csv` e `walking.csv`, ogni 60 campioni calcola, per ogni coordinata: le medie, le varianze, i valori picco picco ed il numero di zero crossings, creando un unico dataframe e memorizzandolo nel file `dataset.csv`.
- `random_forest.py`: Usa i dati raccolti nel file `dataset.csv` per addestrare un modello di Random Forest e per valutarne le prestazioni stampando in terminale l'accuratezza e il classification report (formato dai valori di `precision`, `recall`, `f1-score` e `support`). Infine crea la `matrice di confusione` tramite matplotlib e seaborn.
- `random_forest.onnx`: Modello di Random Forest addestrato, serializzato e memorizzato in un formato compatibile con il linguaggio `Kotlin`.

## Funzionalità

1. **Preprocessing**: Gli script `csv_index.py`, `csv_edit.py` e `preprocessing.py` preparano i dati grezzi dell'accelerometro per formare le feature di addestramento, ottenendo così un unico DataFrame e memorizzandolo in `dataset.csv`.
2. **Addestramento del modello**: Lo script `random_forest.py` carica il file `dataset.csv`, separa le feature dal target, divide i dati in set di addestramento e test, addestra un modello di Random Forest e visualizza le sue prestazioni.
3. **Valutazione del modello**: Le prestazioni valutate consistono in: accuratezza del modello, report di classificazione e matrice di confusione per le diverse classi di attività.

## Requisiti

- Python 3.x
- pandas
- scikit-learn
- matplotlib
- seaborn

## Esecuzione

1. Eseguire in ordine `csv_index.py`, `csv_edit.py` e `preprocessing.py` per generare il file `dataset.csv`.
2. Eseguire `random_forest.py` per addestrare il modello di Random Forest, generare il file `random_forest.onnx` e visualizzarne le prestazioni.