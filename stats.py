def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    char_count = {}
    text = text.lower()
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_on(dict):
    return dict["num"]

def sort_dict_of_char(char_dict):
    #char_dict = char_dict.sort()
    char_list = []
    for k,v in char_dict.items():
        char_list.append({"char": k, "num": v})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    