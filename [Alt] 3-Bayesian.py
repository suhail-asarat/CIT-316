import pandas as pd
from collections import defaultdict
from math import prod

class NaiveBayesClassifier:
    def __init__(self):
        self.feature_probs = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
        self.class_probs = defaultdict(float)

    def fit(self, data, target):
        # Calculate the probability of each class (target) and conditional probabilities for features
        total_samples = len(data)
        classes = data[target].unique()
        
        for c in classes:
            class_data = data[data[target] == c]
            self.class_probs[c] = len(class_data) / total_samples
            
            for feature in data.columns[:-1]:  # Exclude target column
                feature_counts = class_data[feature].value_counts(normalize=True)
                for val, prob in feature_counts.items():
                    self.feature_probs[feature][val][c] = prob

    def predict(self, instance):
        # Calculate posterior probabilities for each class
        class_scores = {}
        for c in self.class_probs:
            # P(c) * P(f1|c) * P(f2|c) * ... * P(fn|c)
            class_scores[c] = self.class_probs[c] * prod(
                self.feature_probs[feature][instance[feature]][c]
                for feature in instance
            )
        
        # Choose the class with the highest posterior probability
        return max(class_scores, key=class_scores.get), class_scores

# Sample data
data = {
    'Outlook': ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy', 'overcast', 'sunny', 'sunny', 'rainy', 'sunny', 'overcast', 'overcast', 'rainy'],
    'Temperature': ['hot', 'hot', 'hot', 'mild', 'cool', 'cool', 'cool', 'mild', 'cool', 'mild', 'mild', 'mild', 'hot', 'mild'],
    'Humidity': ['high', 'high', 'high', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'high'],
    'Windy': [False, True, False, False, False, True, True, False, False, False, True, True, False, True],
    'Play': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Initialize and train the classifier
nb_classifier = NaiveBayesClassifier()
nb_classifier.fit(df, 'Play')

# Test with a new instance
test_instance = {'Outlook': 'sunny', 'Temperature': 'cool', 'Humidity': 'high', 'Windy': True}
prediction, class_scores = nb_classifier.predict(test_instance)

print("Predicted class:", prediction)
print("Class probabilities:", class_scores)
