def sort(word_list):
    """Sort words according to given alphabet."""
    alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
    
    def get_order(char):
        char = char.lower()
        if char in alphabet:
            return alphabet.index(char)
        return len(alphabet)  
    
    return sorted(word_list, key=lambda word: [get_order(c) for c in word])

def read_words_file():
    """Read words from the file and return a dictionary."""
    words_dict = {}
    try:
        with open("words.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if ':' in line:
                    word, definition = line.split(':', 1)
                    words_dict[word.strip()] = definition.strip()
                else:
                    words_dict[line] = ""
        return words_dict
    except FileNotFoundError:
        return {}

def write_words_file(words_dict):
    sorted_words = sort(list(words_dict.keys()))
    
    with open("words.txt", "w", encoding="utf-8") as file:
        for word in sorted_words:
            if words_dict[word]:
                file.write(f"{word} : {words_dict[word]}\n")
            else:
                file.write(f"{word}\n")

def add_word_mode():
    """Mode for adding words to the dictionary."""
    words_dict = read_words_file()
    
    while True:
        word = input("Enter a word to add (or space to return to main menu): ")
        if word == " ":
            return
        
        if word in words_dict:
            print(f"'{word}' already exists in the dictionary.")
        else:
            words_dict[word] = ""
            write_words_file(words_dict)
            print(f"'{word}' has been added to the dictionary.")
        
        if word.lower() == '':
            return

def search_word_mode():
    """Mode for searching words in the dictionary."""
    words_dict = read_words_file()
    
    while True:
        word = input("Enter a word to search (or space to return to main menu): ")
        if word == " ":
            return
        
        if word in words_dict:
            if words_dict[word]:
                print(f"'{word}' : {words_dict[word]}")
            else:
                print(f"'{word}' exists in the dictionary but has no definition.")
        else:
            print(f"'{word}' was not found in the dictionary.")

def define_word_mode():
    """Mode for adding definitions to words."""
    words_dict = read_words_file()
    
    while True:
        word = input("Enter a word to define (or space to return to main menu): ")
        if word == " ":
            return
        
        if word not in words_dict:
            print(f"'{word}' doesn't exist in the dictionary. Adding it now.")
            words_dict[word] = ""
        
        definition = input(f"Enter the definition for '{word}': ")
        words_dict[word] = definition
        write_words_file(words_dict)
        print(f"Definition for '{word}' has been saved.")

def delete_word_mode():
    """Mode for deleting words from the dictionary."""
    words_dict = read_words_file()
    
    while True:
        word = input("Enter a word to delete (or space to return to main menu): ")
        if word == " ":
            return
        
        if word in words_dict:
            del words_dict[word]
            write_words_file(words_dict)
            print(f"'{word}' has been deleted from the dictionary.")
        else:
            print(f"'{word}' was not found in the dictionary.")

def main():
    """Main function to run the program."""
    print("Welcome to the Dictionary Program!")
    
    while True:
        print("\nSelect a mode:")
        print("a - Add words")
        print("s - Search for words")
        print("d - Define words")
        print("e - Delete words")
        print("q - Quit the program")
        
        mode = input("Enter your choice: ").lower()
        
        if mode == 'a':
            add_word_mode()
        elif mode == 's':
            search_word_mode()
        elif mode == 'd':
            define_word_mode()
        elif mode == 'e':
            delete_word_mode()
        elif mode == 'q':
            print("Thank you for using the Dictionary Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
