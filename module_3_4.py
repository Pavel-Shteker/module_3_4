def single_root_words(root_word, *other_words): # первое слово неизменно, остальные неограниченны
    same_words = []
    root_word_lower = root_word.lower()

    for checking in other_words:
        word_lower = checking.lower()
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(checking) # условие для добавления
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

