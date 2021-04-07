import json
import os

def show_words(sets):
    sets = list(sets)
    for set in sets:
        print("{:-^61}".format(os.path.basename(set)))
        with open(set, 'r') as fileobj:
            content = json.load(fileobj)
        for w, d in content.items():
            if str(type(d)) == "<class 'list'>":
                d = ' '.join(d)
            print("{:^30} {:^30}".format(w, str(d)))
        print('\n')

sets = ["people.json", "items.json"]
show_words(sets)