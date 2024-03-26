import random
import string

def generate_random_word(length):
    # Define the pool of letters (only 'j' and 'f')
    letters = 'jf'

    # Generate the random word
    word = ''.join(random.choice(letters) for _ in range(length))
    return word

# Specify the desired word length (between 3 and 5)
desired_length = random.randint(3, 5)

# Generate the random word
random_word = generate_random_word(desired_length)
print(f"Random word with {desired_length} letters: {random_word}")

