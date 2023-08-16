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

sentence = input("Please enter a sentence: ")
sentence = sentence.lower()
letters = [*sentence]

output = ''
for letter in letters:
    if letter in caesarDict:
        encrypted_letter = caesarDict[letter]
        output += encrypted_letter
    else:
        output += letter

print("The encrypted sentence is: ", output)