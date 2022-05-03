from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

if __name__ == '__main__':
    boston = datasets.load_boston()

    X = boston.data
    y = boston.target

    # mostramos todas las muestras, pero solo la dimension 5
    plt.scatter(X[:, 5], y, color="black")
    plt.show()

    l_reg = linear_model.LinearRegression()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = l_reg.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("predictions: ", predictions)

    # mostramos predicciones
    plt.scatter(X_test[:, 5], y_test, color="black")
    plt.show()
