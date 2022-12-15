# image compressor
from PIL import Image
import matplotlib.pyplot as plt
from  tqdm import tqdm
import glob
import os


# image path
image_path = './images/2022/'
save_path = './images_compressed/2022/'
if  not os.path.exists(save_path):
    os.makedirs(save_path)

# get all images
for folder in glob.glob(image_path + '*'):
    # image = folder + '/' + os.listdir(folder)[0]
    image = folder+'/'+'01.jpg'
    img_id = folder.split('/')[-1].split('\\')[-1]
    # open image
    img = Image.open(image)
    # resize to max width 500 
    ratio = 500 / img.size[0]
    img = img.resize((500, int(img.size[1] * ratio)), Image.ANTIALIAS)
    # mkdir
    img_save_path = save_path + img_id + '/'
    if not os.path.exists(img_save_path):
        os.makedirs(img_save_path)
    img_save_path = img_save_path + '01.jpg'
    # print(img_save_path)
    # save image to new path but lower quality (compressed)
    img.save(img_save_path, format='JPEG', quality=80)
    # plt.imsave(img_save_path, img, format='jpg', quality=50)
