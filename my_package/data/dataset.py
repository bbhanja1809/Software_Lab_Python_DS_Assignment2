#Imports
import jsonlines
from PIL import Image
import os
import numpy as np
from my_package.data.transforms import blur,crop,flip,rescale,rotate

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms=None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self.annotation_file = annotation_file
        self.transforms_list = transforms

    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        file = jsonlines.open(self.annotation_file,mode='r')
        lines = 0
        for data in file:
            lines += 1
            
        return lines    

    
    def __getann__(self, idx):
        '''
            return the data items for the index idx as an object
        '''
        read = jsonlines.open(self.annotation_file)
        data_reader = list(read)
        object = data_reader[idx]
        
        return object

    def __transformitem__(self, path):
        '''
            return transformed PIL Image object for the image in the given path
        '''
        image = Image.open(path)
        for transform in self.transforms_list:
            image = transform.__call__(image)
        return image

                

