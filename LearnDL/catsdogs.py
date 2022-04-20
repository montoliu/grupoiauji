# Basado en:
# https://www.kaggle.com/code/reukki/pytorch-cnn-tutorial-with-cats-and-dogs/notebook
import random
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torchvision import transforms
from torch.utils.data import DataLoader
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
from sklearn.model_selection import train_test_split
from LearnDL.MyCNN import MyCnn
from LearnDL.MyDataset import MyDataset
from PIL import Image


# ------------------------------------------------------
# codigo para entrenar la NN
# ------------------------------------------------------
def train(epochs, train_loader, val_loader, model, optimizer, criterion):
    for epoch in range(epochs):
        epoch_loss = 0
        epoch_accuracy = 0

        for data, label in train_loader:  # se obtienen un batch de entre todas las muestras de entrenamiento
            data = data.to(device)      # batch_size muestras de las que hay en el conjunto de entrenamiento
            label = label.to(device)    # Sus labels

            output = model(data)            # estimacion para los datos
            loss = criterion(output, label)

            # con estas tres lineas se le dice al modelo que mejore para el futuro
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            acc = ((output.argmax(dim=1) == label).float().mean())  # exactitud de las muestras de train en el batch
            epoch_accuracy += acc / len(train_loader)
            epoch_loss += loss / len(train_loader)

        print('Epoch : {}, train accuracy : {}, train loss : {}'.format(epoch + 1, epoch_accuracy, epoch_loss))

        # idem con las muestras de validación.
        # Aquí no mejoramos el modelo con esas muestras. Solo nos dirve para comprobar como va
        with torch.no_grad():
            epoch_val_accuracy = 0
            epoch_val_loss = 0
            for data, label in val_loader:
                data = data.to(device)
                label = label.to(device)

                val_output = model(data)
                val_loss = criterion(val_output, label)

                acc = ((val_output.argmax(dim=1) == label).float().mean())
                epoch_val_accuracy += acc / len(val_loader)
                epoch_val_loss += val_loss / len(val_loader)

            print('Epoch : {}, val_accuracy   : {}, val_loss   : {}'.format(epoch + 1, epoch_val_accuracy, epoch_val_loss))


# ------------------------------------------------------
# Predecir la etiqueta de las imagenes de test
# ------------------------------------------------------
def test(test_loader, model):
    dog_probs = []
    model.eval()
    with torch.no_grad():
        for data, fileid in test_loader:
            data = data.to(device)
            preds = model(data)      # predicciones
            preds_list = F.softmax(preds, dim=1)[:, 1].tolist()    # obtiene la prob de ser perro
            dog_probs += list(zip(list(fileid), preds_list))

    return dog_probs


# ------------------------------------------------------
# Mostrar algunos resultados en una figura
# ------------------------------------------------------
def mostrar_resultados(submission, test_dir):
    class_ = {0: 'cat', 1: 'dog'}
    fig, axes = plt.subplots(2, 5, figsize=(20, 12), facecolor='w')

    for ax in axes.ravel():
        i = random.choice(submission['id'].values)

        label = submission.loc[submission['id'] == i, 'label'].values[0]
        if label > 0.5:
            label = 1
        else:
            label = 0

        img_path = os.path.join(test_dir, '{}.jpg'.format(i))
        img = Image.open(img_path)

        ax.set_title(class_[label])
        ax.imshow(img)

    plt.show()


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
if __name__ == '__main__':
    # hyperparametros
    lr = 0.001        # learning_rate
    batch_size = 100  # we will use mini-batch method
    epochs = 50       # How much to train a model
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

    train_data = MyDataset(train_list, transform=my_transforms)
    val_data = MyDataset(val_list, transform=my_transforms)
    test_data = MyDataset(test_list, transform=my_transforms)

    train_loader = torch.utils.data.DataLoader(dataset=train_data, batch_size=batch_size, shuffle=True)
    val_loader = torch.utils.data.DataLoader(dataset=val_data, batch_size=batch_size, shuffle=True)
    test_loader = torch.utils.data.DataLoader(dataset=test_data)

    # crear la NN
    model = MyCnn().to(device)
    model.train()
    optimizer = optim.Adam(params=model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()

    # Entrenamiento
    train(epochs, train_loader, val_loader, model, optimizer, criterion)

    # Estimar la probablidad de que cada imagen de test sea un perro
    dog_probs = test(test_loader, model)
    dog_probs.sort(key=lambda x: int(x[0]))
    print(dog_probs)

    # crear submision para el concurso de kaggle
    idx = list(map(lambda x: x[0], dog_probs))
    prob = list(map(lambda x: x[1], dog_probs))
    submission = pd.DataFrame({'id': idx, 'label': prob})
    submission.to_csv('result.csv', index=False)

    # ver algunos resultados
    mostrar_resultados(submission, test_dir)

