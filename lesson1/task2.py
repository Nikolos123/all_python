"""
Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):
\"""
Функция принимает имя каталога и распечатывает его содержимое в виде «путь и имя файла», а также любые другие файлы во
вложенных каталогах.
\"""
Эта функция подобна os.walk. Использовать функцию os.walk нельзя. Данная задача показывает ваше умение работать с
вложенными структурами.
"""
import os



def dir(path):

    if os.path.isdir(path):
        content = os.listdir(path)
        for name in content:
            filepath = os.path.join(path, name)
            if not os.path.isdir(filepath):
                print(filepath)
            else:
                dir(filepath)


if __name__ == '__main__':
    dir('/etc/home/nik/document/')