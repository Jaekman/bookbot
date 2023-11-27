with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def count_words():
    words = file_contents.split()
    print(len(words))

def count_letters():
    letter_dict = {}
    words = file_contents.split()

    for word in words:
        for letters in word:
            letter_dict[letters.lower()] = letter_dict.get(letters.lower(), 0) + 1
    
    letter_list = list(letter_dict.items())
    letter_list.sort(reverse=True,key=lambda x: x[1])

    def print_report():
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document\n")
        
        for record in letter_list:
            if record[0].isalpha():
                print(f"The {record[0]} charcter was found {record[1]} times")
        print("--- End report ---")
    
    print_report()


count_letters()