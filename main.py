import sys
from stats import *

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    file_contents = get_text(path)
    # print(file_contents)
    # print(char_count(file_contents.lower()))
    create_report(path, file_contents.lower())

def get_text(path):
    with open(path) as f:
        return f.read()
    
def create_report(path, book): 
    words = word_count(book)
    print("---Report of book---")
    print(f"Analyzing book found at {path}:")
    print("----------- Word Count ----------")
    print(f"{words} words found in the document")
    chars = char_count(book)
    all_chars = []
    for char in chars:
        all_chars.append({"char":char, "num":chars[char]})
    all_chars.sort(reverse=True, key=sort_on)
    print("--------- Character Count -------")
    for line in all_chars:
        if line['char'].isalpha():
            print(f"{line['char']}: {line['num']}")
    # print(all_chars)
    print("---End of report---")

# You can use a string's .isalpha() method to check if a string only contains characters from the alphabet.

main()