import torch
from torchvision import transforms
from PIL import Image
import argparse
import numpy as np


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Predicts the season by a given photo")
    arg = parser.add_argument('--img_path', type=str, help='path to an image to classify')
    args = parser.parse_args()

    device = torch.device("cpu")
    model = torch.load('./model/resnet.pth', map_location=device)


    input_size = 224

    data_transform = transforms.Compose([
        transforms.Resize([input_size, input_size]),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    seasons = {0: 'autumn',
               1: 'spring',
               2: 'summer',
               3: 'winter'}

    image = Image.open(args.img_path)
    image_tensor = data_transform(image).float()
    image_tensor = image_tensor.unsqueeze(0)
    input = image_tensor.to(device)
    output = model(input)

    output = output.data.cpu().numpy()[0]
    index = output.argmax()
    prob = np.exp(output[index]) / sum(np.exp(output))

    print("predicted season is :", seasons[index], "with probability {:.3f}".format(prob, 3))
