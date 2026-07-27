def backward_strings(s):
    for letter in s[::-1]:
        print(letter)

# =================================================================

def backward_strings(s):
    for letter in s[::-1]:
        print(letter)
word = input("Enter a word: ")
backward_strings(word)


# ==================================================================

def backward_strings(s):
    return s[::-1]

word = input("Enter a word: ")
result = backward_strings(word)

print("Reversed word:", result)

# ==================================================================

prefixes = 'JKLMNOPQ'
suffix = 'ack'
   for letter in prefixes:
     print letter + suffix
 The output is:
 Jack
 Kack
 Lack
 Mack
 Nack
 Oack
 Pack
 Qack
# Of course, that’s not quite right because “Ouack” and “Quack” are misspelled.
# Exercise 8.2. Modify the program to fix this error.

 for letter in prefixes:
    if letter   == 'O' or letter  == 'Q':
        print(letter + 'U' + suffix)
 else:
    print(letter + suffix)


# ==================


 text = input("Enter a sentence: ")

 text = text.lower() # alles lowercase

 words = text.split()

 word_count = {}

 for word in words:

    word = word.strip(".,!?") # leestekens verwijderen

    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

 print(word_count) 
              








