class Settings:
    def __init__(self):
        # 此类仅用于存储配置参数
        self.apikey = '1dec8cb373f09df013042e4d5e8c21ef'  # 调用API所需的key
        self.dicts = './dicts'  # 词库路径
        self.funcs_info = {  # 功能列表
            '1': '听写单词',
            '2': '退出'
        }
