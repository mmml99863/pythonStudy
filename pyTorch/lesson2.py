from PIL import Image
from torch.utils.data import Dataset
import pandas as pd
import os

from torchvision import transforms


class YoloDataset(Dataset):
    def __init__(self, image_folder, label_folder, transform=None, label_transform=None):
        self.image_folder = image_folder
        self.label_folder = label_folder
        self.transform = transform
        self.label_transform = label_transform
        self.images_names = os.listdir(self.image_folder)

    def __getitem__(self, index):
        img_name = self.images_names[index]
        img_path = os.path.join(self.image_folder, img_name)
        img = Image.open(img_path).convert('RGB')
        label_name = img_name.split('.')[0] + '.txt'
        label_path = os.path.join(self.label_folder, label_name)
        with open(label_path, 'r', encoding='utf-8') as f:
            label_content = f.read()
            content_list = label_content.strip().split('\n')
            f.close()
        target = []
        for content_item in content_list:
            info_list = content_item.strip().split(' ')
            class_id = float(info_list[0])
            center_x = float(info_list[1])
            center_y = float(info_list[2])
            yolo_width = float(info_list[3])
            yolo_height = float(info_list[4])
            info_content = list([class_id, center_x, center_y, yolo_width, yolo_height])
            target.extend(info_content)

        if self.transform is not None:
            img = self.transform(img)
        return img, target

    """图片的数量"""
    def __len__(self) -> int:
        return len(self.images_names)

# if __name__ == "__main__":
#     train_dataset = YoloDataset(r'D:\projects\python\pythonStudy\pyTorch\dataSet\HelmetDataset-YOLO-Train\images',
#                                r'D:\projects\python\pythonStudy\pyTorch\dataSet\HelmetDataset-YOLO-Train\labels',
#                                transforms.Compose([transforms.ToTensor()]), None)
#     print(len(train_dataset))
#     print(train_dataset[0])
