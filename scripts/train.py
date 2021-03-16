import torch
from torch import nn

import numpy as np
from LoadTrainingData import LoadTrainingData
from CustomDataLoader import data_set
import json


data = LoadTrainingData('C:/Users/kf7mx/Documents/Projects/Sit Up Detector Reps Tracker/training-data/time-freq-1-mil/1-milisecond-1','C:/Users/kf7mx/Documents/Projects/Sit Up Detector Reps Tracker/training-data/time-freq-1-mil/1-milisecond-0')
testingTrue = data.getTestingTrueData()
trainingTrue = data.getTrainingTrueData()
testingFalse = data.getTestingFalseData()
trainingFalse = data.getTrainingFalseData()

dataLoader = data_set(trainingTrue,trainingFalse,testingTrue,testingFalse)


# print(training)

# print(type(training[0][0][0]))





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