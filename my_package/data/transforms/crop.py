#Imports
from PIL import Image
import random

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        self.height = shape[0]
        self.width = shape[1]
        self.crop_type = crop_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        h,w = image.size
        if self.crop_type == 'center':
            left = w/2 - self.width/2
            right = w/2 + self.width/2
            top = h/2 - self.height/2  
            bottom = h/2 + self.height/2
            im1 = image.crop((left,top,right,bottom))
            im1.show()
            return im1
        else:
            x1 = random.randrange(self.width,w-self.width)
            y1 = random.randrange(self.height,h-self.height)
            left = x1 - self.width/2
            right = x1 + self.width/2
            top = y1 - self.height/2  
            bottom = y1 + self.height/2
            im1 = image.crop((left,top,right,bottom))
            
            return im1

 