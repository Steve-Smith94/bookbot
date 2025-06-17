from stats import count
from stats import char_count
from stats import sorted_counts
import sys
#usage ptyhon3 main.py <path_to_book>


def get_book_text(filepath):
    with open (filepath) as f:
        file_contents = f.read()
    return file_contents

def main ():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]} ")
        the_book = get_book_text(sys.argv[1])
        word_count = count(the_book)
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        character_counts = char_count(the_book)
        sorted_character_counts = sorted_counts(character_counts) 
        for item in sorted_character_counts:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")



main()
