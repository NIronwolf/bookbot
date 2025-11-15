from stats import get_num_words, get_character_count


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    filename = "books/frankenstein.txt"
    book_text = get_book_text(filename)
    num_words = get_num_words(book_text)
    char_counts = get_character_count(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    [print(f"{data['char']}: {data['cnt']}") for data in char_counts]
    print("============= END ===============")


main()
