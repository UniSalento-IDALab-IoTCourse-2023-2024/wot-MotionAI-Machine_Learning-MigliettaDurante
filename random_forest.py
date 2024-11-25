import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
import matplotlib.pyplot as plt
import seaborn as sns

# Carica il file CSV
df = pd.read_csv('dataset.csv', sep=';', low_memory=False)

# Separazione delle colonne delle feature e del target
X = df.drop(columns='Activity')
Y = df['Activity']

# Dividi il dataset
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=150)

# Addestramento Random Forest
random_forest = RandomForestClassifier(n_estimators=150, random_state=150)

print('Fit Random Forest')
random_forest.fit(X_train, y_train)

print('Predict')
y_pred = random_forest.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

report = classification_report(y_test, y_pred)
print(f'Classification Report:\n{report}')

print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))

# Converte il modello in formato ONNX
initial_type = [('float_input', FloatTensorType([None, X.shape[1]]))]
onnx_model = convert_sklearn(random_forest, initial_types=initial_type)

# Salva il modello in formato ONNX
with open('random_forest.onnx', 'wb') as file:
    file.write(onnx_model.SerializeToString())

# Stampo la matrice di confusione per le 4 classi: driving, running, stationary, walking
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Driving', 'Running', 'Stationary', 'Walking'], yticklabels=['Driving', 'Running', 'Stationary', 'Walking'])
plt.xlabel('Valori predetti')
plt.ylabel('Valori reali')
plt.title('Matrice di Confusione Random Forest')
plt.show()

# Output:

# 150 trees random state 150
# random state train test split 150

# Accuracy: 0.9826254826254827
# Classification Report:
#               precision    recall  f1-score   support

#      Driving       1.00      1.00      1.00       215
#      Running       1.00      1.00      1.00        61
#   Stationary       0.98      0.96      0.97       128
#      Walking       0.96      0.97      0.97       114

#     accuracy                           0.98       518
#    macro avg       0.98      0.98      0.98       518
# weighted avg       0.98      0.98      0.98       518

# Confusion Matrix:
# [[214   0   0   1]
#  [  0  61   0   0]
#  [  1   0 123   4]
#  [  0   0   3 111]]
