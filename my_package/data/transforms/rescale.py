#Imports
from PIL import Image

class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''
        self.output_size = output_size


    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''
        if(len(self.output_size)>1):
            img = image.resize(self.output_size)
        else:
            width, height = img.size
            if(width>height):
                width = width*self.output_size/height
                height = self.output_size
            else:
                height = self.output_size*height/width
                width = self.output_size

            newsize = (width,height)
            img = image.resize(newsize)
            return img