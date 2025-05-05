from stats import count_words, count_characters, sort_dict_of_char
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def print_report(book, words, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for dict in char_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")


def main():
    #book = "books/frankenstein.txt"
    #print(sys.argv)
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
        book_text = get_book_text(book)
        num_words = count_words(book_text)
        num_chars = count_characters(book_text)
        char_list = sort_dict_of_char(num_chars)
        print_report(book, num_words, char_list)


main()