def single_root_words(root_word, *other_words):
    same_words = []
    for x in other_words:
        if x.lower() in root_word.lower() or root_word.lower() in x:
            same_words.append(x)
    return same_words
print(single_root_words('leonardo', 'leo', 'nard', 'awdf' ))
print(single_root_words('leo', 'leonardo', 'napoleon', 'owehf'))