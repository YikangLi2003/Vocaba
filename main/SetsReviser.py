import json


class SetsReviser:
    def __init__(self):
        self.sets = ()
        self.correction_words = {}

    def revise_wrong_definitions(self):  # {"old word":[new word, new defn]}
        for wd_set in self.sets:  # 遍历可能包含待改正的单词的词表
            revised_wds = []  # 已改正的单词
            with open(wd_set, 'r') as set_file:
                content = json.load(set_file)  # 打开并读取json
            for old_word, new in self.correction_words.items():  # 遍历需改正的单词字典
                if old_word in content:  # 存在于此词组中
                    del content[old_word]  # 删除旧内容
                    content[new[0]] = new[1]  # 添加新内容
                    revised_wds.append(old_word)  # 添加此词至已改正的单词列表
            with open(wd_set, 'w') as set_file:
                json.dump(content, set_file)  # 清空原词典内容 写入已修正的新内容
            for w in revised_wds:
                #  将已修正的单词从待改正词表中移除
                del self.correction_words[w]

    def get_revise_words():
        print("[i] Input problematical word(s) and it's new spelling/definition.")
        words = {}
        while True:
            word = input("[>] ").split(',')
            if len(word) != 3:
                if word[0] == 'c':
                    return {}
                elif word[0] == 'ok':
                    return words
                elif word[0] == 'h':
                    # org_word,new_speeling,new_definition
                    print("[i] Format: problem word, correct spelling, correct definition")
                    print("    Eg. helooo, hello, Здравствыйте")
                    print("    Eg. nice,, красивый")
                    continue
                else:
                    print("[×] Fail to identify terms with wrong format. Type 'h' for more info.")
                    continue
            if word[1] == '':
                word[1] = word[0]
            words[word[0].strip()] = [word[1].strip(), word[2].strip()]

    def revise_sets(tkinter, settings):
        sets = get_word_sets(tkinter, settings)
        revise_wds = get_revise_words()
        revise_wrong_definitions(sets, revise_wds)
