import os


def consolidate_all_txt_files_in_dir(directory: str = '.') -> dict:
    files_list = os.scandir(directory)
    files_dict = {}
    for item in files_list:
        path = str(item.name)
        if path.split('.')[-1] == 'txt' and path != 'sorted_files.txt':
            with open(item.name, 'r', encoding='utf-8') as file:
                file_body = file.readlines()
                files_dict[(len(file_body)), item.name] = file_body
    return files_dict


def write_sorted_files(dict_of_files: dict):
    sorted_keys = sorted(dict_of_files.keys())
    with open('sorted_files.txt', 'w', encoding='utf-8') as file:
        for key in sorted_keys:
            file.writelines(key[1] + '\n')
            file.writelines(str(key[0]) + '\n')
            for i in range(key[0]):
                file.write(str(dict_of_files[key][i]))
            file.writelines('\n')
    return True


write_sorted_files(consolidate_all_txt_files_in_dir())
