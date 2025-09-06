from stats import get_num_words, get_count_char, sorted_list
import sys
def get_book_text(path):
    with open(path) as f:
        text = f.read()
        return text

def main():
    print("============ BOOKBOT ============")

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print(f"Analyzing book found at {sys.argv[1]}...")

    book_text = get_book_text(sys.argv[1])

    print("----------- Word Count ----------")
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

    char_counts = get_count_char(book_text)
    chars = sorted_list(char_counts)

    print("--------- Character Count -------")
    for item in chars:
        print(f"{item['char']}: {item['num']}")
        
    print("============= END ===============")

main()