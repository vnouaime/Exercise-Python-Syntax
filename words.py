def print_upper_words(words, first_letter, second_letter): 
    """ Returns the word provided in the words list that either starts with the user input of first_letter or second_letter """
    for word in words: 
        if word[0] == first_letter or word[0] == second_letter:
            print(word.upper())
                

# this should print "HELLO", "HEY", "YO", and "YES"
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], "h", "y")