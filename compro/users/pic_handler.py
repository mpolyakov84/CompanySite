import os.path
from PIL import Image
from flask import current_app, url_for

def add_photo(photo,user):
    pic_name = photo.filename
    pic_ext = pic_name.split('.')[-1]
    
    new_name = user.name + '_' + str(user.id) + pic_ext
    pic_path = os.path.join(current_app.root_path, 'static', new_name)
    print(new_name)
    print(pic_path)
    pic = Image.open(photo)
    scale = (200,200)
    pic.thumbnail(scale)
    pic.save(pic_path)
    
    return new_name