import random

def get_word():
    words = ""
    with open("konnyu.txt", "r", encoding="utf-8") as konnyu:
        words = konnyu.read().splitlines()  # minden sor egy szó
    return random.choice(words)

print(get_word())
