import random
import string

def generate_random_word():
    # Define the pool of letters
    letters = string.ascii_lowercase

    # Generate a random word length (between 3 and 5)
    word_length = random.randint(3, 5)

    # Ensure the word contains 'j' and 'f'
    while True:
        word = ''.join(random.choice(letters) for _ in range(word_length))
        if 'j' in word and 'f' in word:
            break

    return word

# Generate the random word
random_word = generate_random_word()
print(f"Random word: {random_word}")

