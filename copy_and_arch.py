import os
from shutil import copyfile, copy

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


copy(__file__, destdir)  # копируем в указанную директорию
copyfile(__file__, os.path.join(destdir, filename))  # копируем по полному пути нового расположения


def copy(scr, dest):
    shutil.copytree(scr, dest+'/Data/Archives')

def archive(from_path, to_path):
    pass

