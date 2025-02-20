def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
        # print(char_count(file_contents.lower()))
        create_report(file_contents.lower())

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

def create_report(book): 
    words = word_count(book)
    print("---Report of book---")
    print(f"{words} words found in the book file")
    chars = char_count(book)
    all_chars = []
    for char in chars:
        all_chars.append({"char":char, "num":chars[char]})
    all_chars.sort(reverse=True, key=sort_on)
    for line in all_chars:
        if line['char'].isalpha():
            print(f"The '{line['char']}' character was found {line['num']} times.")
    # print(all_chars)
    print("---End of report---")

# You can use a string's .isalpha() method to check if a string only contains characters from the alphabet.

main()