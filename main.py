import os
from art import tprint


COUNT_ADDITIONAL_SYMBOLS = 10


# функция находит файлы в директории
def find(find_directory, find_string):
    for root, dirs, files in os.walk(find_directory):
        for name in files:
            find_string_in_file(os.path.join(root, name), find_string)


# функция находит строку в файлах
def find_string_in_file(file, file_string):
    print('[ / ] Обрабатывается файл:', file)
    f = open(file, 'r', encoding='utf-8')
    content = f.read()
    f.close()
    index = content.find(FIND_STRING)
    if index != -1:
        print_find_info(file, content, FIND_STRING)
    else:
        print("[ - ] В данном файле совпадений не обнаружено..")


def print_find_info(file, content, FIND_STRING):
    # вывод файлов где есть совпадение
    print('\n[ + ] Обнаружено совпадение в файле:', file)
    index = content.find(FIND_STRING)
    start_index = index - COUNT_ADDITIONAL_SYMBOLS if index >= COUNT_ADDITIONAL_SYMBOLS else 0
    end_index = index + len(FIND_STRING) + COUNT_ADDITIONAL_SYMBOLS
    content = content[start_index:end_index]
    content = content.replace(FIND_STRING, '\x1b[32;1m' + FIND_STRING + '\x1b[0m')
    print('...', content, '...')

def program_description():
    tprint("S_Finder")
    print("Программа для нахождения слов/строк в файлах..")
    input("Press Enter to continue...")


if __name__ == '__main__':
    tprint("TextFinder")
    DIRECTORY = input("[ + ] Введите путь к папке в которой содержатся файлы для последующего поиска в них: ")
        # r'D:\Documents\x-Code\projects-Python\textFinder\textFiles'
    FIND_STRING = input("[ + ] Введите слово или фразу, которую необходимо найти: ")
    print("\n[ / ] Программа начинает работу..\n")
    find(DIRECTORY, FIND_STRING)
