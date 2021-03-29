from tkinter import filedialog
import os
import json


def show_funcs(funcs):
    os.system('cls')
    print('=' * 10)
    for k, v in funcs.items():
        print(k + '. ' + v)
    print('=' * 10)


def get_func_index(funcs):
    print('[i] Select with the index: ', end='')
    while True:
        i = input()
        if i in funcs:
            return i


def show_result(score, full_score, mistakes):
    os.system('cls')
    print('{:-^60}'.format('Report'), '\n')
    print('{:^60}'.format('Score: ' + str((100 * (score / full_score))) + ' %'), '\n')

    print('{:-^60}'.format('Incorrect Words'), '\n')
    if not mistakes:
        print("{:^60}".format("None"))
    else:
        for m in mistakes:
            print("{:^60}".format(m))

    print('\n', ('-' * 60))


def get_word_sets(tkinter, settings):
    window = tkinter.Tk()  # 创建tkinter可视化窗口
    window.withdraw()  # 隐藏tk窗口
    sets = filedialog.askopenfilenames(  # 返回包含所选文件绝对路径的元组
        title="Select sets",  # 窗口标题
        filetypes=[('JSON', '.json')],  # 仅能选取json文件
        initialdir=settings.dicts)  # 默认路径
    if sets != '':
        return sets
    else:
        return ()


def get_composed_word_set(tkinter, settings):
    print("[i] Pls select word set(s)")
    word_set_files = get_word_sets(tkinter, settings)
    word_set = {}
    if word_set_files:
        for file in word_set_files:
            with open(file, 'r') as f:
                word_set.update(json.load(f))
    return word_set


def revise_wrong_definitions(wd_set_lists, correction_dict):  # {"old word":[new word, new defn]}
    for wd_set in wd_set_lists:
        with open(wd_set, 'r') as set_file:
            content = json.load(set_file)
        for old_word in correction_dict.keys():
            if old_word in dict:
                new = correction_dict.pop(old_word)
                del content[old_word]
                content[new[0]] = new[1]
        with open(wd_set, 'w') as set_file:
            json.dump(content, set_file)


def dictation_start(dictation, tkinter, settings):
    while True:
        dictation.dcat = get_composed_word_set(tkinter, settings)
        dictation.go_through()
        mistakes = dictation.recovery[:]
        if mistakes:
            for i in range(len(mistakes)):
                mistakes[i] = mistakes[i] + ' - ' + dictation.dcat[mistakes[i]]
        while dictation.recovery:
            dictation.go_through(recovery=True)
        show_result(dictation.score, len(dictation.dcat), mistakes)
        if not input('[?] Start a new round? (y/n): ').lower().startswith('y'):
            break
