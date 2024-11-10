from sklearn.linear_model import LinearRegression

def linear_regression_train(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model

# Example usage
# X = [[0], [1], [2], [3]]
# y = [0, 1, 2, 3]
# model = linear_regression_train(X, y)
# print("Predicted:", model.predict([[4]]))
