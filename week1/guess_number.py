import random
import string
def guess_number():
    words = ''.join(random.choices(string.ascii_lowercase, k = 5))
    print(words)
    guess_words = [''] * len(words)
    life = len(words) *2
    print(guess_words)
    while(life>0):
        word = input("please input:")
        if words.__contains__(word):
            life = life -1
            guess_words[words.index(word)] = word
            print("words:", words)
            print("guess right! you life rest", life)
            print (guess_words)
        else:
            life = life -1
            print("guess wrong you life rest",life)


guess_number()



