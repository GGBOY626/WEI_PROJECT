class SentenceCalculate:
    def __init__(self, sentence):
        self.sentence = sentence
    def sentence_calculate(self,sentence):
        words = sentence.strip().split()
        return len(words)
if __name__ == "__main__":
    sentence = input("input sentence: ")
    obj = SentenceCalculate(sentence)
    result = obj.sentence_calculate(sentence)
    print("calculate result",result)