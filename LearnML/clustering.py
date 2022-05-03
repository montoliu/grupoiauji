from sklearn.datasets import load_breast_cancer
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import scale
import pandas as pd

if __name__ == '__main__':
    bc = load_breast_cancer()
    X = scale(bc.data)
    y = bc.target

    model = KMeans(n_clusters=2)
    model.fit(X)

    print(model.labels_)