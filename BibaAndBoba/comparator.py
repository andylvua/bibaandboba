from math import ceil

from BibaAndBoba.nltk_analyzer import NLTKAnalyzer


def max_correlation(n: int) -> float:
    i = 1
    s = 0

    for i in range(1, n + 1):
        s = s + 1 / i
    return s * 2


class Comparator:
    def __init__(self, person1: NLTKAnalyzer, person2: NLTKAnalyzer, limit: int = 10):
        self.__person1_words = person1.freq_dist(limit=limit)['Word']
        self.__person2_words = person2.freq_dist(limit=limit)['Word']
        self.__person_1_name = person1.get_name()
        self.__person_2_name = person2.get_name()
        self.__max_correlation = max_correlation(len(self.__person1_words))
        self.__same_words = set()
        self.__correlation_percent = self.__correlation()

    def __correlation(self) -> float:
        corr = 0
        for i, word_1 in enumerate(self.__person1_words):
            for j, word_2 in enumerate(self.__person2_words):
                if word_1 == word_2:
                    corr += (1/(i+1) + 1/(j+1))
                    self.__same_words.add(word_1)
                else:
                    continue

        result = (corr/self.__max_correlation)*100
        return ceil(result)

    def get_correlation(self) -> float:
        return self.__correlation_percent

    def get_same_words(self) -> set:
        return self.__same_words
