"""Users module for the Flask app, handles backend"""
import os
import json
from werkzeug.utils import secure_filename
from PIL import Image
from pillow_heif import register_heif_opener

class User:
    def __init__(self, flask_config, form):
        self.email = form.email.data
        self.user_id = secure_filename(self.email.replace('@', '_').replace('.', '_'))
        self.flask_config = flask_config
        self.user_folder_filepath = os.path.join(self.flask_config['USERS_FOLDER'], self.user_id)
        self.form = form
        self.make_user_folder()
        self.json_user_data = {}
        self.make_json_user_data()
        self.save_json_user_data()
        self.convert_image()

    def make_user_folder(self):
        try:
            os.mkdir(self.user_folder_filepath)
        except FileExistsError as e:
            print(e)

    def make_json_user_data(self):
        json_data = {}
        for field in self.form:
            json_data[field.name] = field.data
        self.json_user_data = json_data
        return json_data

    def save_json_user_data(self, filename_ending='_user_data.json'):
        json_filepath = os.path.join(self.user_folder_filepath, self.user_id + filename_ending)
        with open(json_filepath, 'w', encoding='utf-8') as file:
            json.dump(self.json_user_data, file, indent=4, sort_keys=True, default=str)
        return json_filepath

    def convert_image(self, filename_ending='_image.jpg'):
        register_heif_opener()
        image = Image.open(self.form.face_image.data)
        image.convert('RGB')
        image.thumbnail((1000,1000))
        self.image_filepath = os.path.join(self.user_folder_filepath, self.user_id +filename_ending)
        image.save(self.image_filepath, optimize=True, quality=85)
        return image
