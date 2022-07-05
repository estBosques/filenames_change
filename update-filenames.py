import shutil
import os

BASE_DIR = '/Users/estbosqu/Downloads/icons_100x100/'
files_to_modify = os.listdir(BASE_DIR)

for file in files_to_modify:
  new_name = file.replace(' .png', '.png')
  new_name = new_name.split('. ')[1]
  shutil.move(BASE_DIR+file, BASE_DIR+new_name)

if __name__ == "__main()__":
  rename_file()