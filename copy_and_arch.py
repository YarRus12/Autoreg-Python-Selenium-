import os
import shutil
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
    return copy_folder

def trash_f(folder):
    trash_folder = os.path.join(folder, 'Trash')
    if not os.path.exists(trash_folder):
        os.makedirs(trash_folder, exist_ok=True)
    return trash_folder

def archive(folder, to_path):
    """Осталось архив дописать"""
    copy_folder = os.path.join(to_path, 'Copy')
    copy_folder = copy_f(folder, copy_folder)
    trash_folder = trash_f(folder)
    #mail_zip = zipfile.ZipFile(BASE_DIR, 'w')
    #for folder, subfolders, files in os.walk(folder):
    #    for file in files:
    #            mail_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), to_path),
    #                              compress_type=zipfile.ZIP_DEFLATED)
    shutil.move(copy_folder, trash_folder)


archive(BASE_DIR, BASE_DIR+"/Data")
