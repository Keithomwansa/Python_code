# Prompt the user to enter a word
# and assign it to the userWord variable.
userWord = input("Enter a word: ")
userWord = userWord.upper()
for l in userWord:
    # Complete the body of the for loop.
    if l == "A" or l == "E" or l == "I" or l == "O" or l == "U":
        continue

    print(l)