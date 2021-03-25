import tkinter as tk
from TxDict import TxDict
from Dictation import Dictation
from Settings import Settings
from functions import *


def main():
    # 实例化各个对象
    settings = Settings()
    dictation = Dictation()

    while True:
        show_funcs(settings.funcs_info)  # 列出支持的操作
        index = get_func_index(settings.funcs_info)  # 获取用户提供的操作序号
        # 判断序号 执行对应的操作
        if index == '1':
            dictation_start(dictation, tk, settings)
        elif index == '2':
            exit()


if __name__ == '__main__':
    main()
