import os

directory_path = "Databases"
if not os.path.exists(directory_path):
    os.makedirs(directory_path)
databases = os.listdir(directory_path)
