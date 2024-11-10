from sklearn.neural_network import MLPClassifier

def neural_network_train(X, y):
    model = MLPClassifier(max_iter=1000)
    model.fit(X, y)
    return model

# Example usage
X = [[0, 0], [1, 1]]
y = [0, 1]
model = neural_network_train(X, y)
print("Predicted:", model.predict([[2, 2]]))
