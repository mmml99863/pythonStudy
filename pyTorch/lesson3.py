import torch
from torch.nn import Sequential
from torchvision import transforms
from torch import nn
import torch.nn.functional as F

from pyTorch.lesson2 import YoloDataset


class Model(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # self.conv1 = nn.Conv2d(3, 20, 5)
        # self.conv2 = nn.Conv2d(20, 20, 5)
        self.seq = Sequential(
            # nn.MaxPool2d(2)
            nn.AdaptiveMaxPool2d((256, 256)),
        )

    def forward(self, x):
        # x = F.relu(self.conv1(x))
        # return F.relu(self.conv2(x))
        return self.seq(x)

if __name__ == '__main__':
    model = Model()
    dataset = YoloDataset(
        r'D:\projects\python\pythonStudy\pyTorch\dataSet\HelmetDataset-YOLO-Train\images',
        r'D:\projects\python\pythonStudy\pyTorch\dataSet\HelmetDataset-YOLO-Train\labels',
        transforms.Compose([transforms.ToTensor(), transforms.Resize((512, 512))]),
        None
    )
    img, target = dataset[0]
    output = model(img)
    # print(output)
    # 可视化网站https://netron.app/
    #
    # torch.onnx.export(model, img, 'lesson3-pooling.onnx')
    print(output.shape)
