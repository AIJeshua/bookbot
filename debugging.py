def num_each_character_instances(book_text):
    book_text = book_text.lower()
    letter_counts = {}
    for char in book_text:
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    return letter_counts

def debug():
    book_text = get_book_text("books/frankenstein.txt")
    print(num_each_character_instances(book_text))  # This will print the dictionary with character counts
    print(len(num_each_character_instances(book_text))) # This will print the number of unique characters in the book

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()


debug()