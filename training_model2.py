import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Charger les données
data = pd.read_csv("dataset-tortuga-filled-modified6.csv")

# 2. Pré-traitement des données
# Convertir les valeurs catégorielles en numériques pour l'entraînement
data['ORIENTATION'] = data['ORIENTATION'].map({'PRACTICE': 1, 'THEORY': 0})
data.drop(['FAV_COURS', 'HAT_COURS'], axis=1, inplace=True)  # Supprimer les colonnes qui ne seront pas utilisées comme caractéristiques pour la formation

# 3. Séparer les données
X = data.drop("PROFILE", axis=1)
y = data["PROFILE"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Entraîner le modèle
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

# 5. Prédiction et évaluation
y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print(classification_report(y_test, y_pred))


# ----------- TEST -----------

# Import necessary libraries
import numpy as np

# Define new observations (the values must be in the same order as in your training data)
new_observation_1 = np.array([[1, 3, 4, 2, 0, 1, 75, 68, 70, 60, 50, 150, 120, 130, 100, 110, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
new_observation_2 = np.array([[2, 1, 5, 3, 1, 0, 80, 90, 85, 70, 60, 160, 180, 150, 110, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


predictions_1 = clf.predict(new_observation_1)
predictions_2 = clf.predict(new_observation_2)

print(f"Prediction for observation 1: {predictions_1[0]}")
print(f"Prediction for observation 2: {predictions_2[0]}")

import joblib

# Assume that `model` is the trained model
joblib.dump(clf, 'model_3.pkl')
