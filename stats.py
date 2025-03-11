def word_count(book):
    words = book.split()
    return len(words)

def char_count(book):
    chars = {}
    for char in book:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    # print(chars)
    return chars

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list