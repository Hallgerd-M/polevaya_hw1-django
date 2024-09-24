import os

def root_join(*parts):
    """ Функция которая возвращает полный путь к файлу """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_dir, *parts)
    return full_path

#path = root_join("src.contacts.html")
#print(path)