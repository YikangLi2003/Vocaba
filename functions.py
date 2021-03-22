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

