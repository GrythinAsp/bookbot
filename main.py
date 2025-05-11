from stats import (
    calculate_num_words,
    calculate_unique_characters,
    create_sorted_list_from_dict
)
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = calculate_num_words(book_text)
    unique_characters = calculate_unique_characters(book_text)
    sorted_list = create_sorted_list_from_dict(unique_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        filepath_contents = f.read()
    return filepath_contents

main()