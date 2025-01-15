import os
import shutil


downloads_folder = "C:/Users/rhssr/Downloads"

file_types = {
    'Images': ['jpg', 'jpeg', 'png', 'gif'],
    'Documents': ['pdf', 'docx', 'xlsx', 'txt'],
    'Videos': ['mp4', 'mkv', 'avi'],
    'Archives': ['zip', 'rar', '7z'],
    'Software': ['exe', 'msi']
}

for category in file_types.keys():
    folder_path = os.path.join(downloads_folder, category)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for filename in os.listdir(downloads_folder):
    if os.path.isfile(os.path.join(downloads_folder, filename)):
        file_extension = filename.split('.')[-1].lower()
        for category, extensions in file_types.items():
            if file_extension in extensions:
                source_path = os.path.join(downloads_folder, filename)
                destination_path = os.path.join(downloads_folder, category, filename)
                shutil.move(source_path, destination_path)
                print(f"Moved {filename} to {category}")
                break
