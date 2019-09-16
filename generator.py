from PIL import Image
import random
import os
images_path = 'images/png/'
body_path = images_path + 'body/'
background_path = images_path + 'background/'
avatar = Image.open(background_path + '/background.png');
for dir in os.listdir(body_path):
    max_number = len(os.listdir(body_path+dir))
    random_number = str(random.randint(1,max_number))
    part = Image.open(body_path+dir+"/"+dir+random_number+".png")
    avatar = Image.alpha_composite(avatar, part)

avatar.save("avatar.png")