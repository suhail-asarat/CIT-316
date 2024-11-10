from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np

# Define the dataset
X = [['Rainy', 'Hot', 'High', 'False'],
     ['Rainy', 'Hot', 'High', 'True'],
     ['Overcast', 'Hot', 'High', 'False'],
     ['Sunny', 'Mild', 'High', 'False'],
     ['Sunny', 'Cool', 'Normal', 'False'],
     ['Sunny', 'Cool', 'Normal', 'True'],
     ['Overcast', 'Cool', 'Normal', 'True'],
     ['Rainy', 'Mild', 'High', 'False'],
     ['Rainy', 'Cool', 'Normal', 'False'],
     ['Sunny', 'Mild', 'Normal', 'False'],
     ['Rainy', 'Mild', 'Normal', 'True'],
     ['Overcast', 'Mild', 'High', 'True'],
     ['Overcast', 'Hot', 'Normal', 'False'],
     ['Sunny', 'Mild', 'High', 'True']]

y = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']

# Encode the features
encoder = OneHotEncoder(sparse_output=False)
X_encoded = encoder.fit_transform(X)

# Create a Decision Tree classifier
clf = DecisionTreeClassifier()

# Train the classifier
clf = clf.fit(X_encoded, y)

# Visualize the decision tree
plt.figure(figsize=(15, 10))
tree.plot_tree(clf, filled=True, feature_names=encoder.get_feature_names_out(), class_names=np.unique(y))
plt.show()

# Test a new case
new_case = [['Sunny', 'Cool', 'Normal', 'False']]
new_case_encoded = encoder.transform(new_case)
prediction = clf.predict(new_case_encoded)
print("Prediction for the new case:", prediction)
