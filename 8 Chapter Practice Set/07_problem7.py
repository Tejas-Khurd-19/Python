# Write a python function to remove a given word from a list and strip it at the same Time.

def remove_and_strip(word_list, word_to_remove):
    # Strip leading and trailing spaces from each word in the list.
    word_list = [word.strip() for word in word_list]
    
    # Remove the word from the list if it matches.
    if word_to_remove.strip() in word_list:
        word_list.remove(word_to_remove.strip())
    
    return word_list

def main():
    # Example list and word to remove.
    word_list = [" hello ", "world", "  python ", " code "]
    word_to_remove = "  python "
    
    # Remove and strip the word.
    updated_wordlist = remove_and_strip(word_list, word_to_remove)
    
    # Print the updated list.
    print(updated_wordlist)

# Call the main function.
main()
