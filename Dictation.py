import random


class Dictation:
    def __init__(self, dic_lst):
        self.dic_lst = dic_lst
        self.incorrect_lst = []

    @staticmethod
    def show_definition(definitions):
        random.shuffle(definitions)
        print('{:-^60}'.format('definition'))
        for d in definitions:
            if len(d) < 60:
                print('{:-^60}'.format(d))
            else:
                print(d)
        print('-' * 60)

    def go_through(self):
        dic_lst = self.dic_lst[:]
        random.shuffle(dic_lst)
        for word, definitions in dic_lst.items():
            self.show_definition(definitions)
            if input("Answer: ") == word:
                print('[INFO] Correct!')
            else:
                print('[INFO] INCORRECT! Answer: ' + word)
                self.incorrect_lst.append(word)
            input()

    def go_through_incorrect_lst(self):
        inc_lst = self.incorrect_lst[:]
        random.shuffle(inc_lst)
        for w in inc_lst:

