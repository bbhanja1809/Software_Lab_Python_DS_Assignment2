#Imports
from my_package.model import ImageCaptioningModel
from my_package.data.dataset import Dataset
from my_package.data.download import Download
from my_package.data.transforms.flip import FlipImage
from my_package.data.transforms.rescale import RescaleImage
from my_package.data.transforms.blur import BlurImage
from my_package.data.transforms.crop import CropImage
from my_package.data.transforms.rotate import RotateImage
import numpy as np
from PIL import Image
import os
from matplotlib import pyplot as plt


def experiment(annotation_file, captioner, transforms, outputs):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        captioner: The image captioner
        transforms: List of transformation classes
        outputs: Path of the output folder to store the images
    '''

    #Create the instances of the dataset, download
    dataset = Dataset(annotation_file,transforms)
    download = Download()

    #Print image names and their captions from annotation file using dataset object
    #Download images to ./data/imgs/ folder using download object    

    length = dataset.__len__()
    for i in range(length):
        data = dataset.__getann__(i)
        fullpath = os.path.join('./data/imgs/',data["file_name"])
        download.__call__(fullpath,data["url"])
        data = dict(data)
        print(f'{data["file_name"]}:')
        for caption in data["captions"]:
            print(caption)
        print()        

    #Transform the required image (roll number mod 10) and save it seperately 
      
    image = dataset.__transformitem__('./data/imgs/5.jpg')
    image.save('./5.jpg','JPEG')


    #Get the predictions from the captioner for the above saved transformed image  
    
    path = './5.jpg'
    caption_num = 8
    caption_generated = captioner.__call__(path,caption_num)
    print("Captions Generated:")
    for i in range(len(caption_generated)):
        print(caption_generated[i])

    # Matplotlib plotting image along with captions
    fig = plt.figure(figsize=(12, 4))
    rows = 1
    cols = 2
    img = Image.open('./5.jpg')
    fig.add_subplot(rows, cols, 1)
    plt.imshow(img)
    plt.axis('off')
    fig.add_subplot(rows,cols,2)
    plt.axis('off')
    plt.title("Generated Captions")
    for i in range(len(caption_generated)):        
        plt.text(0,0.8-0.07*i,caption_generated[i])    

    plt.show()

def main():
    captioner = ImageCaptioningModel()
    experiment('./data/annotations.jsonl', captioner, [FlipImage(), BlurImage(1)], None) # Sample arguments to call experiment()


if __name__ == '__main__':
    main()