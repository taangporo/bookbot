def main():
    path_to_file = "books/frankenstein.txt"
    
    with open (path_to_file) as f:
        file_contents = f.read()
        
    print(file_contents)
    
    word_count = count_words(file_contents)
    print("Number of words in the text:", word_count)
    
def count_words(text):
    words = text.split()
    return len(words)
    
if __name__ == "__main__":
    main()