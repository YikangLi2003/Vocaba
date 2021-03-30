import json

def revise_wrong_definitions(wd_set_lists, correction_dict):  # {"old word":[new word, new defn]}
    for wd_set in wd_set_lists:
        revised_wds = []
        with open(wd_set, 'r') as set_file:
            content = json.load(set_file)
        for old_word, new in correction_dict.items():
            if old_word in content:
                del content[old_word]
                content[new[0]] = new[1]
                revised_wds.append(old_word)
        with open(wd_set, 'w') as set_file:
            json.dump(content, set_file)
        for w in revised_wds:
            del correction_dict[w]


if __name__ == "__main__":
    lst = ("items.json", "people.json")
    dt = {
        "shopper": ["shit used to be a kid", "孩子屎"],
        "tourist": ["children is shit", "这是屎"],
        "visa": ["visa", "通往自由灯塔的船票"],
        "walking boots": ["local his book", "卑鄙的异乡人"]
    }
    revise_wrong_definitions(lst, dt)