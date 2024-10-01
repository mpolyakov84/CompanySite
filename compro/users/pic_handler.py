from PIL import Image
from flask import current_app

def add_photo(photo,user):
    pic_name = photo.filename
    pic_ext = pic_name.split('.')[-1]
    
    new_name = user.name + '_' + Str(user.id) + pic_ext
    pic_path = url_for(current_app.root_path, static,new_name)
    
    pic = Image.open(photo)
    scale = (200,200)
    pic.tumbnail(scale)
    pic.save(pic_path)
    
    return new_name