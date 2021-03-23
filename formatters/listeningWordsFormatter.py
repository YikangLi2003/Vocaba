import os
import json

DICTS = "../dicts/ListeningSceneWords"  # 格式化后的词典储存路径
ORIGINAL_WORDS = "./ListeningSceneWords"  # 原始单词列表的路径
PACKAGES = os.listdir(ORIGINAL_WORDS)  # 单词包的路径列表


def remove_y(line):
    return line[2:]


def split_word_defn(line):
    word = "".join(i for i in line if ord(i) < 256).strip()
    defn = "".join(i for i in line if ord(i) > 256).strip()
    return {word: defn}


def prep_packages_dirs(dicts, packages):
    for p in packages:
        try:
            os.mkdir(dicts + '/' + p)
        except FileExistsError:
            print("[!] Cannot make dir:", dicts + '/' + p, "already exist.\n")


def paths(original_words, dicts, packages):
    wdlst_paths = []
    dict_paths = []
    for package in packages:
        word_lists = os.listdir(original_words + '/' + package)
        for word_list in word_lists:
            wdlst_paths.append("/".join([original_words, package, word_list]))
            dict_paths.append("/".join([dicts, package, os.path.splitext(word_list)[0] + '.json']))
    return zip(wdlst_paths, dict_paths)


def get_formatted_wdlist(wdlst_path):
    temp_dict = {}
    with open(wdlst_path, 'r', encoding='utf-8') as wdlst:
        for line in wdlst.readlines():
            temp_dict.update(split_word_defn(remove_y(line)))
    return temp_dict


def dump_dict(dict_path, content):
    if os.path.exists(dict_path):
        print("[!] Cannot write dictionary data, file already exists.")
    else:
        with open(dict_path, 'w') as dict_file:
            json.dump(content, dict_file)


def main():
    prep_packages_dirs(DICTS, PACKAGES)
    for (word_lst, dict_path) in paths(ORIGINAL_WORDS, DICTS, PACKAGES):
        print("Word list:", word_lst)
        dump_dict(dict_path, get_formatted_wdlist(word_lst))
        print("Dictionary:", dict_path, '\n')


if __name__ == '__main__':
    main()
