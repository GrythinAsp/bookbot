def calculate_num_words(book_text):
    words_list = book_text.split()
    return len(words_list)

def calculate_unique_characters(book_text):
    unique_characters = {}
    words_list = book_text.lower().split()
    for word in words_list:
        for letter in word:
            if letter in unique_characters:
                unique_characters[letter] += 1
            else:
                unique_characters[letter] = 1
    return unique_characters

def get_dict_num_key(dic):
    return dic["num"]

def create_sorted_list_from_dict(dic):
    sorted_list = []
    for key in dic:
        if not key.isalpha():
            continue
        value = dic[key]
        new_dic = {
            "char": key,
            "num": value
        }
        sorted_list.append(new_dic)
    sorted_list.sort(reverse=True, key=get_dict_num_key)
    return sorted_list