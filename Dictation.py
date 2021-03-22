import random


class Dictation:
    def __init__(self, dcat):
        self.dcat = dcat  # 作为听写内容的词典 {'hello':['i:喂,欸,你好,哎', 'v:你好']}
        self.mistakes = []  # 存储听写过程中拼写错误的单词

    @staticmethod  # 传入单词释义列表 格式化输出
    def show_definition(definitions):
        random.shuffle(definitions)
        print('{:-^60}'.format('definition'))
        for d in definitions:
            if len(d) < 60:
                print('{:-^60}'.format(d))
            else:
                print(d)
        print('-' * 60)

    # 听写流程
    def go_through(self, mistakes=False):
        # mistake布尔值参数 是否单独听写上次拼写错误的单词
        words = []
        if mistakes:
            words = self.mistakes[:]
            self.mistakes = []  # 清空错记录用来存储新的错误
        else:
            for k in self.dcat.keys():
                words.append(k)
        random.shuffle(words)

        for word in words:
            self.show_definition(self.dcat[word])
            print("Process:", str((words.index(word)) + 1) + '/' + str(len(words)))
            if input("Answer: ") == word:
                print('[√] Correct!')
            else:
                print('[×] INCORRECT! Answer: ' + word)
                self.mistakes.append(word)
