import tkinter as tk
from TxDict import TxDict
from Dictation import Dictation
from Settings import Settings
from functions import *


def main():
    settings = Settings()
    dictation = Dictation()

    while True:
        show_funcs(settings.funcs_info)
        index = get_func_index(settings.funcs_info)
        if index == '1':
            dictation_start(dictation, tk, settings)
        elif index == '2':
            exit()


if __name__ == '__main__':
    main()
