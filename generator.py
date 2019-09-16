from PIL import Image
import random
import os

images_path = 'images/png/'
background_path = images_path + 'background/'
body_path = images_path + 'body/'
antennas_path = images_path + 'antennas/'
antennas_category = '2antennas'

avatar = Image.open(background_path + '/background.png')

for dir in os.listdir(body_path):
    max_number = len(os.listdir(body_path+dir))
    random_number = str(random.randint(1,max_number))
    part = Image.open(body_path+dir+"/"+dir+random_number+".png")
    avatar = Image.alpha_composite(avatar, part)

max_number = len(os.listdir(antennas_path+antennas_category))
random_number = str(random.randint(1,max_number))
part = Image.open(antennas_path+antennas_category+"/"+antennas_category+random_number+".png")
avatar = Image.alpha_composite(avatar, part)

avatar.save("avatar.png")