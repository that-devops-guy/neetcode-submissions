def get_longer_word(word1: str, word2: str) -> str:
    len1 = len(word1)
    len2 = len(word2)

    max_len = max(len1,len2)

    if max_len == len1:
        return word1
    elif max_len == len2:
        return word2
    else:
        return word1




# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
