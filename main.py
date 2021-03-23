from TxDict import TxDict
from Dictation import Dictation
from Settings import Settings
from functions import *


FUNCS = {
        '1': ['听写单词', start_dictation()],
        '2': ['批量生成单词中文释义', function_2()]
        }

while True:
    show_funcs(FUNCS)
    func_num = get_func_num()