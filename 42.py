import itertools

TARGET_SUM = 42
for combo in itertools.product(range(1, 27), repeat=7):
    if sum(combo) == TARGET_SUM:
        word = ''.join([chr(num + 96) for num in combo])
        print(word)
        break
