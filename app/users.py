import os, json
from werkzeug.utils import secure_filename

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.user_folder = self.return_user_folder(user_id=user_id)

    def return_user_folder(user_id):
        user_folder_filepath = os.path.join(app.config['USERS_FOLDER'], user_id)
        return user_folder_filepath

    def make_user_folder(user_id):
        user_folder_filepath = return_user_folder(user_id=user_id)
        try:
            os.mkdir(user_folder_filepath)
        except Exception as e:
            print(e)
        return user_folder_filepath

    def save_json_user_data(user_id, json_user_data, filename_ending='_user_data.json'):
        json_user_data_filepath = os.path.join(return_user_folder(user_id=user_id), user_id + filename_ending)
        with open(json_user_data_filepath, 'w', encoding='utf-8') as file:
            json.dump(json_user_data, file, indent=4, sort_keys=True, default=str)
        return json_user_data_filepath

    def secure_user_email(email):
        email = email.replace('@', '_')
        email = email.replace('.', '_')
        return secure_filename(email)

    def make_json_data(form):
        json_data = {}
        for field in form:
            json_data[field.name] = field.data
        return json_data

    def save_image(user_id):
        pass
            # user_folder = os.path.join(app.config['USERS_FOLDER'], unique_id)


            # face_image_filepath = os.path.join(user_folder, unique_id + '_face_image.jpg')
            # passport_image_filepath = os.path.join(user_folder, unique_id + '_passport_image.jpg')
            
            # face_image_filename = unique_id + '_face_image.jpg'
            # request.files['face_image'].save(os.path.join(user_folder, face_image_filename))
            # passport_image_filename = unique_id + '_passport_image.jpg'
            # request.files['passport_image'].save(os.path.join(user_folder, passport_image_filename))


