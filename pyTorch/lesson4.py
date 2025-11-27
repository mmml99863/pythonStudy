import os
from os.path import split

from torch.utils.data import Dataset
from torch.utils.data.dataset import _T_co
from torchvision import transforms
from PIL import Image

class DataSet(Dataset):
    def __init__(self, base_folder, image_folder,label_folder,  image_transform=None, label_transform=None):
        self.base_folder = base_folder
        self.images_source = image_folder
        self.label_source = label_folder
        self.image_transform = image_transform
        self.label_transform = label_transform

    def __getitem__(self, index) -> _T_co:
        images_path = os.path.join(self.base_folder, self.images_source)
        labels_path = os.path.join(self.base_folder, self.label_source)
        images_name = os.listdir(images_path)
        self.images_name = images_name
        '''打开文件'''
        for image_name in images_name:
            img_path = os.path.join(images_path, image_name)
            '''将名称更改'''
            if image_name.endswith('jpg'):
                label_name = image_name.split('.')[0] + 'txt'
            img = Image.open(img_path).convert('RGB')

    def __len__(self) -> int:
        return len(self.images_name)