import sys
from stats import word_count
from stats import count_chars
from stats import sort_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    text = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(text)} total words")

    counts = count_chars(text)
    sorted_chars = sort_char_counts(counts)

    print("--------- Character Count -------")
    for item in sorted_chars:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    print("============= END ===============")
main()