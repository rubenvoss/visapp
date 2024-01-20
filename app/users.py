import os, json
from werkzeug.utils import secure_filename

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
        self.save_image()
    
    def make_user_folder(self):
        try:
            os.mkdir(self.user_folder_filepath)
        except Exception as e:
            print(e)

    def make_json_user_data(self):
        json_data = {}
        for field in self.form:
            json_data[field.name] = field.data
        self.json_user_data = json_data
        return json_data

    def save_json_user_data(self, filename_ending='_user_data.json'):
        json_user_data_filepath = os.path.join(self.user_folder_filepath, self.user_id + filename_ending)
        with open(json_user_data_filepath, 'w', encoding='utf-8') as file:
            json.dump(self.json_user_data, file, indent=4, sort_keys=True, default=str)
        return json_user_data_filepath

    def convert_image(self):
        pass

    def save_image(self, filename_ending='_image.jpg'):
            face_image_filepath = os.path.join(self.user_folder_filepath, self.user_id + filename_ending)    
            self.form.face_image.data.save(face_image_filepath)
            return face_image_filepath