caesarDict = {
    "a": "v",
    "b": "w",
    "c": "x",
    "d": "y",
    "e": "z",
    "f": "a",
    "g": "b",
    "h": "c",
    "i": "d",
    "j": "e",
    "k": "f",
    "l": "g",
    "m": "h",
    "n": "i",
    "o": "j",
    "p": "k",
    "q": "l",
    "r": "m",
    "s": "n",
    "t": "o",
    "u": "p",
    "v": "q",
    "w": "r",
    "x": "s",
    "y": "t",
    "z": "u",
    
            }

sentence = input("Welcome to Caesar's Cipher program. Please enter a phrase to be encrypted: ")
print("You have entered the phrase: ", sentence)
sentence = sentence.lower()
letters = [*sentence]

output = ''
for letter in letters:
    if letter in caesarDict:
        encrypted_letter = caesarDict[letter]
        output += encrypted_letter
    else:
        output += letter

print("After encryption, the phrase reads: ", output)

while True:
    nextSentence = input("Please enter another phrase to be encrypted: ")
    print("You have entered the phrase: ", nextSentence)
    nextSentence = nextSentence.lower()
    nextLetters = [*nextSentence]

    nextOutput = ''
    for nextLetter in nextLetters:
        if nextLetter in caesarDict:
            next_encrypted_letter = caesarDict[nextLetter]
            nextOutput += next_encrypted_letter
        else:
            nextOutput += nextLetter

    print("After encryption, the phrase reads: ", nextOutput)    