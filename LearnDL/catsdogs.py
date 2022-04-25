# Basado en:
# https://www.kaggle.com/code/reukki/pytorch-cnn-tutorial-with-cats-and-dogs/notebook
import random

import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import os
import glob
from sklearn.model_selection import train_test_split
from MyCNN import MyCnn
from MyDataset import MyDataset
from PIL import Image


# ------------------------------------------------------
# codigo para entrenar la NN
# ------------------------------------------------------
# El proceso de entrenamiento se repite epochs veces
# En cada iteración se selecciona un subconunto (batch) en vez de entrenar con todas
# Así se evita el sobre entrenamiento (overfitting)
def train(epochs, train_loader, val_loader, model, optimizer, criterion):
    for epoch in range(epochs):
        epoch_loss = 0
        epoch_accuracy = 0

        for data, label in train_loader:  # Se obtienen un batch de entre todas las muestras de entrenamiento
            data = data.to(device)        # batch_size muestras de las que hay en el conjunto de entrenamiento
            label = label.float().to(device)    # Sus labels

            output = model(data)       # estimacion para los datos
            output = output.view(output.shape[0])
            loss = criterion(output, label)

            # con estas tres lineas se le dice al modelo que mejore para el futuro
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            acc = sum(torch.round(output) == label) / label.shape[0]
            epoch_accuracy += acc / len(train_loader)
            epoch_loss += loss / len(train_loader)

        # idem con las muestras de validación.
        # Aquí no mejoramos el modelo con esas muestras. Solo nos dirve para comprobar como va
        with torch.no_grad():  # para que no guarde los gradientes ya que no los vamos a usar
            epoch_val_accuracy = 0
            epoch_val_loss = 0
            for data, label in val_loader:
                data = data.to(device)
                label = label.to(device)

                val_output = model(data)
                val_output = val_output.view(val_output.shape[0])
                val_loss = criterion(val_output, label)

                acc = sum(torch.round(val_output) == label) / label.shape[0]
                # acc = ((val_output.argmax(dim=1) == label).float().mean())
                epoch_val_accuracy += acc / len(val_loader)
                epoch_val_loss += val_loss / len(val_loader)

            print("Epoch:" + str(epoch+1) + " Train_acc: {0:0.2f}".format(epoch_accuracy) +
                  " train_loss: {0:0.2f}".format(epoch_loss) +
                  " Val_acc: {0:0.2f}".format(epoch_val_accuracy) +
                  " Val_loss: {0:0.2f}".format(epoch_val_accuracy))


# ------------------------------------------------------
# Predecir la etiqueta de las imagenes de test
# Se prefice la probabilidad de que la imagen sea un perro
# ------------------------------------------------------
def test(test_loader, model):
    dog_probs = []
    model.eval()
    with torch.no_grad():
        for data, fileid in test_loader:
            data = data.to(device)
            preds = model(data)
            id_image = int(fileid[0])
            prob_image = preds.cpu().numpy()[0, 0]
            dog_probs.append([id_image, prob_image])

    return dog_probs


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
if __name__ == '__main__':
    # hyperparametros
    lr = 0.001        # learning_rate
    batch_size = 100  # we will use mini-batch method
    epochs = 10       # How much to train a model
    print("Learning rate: " + str(lr))
    print("Batch size   : " + str(batch_size))
    print("Epochs       : " + str(epochs))

    # Por si tenemos GPU
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print("Device       : " + device)

    # Variables utiles para saber donde tenemos las imagenes
    # Se recomienda empezar con el dataset mini_train y mini_test
    train_dir = './data/mini_train'
    test_dir = './data/mini_test'

    train_list = glob.glob(os.path.join(train_dir, '*.jpg'))
    test_list = glob.glob(os.path.join(test_dir, '*.jpg'))
    print("There are " + str(len(train_list)) + " images for training")
    print("There are " + str(len(test_list)) + " images for testing")

    # Crear conjunto de entrenamiento (80%) y de validacion (20%)
    train_list, val_list = train_test_split(train_list, test_size=0.2)

    # Transforma imagen en Tensors
    my_transforms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        ])

    # Pytorch datasets
    train_data = MyDataset(train_list, transform=my_transforms)
    val_data = MyDataset(val_list, transform=my_transforms)
    test_data = MyDataset(test_list, transform=my_transforms)

    train_loader = torch.utils.data.DataLoader(dataset=train_data, batch_size=batch_size, shuffle=True)
    val_loader = torch.utils.data.DataLoader(dataset=val_data, batch_size=batch_size, shuffle=True)
    test_loader = torch.utils.data.DataLoader(dataset=test_data)

    # crear la NN
    model = MyCnn().to(device)
    model.train()                                              # Indicamos que vamos a entrenar el modelo
    optimizer = optim.Adam(params=model.parameters(), lr=lr)   # Una forma de actualizar los parametros
    criterion = nn.MSELoss()                                   # Para comparar lo que da con lo que es

    # Entrenamiento
    train(epochs, train_loader, val_loader, model, optimizer, criterion)

    # Estimar la probablidad de que cada imagen de test sea un perro
    dog_probs = test(test_loader, model)
    dog_probs.sort(key=lambda x: int(x[0]))
    print(dog_probs)

    true_labels = pd.read_csv("./data/true_labels.csv", header=None)
    true_labels = true_labels.values
    acc = 0
    for i in range(len(dog_probs)):
        if dog_probs[i][1] >= 0.5:
            est_label = 1
        else:
            est_label = 0

        true_label = true_labels[i][0]

        if est_label == true_label:
            acc += 1
        else:
            print(str(i+1) + " -> Estimated: " + str(est_label) + " but it is: " + str(true_label))

    print("Accuracy on test set: " + str(acc/len(dog_probs)))



