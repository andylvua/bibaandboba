import pandas as pd
import pkgutil

from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

from BibaAndBoba._reader import Reader
from BibaAndBoba._progress_bar import progress_bar

FIRST_RUN = True

stopwords = pkgutil.get_data(__name__, 'dictionaries/stopwords.txt')
STOPWORDS = set(stopwords.decode('utf-8').split())
base_ua = pkgutil.get_data(__name__, "dictionaries/base_ua.txt")
STOPWORDS_UA = set(base_ua.decode('utf-8').split())


def tokenize(messages: list[str], companion_name: str) -> list[str]:
    tokenized_list = []

    for message in progress_bar(messages, prefix=f'Analyzing {companion_name} messages:'):
        tokenized = word_tokenize(message)
        for token in tokenized:
            token = token.lower()
            if token not in STOPWORDS_UA and not any(word in token for word in STOPWORDS):
                tokenized_list.append(token)

    return tokenized_list


class NLTKAnalyzer:
    def __init__(self, path_to_file_1: str, path_to_file_2: str):
        __file_1 = Reader(path_to_file_1)
        __file_2 = Reader(path_to_file_2)
        if __file_1.get_file_name() == __file_2.get_file_name():
            raise ValueError("Files must be different")

        global FIRST_RUN
        if FIRST_RUN:
            print("Please wait for your files to be analyzed...")
            FIRST_RUN = False

        self.__messages_person_1 = __file_1.get_messages()
        self.__messages_person_2 = __file_2.get_messages()
        self.__person_1_name = __file_1.get_companion_name()
        self.__person_2_name = __file_2.get_companion_name()
        self.__tokenized_person_1 = tokenize(self.__messages_person_1, self.__person_1_name)
        self.__tokenized_person_2 = tokenize(self.__messages_person_2, self.__person_2_name)
        self.__difference_words = self.__substraction()

    def __substraction(self) -> list[str]:
        messages_minuend = self.__tokenized_person_1
        messages_subtrahend = set(self.__tokenized_person_2)
        difference_words = []

        for word in messages_minuend:
            if word not in messages_subtrahend:
                difference_words.append(word)

        return difference_words

    def freq_dist(self, limit: int = 10) -> pd.DataFrame:
        fdist = FreqDist(self.__difference_words)
        df = pd.DataFrame(fdist.most_common(limit), columns=['Word', 'Count'])

        return df

    def get_words_person_1(self) -> list[str]:
        return self.__tokenized_person_1

    def get_words_person_2(self) -> list[str]:
        return self.__tokenized_person_2

    def get_name(self) -> str:
        return self.__person_1_name

    def get_difference_words(self) -> list[str]:
        return self.__difference_words
