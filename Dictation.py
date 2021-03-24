import random
import time
import os


class Dictation:
    def __init__(self, dcat=None):
        if dcat is None:
            dcat = {}
        self.dcat = dcat  # 作为听写内容的词典 {'hello':['i:喂,欸,你好,哎', 'v:你好'], 'cookie':'n:饼干'}
        self.recovery = []  # 存储听写过程中拼写错误的单词
        self.score = 0

    @staticmethod  # 传入单词释义列表 格式化输出
    def show_definition(defin, recovery):
        os.system('cls')
        if recovery:
            print('{:-^60}'.format('Recovery'), '\n')
        else:
            print('{:-^60}'.format('Definition'), '\n')

        if str(type(defin)) == "<class 'str'>":
            print('{:^60}'.format(defin))
        elif str(type(defin)) == "<class 'list'>":
            for d in defin:
                if len(d) < 60:
                    print('{:^60}'.format(d))
                else:
                    print(d)

        print('\n' + ('-' * 60))

    def get_wordlist(self, recovery):
        if recovery:
            # recovery为True代表纠错模式 听写上次拼写出错的单词
            words = self.recovery[:]
            self.recovery = []  # 清空错记录用来存储新的错误
        else:
            words = []
            for k in self.dcat.keys():
                words.append(k)

        random.shuffle(words)
        return words

    # 听写流程
    def go_through(self, recovery=False):
        if not self.dcat:
            return None

        words = self.get_wordlist(recovery)  # 将要听写的词表
        if not recovery:
            self.score = len(words)

        for word in words:
            self.show_definition(self.dcat[word], recovery)  # 列出释义
            print("Process:", str((words.index(word)) + 1) + '/' + str(len(words)))  # 显示进度
            answer = input("Answer: ")
            if answer == word or answer == '$':
                # 答案正确
                print('[√] Correct!')
                time.sleep(0.5)
            elif answer == '*':
                self.recovery = []
                self.score = 0
                break
            else:
                # 答案错误
                print('[×] INCORRECT! Answer: ' + word)
                self.recovery.append(word)  # 显示答案 记录错词
                if not recovery:
                    self.score -= 1
                input("[i] Press 'enter' to continue...")