import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader


# defining the Dataset class
class data_set(Dataset):
    def __init__(self,trueTrainingSet,falseTrainingSet,trueTestingSet,falseTestingSet):
        self.trueTrainingSet = trueTrainingSet
        self.falseTrainingSet = falseTrainingSet
        self.trueTestingSet = trueTestingSet
        self.falseTrainingSet = falseTestingSet
        #numbers = list(range(0, 100, 1))
        #self.data = numbers

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):

        return self.data[index]
