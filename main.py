from stats import num_words_in_book
from stats import occurence_characters, sort
import sys


def get_book_text(path):
    with open(path) as f: # do something with f (the file) here
        file_contents = f.read() #f is a file object
    return (file_contents)





def main ():
    book_path=sys.argv
    if len(book_path)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book=get_book_text(f"{book_path[1]}")
    num_words=num_words_in_book(book)
    occ=occurence_characters(book)
    sorted_occurence_characters=sort(occ)

#print section
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path[1]}...")
    print("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_occurence_characters:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    



main()


