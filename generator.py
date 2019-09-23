from PIL import Image
import random
import os

def generate(antennas_category=""):
    path = os.path.dirname(os.path.abspath(__file__))
    images_path = path + '/images/png/'
    background_path = images_path + 'background/'
    body_path = images_path + 'body/'
    antennas_path = images_path + 'antennas/'

    avatar = Image.open(background_path + 'background.png')

    for dir in os.listdir(body_path):
        max_number = len(os.listdir(body_path+dir))
        random_number = str(random.randint(1,max_number))
        part = Image.open(body_path+dir+"/"+dir+random_number+".png")
        avatar = Image.alpha_composite(avatar, part)

    if (antennas_category != ""):
        max_number = len(os.listdir(antennas_path+antennas_category))
        random_number = str(random.randint(1,max_number))
        part = Image.open(antennas_path+antennas_category+"/"+antennas_category+random_number+".png")
        avatar = Image.alpha_composite(avatar, part)

    return avatar