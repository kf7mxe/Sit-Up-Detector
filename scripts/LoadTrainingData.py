import json
import os
import random
import numpy as np

# Opening JSON file
class LoadTrainingData:
    def __init__(self):
        pass
    def load1Data(self):
        dirPath = "C:/Users/kf7mx/Documents/Projects/Sit Up Detector Reps Tracker/training-data/time-freq-1-mil/1-milisecond-1"
        self.fileList = []
        self.trainingList = []
        self.testingList = []
        for root, dirs, files in os.walk(dirPath):
            for file in files:
                #append the file name to the list
                self.fileList.append(os.path.join(root,file))


        self.allSitUpsData = []
        for filePath in self.fileList:
            file = open(filePath)
            jsonFromFile = json.load(file)
            for sitUp in jsonFromFile:
                sitUpData = []
                for instance in sitUp:
                    xyz = [float(instance['x']), float(instance['y']), float(instance['z'])]
                    sitUpData.append(xyz)
                self.allSitUpsData.append(np.array(sitUpData))
        random.shuffle(self.allSitUpsData)

        sizeOfTrainingSet = self.allSitUpsData.__len__()
        sizeOfTestingSet = int(sizeOfTrainingSet*0.10)
        sizeOfTrainingSet = sizeOfTrainingSet -sizeOfTestingSet
        for i in range(0,sizeOfTestingSet):
            self.testingList.append(self.allSitUpsData[i])
        for i in range(sizeOfTestingSet,sizeOfTrainingSet):
            self.trainingList.append(self.allSitUpsData[i])
# print(allSitUpsData)
# print(allSitUpsData[0][0])

    def getTrainingData(self):
        return self.trainingList


    def getTestingData(self):
        return self.testingList





# firstFilePath = open('C:/Users/kf7mx/Documents/Projects/Sit Up Detector Reps Tracker/training-data/time-freq-1-mil/1-milisecond-1/sitUpData.json', )
# firstFilePath = open(fileList[0], )
#
# # returns JSON object as
# # a dictionary
# jsonFile1 = json.load(firstFilePath)
# #jsonFile2 = json.load(firstFilePath)
#
#
# #print(data)
# # Iterating through the json
# # list
# allSitUpsData = []
# for sitUp in jsonFile1:
#     sitUpData = []
#     for instance in sitUp:
#         xyz = [instance['x'],instance['y'],instance['z']]
#         sitUpData.append(xyz)
#     allSitUpsData.append(sitUpData)
#
# print(allSitUpsData[0][0])
# # Closing file
# #jsonFile1.close()
#
# with open('combinedData.json','w') as file :
#     json.dump(allSitUpsData,file)