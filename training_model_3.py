import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import numpy as np

# 1. Load the data
data = pd.read_csv("dataset-tortuga-filled-modified7.csv")

# 2. Data preprocessing
data['ORIENTATION'] = data['ORIENTATION'].map({'PRACTICE': 1, 'THEORY': 0})
data.drop(['FAV_COURS', 'HAT_COURS'], axis=1, inplace=True)

# 3. Splitting the data
X = data.drop(["USER_ID", "NAME", "PROFIL_DATASCIENCE", "PROFIL_BACKEND", "PROFIL_FRONTEND", "PROFIL_IA", "PROFIL_BDD"], axis=1)
y = data[["PROFIL_DATASCIENCE", "PROFIL_BACKEND", "PROFIL_FRONTEND", "PROFIL_IA", "PROFIL_BDD"]]

# Create train and test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the model using MultiOutputClassifier
forest = RandomForestClassifier(n_estimators=100)
multi_target_forest = MultiOutputClassifier(forest, n_jobs=-1)
multi_target_forest.fit(X_train, y_train)

# 5. Make predictions and evaluate
y_pred = multi_target_forest.predict(X_test)

# Print accuracy for each profile column
for idx, col in enumerate(y.columns):
    accuracy = accuracy_score(y_test.iloc[:, idx], y_pred[:, idx])
    print(f"Accuracy for {col}: {accuracy:.2f}%")

# 6. Save the trained model to a file
joblib.dump(multi_target_forest, 'multi_target_model_4.pkl')

# 7. Test
new_observation = np.array([[7,	39, 29,	5, 30, 2, 4, 5,	25,	15,	2,	35,	50,	11,	20,	84,	74,	19,	73,	53,	32,	238, 268 ,12 ,131, 0]])
# Make predictions for new observations
predictions = multi_target_forest.predict(new_observation)
print(f"Prediction for observation 1: {predictions[0]}")

