from PIL import Image
import random
import os

path = 'images/png/'
avatar = Image.open('images/template.png');
for dir in os.listdir(path):
    max_number = len(os.listdir(path+dir))
    random_number = str(random.randint(1,max_number))
    part = Image.open(path+"/"+dir+"/"+dir+random_number+".png")
    avatar = Image.alpha_composite(avatar, part)

avatar.save("avatar.png")