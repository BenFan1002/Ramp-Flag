import hashlib

from nltk.corpus import words


stored_hash = "a1569b423225dd477ada7b7ef6e45819"  # replace with the stored hash
salt = "f3f0a9106617"  # replace with the salt
filtered_words = [word for word in words.words() if len(word) == 7]

for combination in filtered_words:
    input_with_salt = f'{combination.lower()}{salt}'
    result = hashlib.md5(input_with_salt.encode())
    if result.hexdigest() == stored_hash:
        print("User input is: " + combination)
        break

