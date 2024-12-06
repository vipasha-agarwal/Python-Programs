def search_alphabet_in_word(alphabet, word):

    alphabet = alphabet.lower()
    word = word.lower()
    
    for i in range(len(word)):
        if word[i] == alphabet:
            return True
    return False

word = "Vipasha"
alphabet_to_find = "i"

if search_alphabet_in_word(alphabet_to_find, word):
    print(f"The alphabet '{alphabet_to_find}' is found in the word.")
else:
    print(f"The alphabet '{alphabet_to_find}' is not found in the word.")
