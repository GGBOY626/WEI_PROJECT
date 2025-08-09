import random
import string
class Guess:
    @staticmethod
    def guess_number():
        wordslist = ["python","java","csharp","golang","javascript","html"]
        words = random.choice(wordslist)
        print(words)
        guess_words = [''] * len(words)
        life = len(words)
        print("word you need guess:", guess_words)
        while life > 0 and guess_words != list(words):
            word = input("please input:")
            if words.__contains__(word):
                for idx, ch in enumerate(words):
                    if ch == word:
                        guess_words[idx] = word
                print("guess right! you life rest", life)
                print("word you need continue to guess:", guess_words)
                print(guess_words)
            else:
                life = life - 1
                print("guess wrong you life rest", life)
        if guess_words == list(words):
            print("congratulation you win")
        else:
            print("you lost")

    # 运行
if __name__ == "__main__":
    Guess.guess_number()