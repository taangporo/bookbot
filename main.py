def main():
    path_to_file = "books/frankenstein.txt"
    
    with open (path_to_file, "r") as f:
        file_contents = f.read()
        
    print("--- Begin report of", path_to_file, "---")
    
    word_count = count_words(file_contents)
    print("\n{} words found in the document\n".format(word_count))
    
    char_counts = count_characters(file_contents)
    print("Character counts:")
    for char, count in char_counts.items():
        print("The '{}' character was found {} times".format(char, count))
    print("--- End report ---")
    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_counts = {}
    
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts
    
if __name__ == "__main__":
    main()