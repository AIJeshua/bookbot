def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()


def count_words(book_text):
    num_words = len(book_text.split())
    return num_words

def count_each_character_instances(book_text):
    lowered_book_text = book_text.lower()
    letter_counts = {}
    for char in lowered_book_text:
        if char.isalpha():
            if char in letter_counts:   
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    return letter_counts


def generate_report(file_path):
    book_text = get_book_text(file_path)
    word_count = count_words(book_text)
    character_counts = count_each_character_instances(book_text)
    
    # Sort characters by count in descending order
    sorted_chars = sorted(character_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Generate the report
    report = []
    report.append("============ BOOKBOT ============")
    report.append(f"Analyzing book found at {file_path}...")
    report.append("----------- Word Count ----------")
    report.append(f"Found {word_count} total words")
    report.append("--------- Character Count -------")
    
    # Add each character and its count
    for char, count in sorted_chars:
        report.append(f"{char}: {count}")
    
    report.append("============= END ===============")
    
    # Print the report
    print("\n".join(report))

