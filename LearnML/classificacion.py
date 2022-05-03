# Based on: https://www.youtube.com/watch?v=pqNCD_5r0IU&ab_channel=freeCodeCamp.org
# https://github.com/DL-Academy/MachineLearningSKLearn/blob/master/traintestsplit

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier

if __name__ == '__main__':
    data = datasets.load_iris()
    #data = datasets.load_breast_cancer()

    x = data.data
    y = data.target

    # 80% para entrenar, 20% para testear
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    print("Train dataset: " + str(x_train.shape))
    print("Test dataset : " + str(x_test.shape))

    # knn k=1
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    acc = accuracy_score(y_test, predictions)
    print("K==1 accuracy = " + str(acc))

    # knn k=3
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    acc = accuracy_score(y_test, predictions)
    print("K==3 accuracy = " + str(acc))

    # Gaussian Bayes
    model = GaussianNB()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    acc = accuracy_score(y_test, predictions)
    print("NB accuracy = " + str(acc))

    # Decsion Tree
    model = DecisionTreeClassifier()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    acc = accuracy_score(y_test, predictions)
    print("Tree accuracy = " + str(acc))

    # Decision Tree
    model = svm.SVC()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    acc = accuracy_score(y_test, predictions)
    print("SVM accuracy = " + str(acc))

    # NN
    model = MLPClassifier()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    acc = accuracy_score(y_test, predictions)
    print("NN accuracy = " + str(acc))
