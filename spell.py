import random
import string

def fire():
    letters = 'jf'
    length = random.randint(1,5)

    word = ''.join(random.choice(letters) for _ in range(length))
    
    wordType = input(f"Fire incantation {word}: ")

    return "Success" if wordType == word else "Fail"

