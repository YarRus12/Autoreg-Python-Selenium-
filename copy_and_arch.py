import os
import shutil
import zipfile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def copy_f(scr, dest):
    for i in scr:
        if i.split('.')[1] == 'py':
            shutil.copytree(i, dest+'/Data/Copy')


def archive(folder, to_path):
    """Нужно будет доработать"""
    mail_zip = zipfile.ZipFile(BASE_DIR, 'w')
    for folder, subfolders, files in os.walk(folder):
        for file in files:
                mail_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), to_path),
                                  compress_type=zipfile.ZIP_DEFLATED)

copy_f(BASE_DIR, BASE_DIR+"/Data/Copy")
#archive(BASE_DIR+"/Data/Copy", BASE_DIR+"/Data/Archives")
