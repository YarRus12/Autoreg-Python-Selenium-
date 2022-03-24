import os
from shutil import copyfile, copy
import zipfile


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


copy(__file__, destdir)  # копируем в указанную директорию
copyfile(__file__, os.path.join(destdir, filename))  # копируем по полному пути нового расположения


def copy(scr, dest):
    shutil.copytree(scr, dest+'/Data/Copy')

def archive(folder, to_path):
    """Нужно будет доработать"""
    mail_zip = zipfile.ZipFile(BASE_DIR, 'w')
    for folder, subfolders, files in os.walk(folder):
        for file in files:
                mail_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), to_path),
                                  compress_type=zipfile.ZIP_DEFLATED)
archive(BASE_DIR+"/Data/Copy", BASE_DIR+"/Data/Archives")
