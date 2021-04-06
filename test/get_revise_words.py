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



if __name__ == "__main__":
    print(get_revise_words())