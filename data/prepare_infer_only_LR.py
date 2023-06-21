import os
import argparse
from PIL import Image

def upsample_bicubic(input_path):
    
    imgs_list = os.listdir(input_path)
    image = Image.open(input_path+'/'+imgs_list[0])
    width, height = image.size
    new_width = width * 4
    new_height = height * 4
    
    directory, filename = os.path.split(input_path)
    
    output_path_hr = directory+'/hr_'+str(width)
    output_path_sr = directory+'/sr_'+str(width)+'_'+str(width*4)
    
    os.makedirs(output_path_hr)
    os.makedirs(output_path_sr)
    
    counter = 0
    for i in imgs_list:
        image = Image.open(input_path+'/'+i)

        upsampled_image = image.resize((new_width, new_height), resample=Image.BICUBIC)

        upsampled_image.save(output_path_hr+'/'+str(counter)+'.png', format='PNG')
        upsampled_image.save(output_path_sr+'/'+str(counter)+'.png', format='PNG')
        
        counter +=1
    print("Data prepared for inference")
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('input_path', type=str, help='Absolute path to the input directory. The other folders will be saved in the same parent directory.')

    args = parser.parse_args()

    upsample_bicubic(args.input_path)