import random
import string
def guess_number():
    words = ''.join(random.choices(string.ascii_lowercase, k = 5))
    print(words)
    guess_words = [''] * len(words)
    life = len(words) *2
    print("word you need guess:",guess_words)
    while life > 0 and guess_words != list(words):
        word = input("please input:")
        if words.__contains__(word):
            life = life -1
            guess_words[words.index(word)] = word
            print("guess right! you life rest", life)
            print("word you need continue to guess:",guess_words)
            print (guess_words)
        else:
            life = life -1
            print("guess wrong you life rest",life)
    if guess_words == list(words):
        print("congratulation you win")
    else:
        print("you lost")


guess_number()



