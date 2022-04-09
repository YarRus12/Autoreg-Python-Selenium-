import os
import shutil
from zipfile import ZipFile
import zipfile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def copy_f(scr, copy_folder):
    """Нужно будет доработать"""
    if not os.path.exists(copy_folder):
        os.makedirs(copy_folder, exist_ok=True)
    for i in os.listdir(scr):
        try:
            if i.split('.')[1] == 'py':
                shutil.copy(i, copy_folder)
        except IndexError:
            pass

def trash_f(folder):
    trash_folder = os.path.join(folder, 'Trash')
    if not os.path.exists(trash_folder):
        os.makedirs(trash_folder, exist_ok=True)

def archive(folder, to_path):
    """Осталось архив дописать"""
    copy_folder = os.path.join(to_path, 'Copy')
    #copy_f(folder, copy_folder)
    archive_folder = os.path.join(to_path, 'Archives')
    ziph = zipfile.ZipFile("Archives.zip", 'w')
    for root, dirs, files in os.walk(to_path):
        for file in files:
            ziph.write(os.path.join(copy_folder, file), arcname=archive_folder)
    ziph.close()

archive(BASE_DIR, BASE_DIR+"/Data")
