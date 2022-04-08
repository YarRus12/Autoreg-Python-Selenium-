import os
import shutil
import zipfile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def copy_f(scr, dest):

    for i in os.listdir(scr):
        """Проблема в том что паки копия не существует, чтобы ее решить нужно найти фрагмент кода в котором
        мы проверяем наличие папки и если ее нет, то создаем"""
        try:
            if i.split('.')[1] == 'py':
                shutil.copy(i, dest+i)
        except IndexError:
            pass


def archive(folder, to_path):
    """Нужно будет доработать"""
    mail_zip = zipfile.ZipFile(BASE_DIR, 'w')
    for folder, subfolders, files in os.walk(folder):
        for file in files:
                mail_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), to_path),
                                  compress_type=zipfile.ZIP_DEFLATED)

copy_f(BASE_DIR, BASE_DIR+"/Data/")
#archive(BASE_DIR+"/Data/Copy", BASE_DIR+"/Data/Archives")
