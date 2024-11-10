from sklearn.tree import DecisionTreeClassifier

def decision_tree_train(X, y):
    clf = DecisionTreeClassifier()
    clf.fit(X, y)
    return clf

# Example usage
# X = [[0, 0], [1, 1]]
# y = [0, 1]
# model = decision_tree_train(X, y)
# print("Predicted:", model.predict([[2, 2]]))
