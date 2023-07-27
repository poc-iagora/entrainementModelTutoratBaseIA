import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load the data
data = pd.read_csv("dataset-tortuga-filled.csv")

# Drop the columns that are not used
X = data.drop(["USER_ID", "PROFILE"], axis=1)
y = data["PROFILE"]
# Encode the target variable
le = LabelEncoder()
y = le.fit_transform(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = RandomForestClassifier()

# Fit the model
model.fit(X_train, y_train)

# Predict the target variable for the test data
y_pred = model.predict(X_test)

# Print the accuracy of the model
print("Accuracy:", accuracy_score(y_test, y_pred))



# Import necessary libraries
import numpy as np

# Define a new observation (the values must be in the same order as in your training data)
new_observation = np.array([[58283940, 7, 39, 29, 2, 4, 0, 2, 5, 0, 84, 74, 0]])


# Use the model to predict the class of this new observation
predicted_profile = model.predict(new_observation)

# Since you used label encoding to encode the PROFILE values, the output of this prediction will be a number.
# You can use the LabelEncoder object to translate this number back into a string like this:
predicted_profile_label = le.inverse_transform(predicted_profile)

print(predicted_profile_label)