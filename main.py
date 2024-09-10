def main():
    generate_book_report('books/frankenstein.txt')

def generate_book_report(file_path):
    with open(file_path) as f:
        file_content = f.read()
        print(f"--- Beginning report of {file_path} ---")

        num_of_words = getNumOfWords(file_content)
        print(f"{num_of_words} words found in the document")

        character_numbers = getNumOfCharacters(file_content)
        for item in character_numbers:
            print(f"The '{item[0]} character was found {item[1]} times")

        print('--- End report ---')


def getNumOfWords(string):
    return len(string.split()) 

def getNumOfCharacters(string):
    lowered_string = string.lower()
    letter_counts = {}
    for word in lowered_string:
        for letter in word:
            if letter.isalpha():
                if letter in letter_counts:
                    letter_counts[letter] += 1
                else: 
                    letter_counts[letter] = 1
            else: 
                pass

    return sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)



main()