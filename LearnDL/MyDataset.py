import torch
from torch.utils.data import DataLoader, Dataset
from PIL import Image


class MyDataset(torch.utils.data.Dataset):
    def __init__(self, file_list, transform=None):
        self.file_list = file_list
        self.transform = transform

    # dataset length
    def __len__(self):
        self.filelength = len(self.file_list)
        return self.filelength

    # load an one of images
    def __getitem__(self, idx):
        img_path = self.file_list[idx]
        img = Image.open(img_path)
        img_transformed = self.transform(img)

        label = img_path.split('\\')[-1].split('.')[0]
        # label = img_path.split('/')[-1].split('.')[0]  # linux
        if label == 'dog':
            label = 1.0
        elif label == 'cat':
            label = 0.0

        return img_transformed, label
