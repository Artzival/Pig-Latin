input_text = input("Enter a word or phrase to be turned into pig latin: ")
words = input_text.split()
for word in words:
    if len(word) > 1:    
        first_letter = word[0]
        word = word[1:] + "-" +first_letter + "ay"
    print(word, end=" ")