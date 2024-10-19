def single_root_words(root_word, *other_words):
    same_words = []
    for x in other_words:
        if x in root_word:
            same_words.append(x)
            print(same_words)
single_root_words('leonardo', 'leo', 'nard', 'awdf' )
single_root_words('leo', 'leonardo')