import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle as pkl
import matplotlib.pyplot as plt
import seaborn as sns

# Carica il file CSV
df = pd.read_csv('datalog.csv', sep=';', low_memory=False)

# Separazione delle colonne delle feature e del target
X = df.drop(columns='Y')
Y = df['Y']

# Dividi il dataset
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=35)

# Numero massimo di nodi per albero
max_nodes_per_tree = 128 // 4

# Addestramento Random Forest
random_forest = RandomForestClassifier(n_estimators=4, max_leaf_nodes=max_nodes_per_tree, random_state=42)

print('Fit Random Forest')
random_forest.fit(X_train, y_train)

print('Predict')
y_pred = random_forest.predict(X_test)

# Calcola l'accuratezza
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Stampa il report di classificazione
report = classification_report(y_test, y_pred)
print(f'Classification Report:\n{report}')

# Salva il modello
with open('random_forest.pkl', 'wb') as file:
    pkl.dump(random_forest, file)

# Stampo la matrice di confusione per le 5 classi: biking, driving, jogging, stationary, walking
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Biking', 'Driving', 'Jogging', 'Stationary', 'Walking'], yticklabels=['Biking', 'Driving', 'Jogging', 'Stationary', 'Walking'])
plt.xlabel('Valori predetti')
plt.ylabel('Valori reali')
plt.title('Matrice di Confusione Random Forest')
plt.show()


# Output:

# Accuracy: 0.9462738301559792
# Classification Report:
#               precision    recall  f1-score   support

#       biking       0.95      0.83      0.89       242
#      driving       1.00      1.00      1.00       226
#      jogging       0.96      0.97      0.97       236
#   stationary       1.00      1.00      1.00       219
#      walking       0.84      0.93      0.88       231

#     accuracy                           0.95      1154
#    macro avg       0.95      0.95      0.95      1154
# weighted avg       0.95      0.95      0.95      1154
