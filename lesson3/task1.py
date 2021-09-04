import os


def get_name(path: str):
    return os.path.splitext(os.path.basename(path))[0]


if __name__ == '__main__':
    file_name = '/home/test. name - book.mp3'
    print(f'{file_name}\t\t{get_name(file_name)}')