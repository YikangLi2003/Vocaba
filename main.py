from TxDict import TxDict
from functions import *

APIKEY = '1dec8cb373f09df013042e4d5e8c21ef'
FUNCS = {
    '1': ['听写单词', function_1()]
    '2': ['批量生成单词中文释义', function_2()]
    }

while True:
    func_num = get_func_num()