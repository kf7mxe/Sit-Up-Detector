import torch
from torch import nn

import numpy as np
from LoadTrainingData import LoadTrainingData
import json


data = LoadTrainingData()
testing = data.getTestingData()
training = data.getTrainingData()
print(training)

print(type(training[0][0][0]))
#trainingTensor = torch.from_numpy(np.array(training))
#testingTensor = torch.from_numpy(np.array(testing))

# Opening JSON file
f = open('C:/Users/kf7mx/Documents/Projects/Sit Up Detector Reps Tracker/training-data/time-freq-1-mil/1-milisecond-1/sitUpData.json', )

# returns JSON object as
# a dictionary
sitUps = json.load(f)

#print(data)
# Iterating through the json
# list
allSitUpsData = []
for sitUp in sitUps:
    sitUpData = []
    for instance in sitUp:
        xyz = [instance['x'],instance['y'],instance['z']]
        sitUpData.append(xyz)
    allSitUpsData.append(sitUpData)

print(allSitUpsData[0][0])
# Closing file
f.close()

# ## Testing and seeing what the tensor has to be to be sent into the network
# import torchvision.datasets as dsets
# import torchvision.transforms as transforms
# DOWNLOAD_MNIST = True
#
# train_data = dsets.MNIST(
#     root='./mnist/',
#     train=True,                         # this is training data
#     transform=transforms.ToTensor(),    # Converts a PIL.Image or numpy.ndarray to
#                                         # torch.FloatTensor of shape (C x H x W) and normalize in the range [0.0, 1.0]
#     download=DOWNLOAD_MNIST,            # download it if you don't have it
# )
# print(type(train_data))
# print(train_data)