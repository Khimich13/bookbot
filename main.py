import sys
from stats import count_words
from stats import count_chars
from stats import sort_counted_chars
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        raise sys.exit(1)
    book_path = f"{sys.argv[1]}"
    full_path = f"/home/khimich13/bookbot/{book_path}"
    text = get_book_text(full_path)
    word_count = count_words(text)
    chars_count = count_chars(text)
    sorted_counted_chars = sort_counted_chars(chars_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_counted_chars:
        character = item["char"]
        if character.isalpha():
            print(f"{character}: {item["num"]}")
    print("============= END ===============")
main()