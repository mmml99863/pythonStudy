import torch
import xmltodict
from PIL import Image
from torch.utils.data import Dataset
import os

from torchvision import transforms


class VocDataset(Dataset):
    def __init__(self, image_folder, label_folder, transform=None, label_transform=None):
        self.image_folder = image_folder
        self.label_folder = label_folder
        self.transform = transform
        self.label_transform = label_transform
        self.images_names = os.listdir(self.image_folder)
        self.class_list = ['no helmet', 'motor', 'number', 'with helmet']

    def __getitem__(self, index):
        img_name = self.images_names[index]
        img_path = os.path.join(self.image_folder, img_name)
        img = Image.open(img_path).convert('RGB')
        label_name = img_name.split('.')[0] + '.xml'
        label_path = os.path.join(self.label_folder, label_name)
        with open(label_path, 'r', encoding='utf-8') as f:
            label_content = f.read()
            f.close()
        label_dict = xmltodict.parse(label_content)
        label_objects = label_dict['annotation']['object']
        target = []
        for label_object in label_objects:
            label_obj_name = label_object['name']
            label_class_id = self.class_list.index(label_obj_name)
            label_obj_bndbox = label_object['bndbox']
            label_obj_xmax = float(label_obj_bndbox['xmax'])
            label_obj_ymax = float(label_obj_bndbox['ymax'])
            label_obj_xmin = float(label_obj_bndbox['xmin'])
            label_obj_ymin = float(label_obj_bndbox['ymin'])
            label_obj = list([label_class_id, label_obj_xmin, label_obj_ymin, label_obj_xmax, label_obj_ymax])
            target.append(label_obj)
        target = torch.Tensor(target)
        if self.transform is not None:
            img = self.transform(img)
        return img, target

    """图片的数量"""
    def __len__(self) -> int:
        return len(self.images_names)

if __name__ == "__main__":
    train_dataset = VocDataset(r'D:\projects\python\pythonStudy\pyTorch\dataSet\HelmetDataset-VOC\train\images',
                               r'D:\projects\python\pythonStudy\pyTorch\dataSet\HelmetDataset-VOC\train\labels',
                               transforms.Compose([transforms.ToTensor()]), None)
    print(len(train_dataset))
    print(train_dataset[0])
