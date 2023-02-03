

import os
import exifread
from PIL import Image
#path = "C://Users//Umer//Desktop//imgs" (path to the folder)

def tiff_to_jpeg(input_folder, output_folder):
    for file in os.listdir(input_folder):
        if file.endswith(".tif"):
            file_path = os.path.join(input_folder, file)
            with open(file_path, 'rb') as f:
                tags = exifread.process_file(f)
            image = Image.open(file_path)
            image.mode = 'I'
            image.point(lambda i:i*(1./256)).convert('L').save('C://Users//Umer//Desktop//imgs//'+file+'.jpg')
            

# Get the list of all files and directories

tiff_to_jpeg(path,path)






