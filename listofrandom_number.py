import random

def random_list(n, secure=True):
    random_dot = []
    if secure:
        crypto = random.SystemRandom()
        random_dot = crypto.random
    else:
        random_dot = random.random
    for _ in range(n):
        random_dot.append(random_dot())
    return random_dot

print(random_list(10, secure=False))
