import os.path
from PIL import Image
from flask import current_app, url_for
from random import randint

def add_photo(photo,user):
    # delete old image
    img_path = pic_path = os.path.join(current_app.root_path, 'static')
    outdated_name = user.username + '_' + str(user.id)
    print(img_path)
    for root, dirs, files in os.walk(img_path):
        for name in files:
            if outdated_name in name:
                os.remove(os.path.join(root, name))
                print(f'File with name {name} has been deleted')

    # create name for new image
    pic_name = photo.filename
    pic_ext = pic_name.split('.')[-1]
    random_integer = randint(1,999999)
    new_name = user.username + '_' + str(user.id) + '_' + str(random_integer) + '.' + pic_ext
    pic_path = os.path.join(current_app.root_path, 'static', new_name)

    pic = Image.open(photo)
    scale = (200,200)
    pic.thumbnail(scale)
    pic.save(pic_path)
    
    return new_name