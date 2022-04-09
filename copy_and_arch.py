import os
import shutil
from zipfile import ZipFile
import zipfile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def copy_f(scr, copy_folder):
    """Функция принимает в себя значение источника и
    значение папки: куда следует поместить копии файлов"""
    #Если папка для копий файлов не существует, ее необходимо создать
    if not os.path.exists(copy_folder):
        os.makedirs(copy_folder, exist_ok=True)
    #В цикле перебираем список файлов в источнике
    #и если наименования файлов включают в себя расширение .py то копируем их.
    for i in os.listdir(scr):
        try:
            if i.split('.')[1] == 'py':
                shutil.copy(i, copy_folder)
        except IndexError:
            pass
    return copy_folder

def archive(folder, to_path):
    """Осталось архив дописать"""
    copy_folder = os.path.join(to_path, 'Copy')
    copy_folder = copy_f(folder, copy_folder)
    with zipfile.ZipFile("Archives.zip", mode="w") as archive:
        for root, dirs, files in os.walk(copy_folder):
            for file in files:
                archive.write(file)
    #Удаляем папку с копиями
    shutil.rmtree(copy_folder)

archive(BASE_DIR, BASE_DIR+"/Data")
