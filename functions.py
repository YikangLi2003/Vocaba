from Dictation import *


def show_funcs(funcs):
    print('=' * 10)
    for k, v in funcs.items():
        print(k + '. ' + v)
    print('=' * 10)


def get_func_num(funcs):
    print('[INPUT] 输入要执行的操作的编号')
    while True:
        num = input('>>> ')
        if num in funcs:
            return num


def start_dictation(*dicts):
    dic = Dictation()
    for d in dicts:
        dic.dcat.update(d)
    dic.go_through()
    while dic.recovery:
        dic.go_through(recovery=True)
    print('[i]', 'Dictation finished. Score:', (100 * (dic.score / len(dic.dcat))), '%')


def dictation_guide(dicts_path):
    print("[INPUT] Select word sets for dictation with numbers (split with a blank)")
    org_path = os.getcwd()
    while True:
        objects = os.listdir(dicts_path).append("go back")
        for i in range(len(objects)):
            print(str(i) + '.', objects[i])




#dictation({'hello': ['i:喂,欸,你好,哎', 'v:你好'], 'cookie': 'n:饼干', 'shit': ['n:屎,粪便', 'v:拉屎']})
