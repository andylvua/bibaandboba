import pandas as pd
import pkgutil

from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

from BibaAndBoba.utils.reader import Reader
from BibaAndBoba.utils.progress_bar import progress_bar

from BibaAndBoba.utils.reader import FileInput

print("Please wait for your files to be analyzed...")

stopwords = pkgutil.get_data(__name__, 'dictionaries/stopwords.txt')
STOPWORDS = set(stopwords.decode('utf-8').split())
base_ua = pkgutil.get_data(__name__, "dictionaries/base_ua.txt")
STOPWORDS_UA = set(base_ua.decode('utf-8').split())


def tokenize(messages: list[str], companion_name: str) -> list[str]:
    """
    The tokenize function takes a list of messages and a companion name as arguments.
    It then tokenizes each message in the list and removes stopwords.
    The function returns list of generated tokens or simply separate words.

    :param messages: list[str]: Pass a list of messages to the function
    :param companion_name: str: The name of the companion that will be shown in a progress bar
    :return: A list of strings
    """
    tokenized_list = []

    for message in progress_bar(messages, prefix=f'Analyzing {companion_name} messages:'):
        tokenized = word_tokenize(message)
        for token in tokenized:
            token = token.lower()
            if token not in STOPWORDS_UA and not any(word in token for word in STOPWORDS):
                tokenized_list.append(token)

    return tokenized_list


class BibaAndBoba:
    """
    BibaAndBoba is a class that for analyzing two Telegram chat history files.
    It provides a methods to get the difference words, the frequency distribution of the difference words,
    and other parameters. Uses NLTK library to tokenize the messages. :class:`BibaAndBoba.Reader` class is used to read
    the files.
    """

    # A cache variable that is shared by all instances of the class and is used to store the tokenized messages
    __cache = {}

    def __init__(self, file_1: FileInput, file_2: FileInput):
        """
        The __init__ function is called when an instance of the class is created.
        It initializes all the variables that are unique to each instance.

        :param self: Reference the object itself
        :param file_1: Specify the first file
        :param file_2: Specify the second file
        :raises: ValueError: If files is identical
        """
        file_1 = Reader(file_1)
        file_2 = Reader(file_2)
        if file_1.get_companion_id() == file_2.get_companion_id():
            raise ValueError("Files must be different")

        self.__person_1_name = file_1.get_companion_name()
        self.__person_2_name = file_2.get_companion_name()

        if file_1.get_companion_id() in self.__cache:
            print(f"{format(self.__person_1_name)} messages are already analyzed. Using cached data")
            self.__tokenized_person_1 = self.__cache[file_1.get_companion_id()]
        else:
            self.__messages_person_1 = file_1.get_messages()
            self.__tokenized_person_1 = tokenize(self.__messages_person_1, self.__person_1_name)
        if file_2.get_companion_id() in self.__cache:
            print(f"{format(self.__person_2_name)} messages are already analyzed. Using cached data")
            self.__tokenized_person_2 = self.__cache[file_2.get_companion_id()]
        else:
            self.__messages_person_2 = file_2.get_messages()
            self.__tokenized_person_2 = tokenize(self.__messages_person_2, self.__person_2_name)

        self.__difference_words = self.__substraction()

        self.__cache[file_1.get_companion_id()] = self.__tokenized_person_1
        self.__cache[file_2.get_companion_id()] = self.__tokenized_person_2

    def __substraction(self) -> list[str]:
        """
        The __substraction function takes two lists of strings as input.
        It returns a list of words that are in the first list but not in the second.

        :param self: Access variables that belongs to the class
        :return: A list of words that are present in the minuend but not in the subtrahend
        :doc-author: Trelent
        """
        messages_minuend = self.__tokenized_person_1
        messages_subtrahend = set(self.__tokenized_person_2)
        difference_words = []

        for word in messages_minuend:
            if word not in messages_subtrahend:
                difference_words.append(word)

        return difference_words

    def freq_dist(self, limit: int = 10) -> pd.DataFrame:
        """
        Takes a list of words, counts the frequency of each word, and returns a :class:`pd.DataFrame` with the most
        frequent ones.

        :param limit: The number of words to return, defaults to 10
        :type limit: int (optional)
        :return: A dataframe with the most common words and their counts.
        """
        fdist = FreqDist(self.__difference_words)
        df = pd.DataFrame(fdist.most_common(limit), columns=['Word', 'Count'])

        df["Quotient"] = (df["Count"] / len(self.__tokenized_person_1)) * 100

        return df

    def get_words_person_1(self) -> list[str]:
        """
        Returns a list of all words in the message
        sent by person 1.

        :param self: Refer to the object of the class
        :return: A list of all the words in the person 1 messages
        """
        return self.__tokenized_person_1

    def get_words_person_2(self) -> list[str]:
        """
        Returns a list of all words in the message
        sent by person 2.

        :param self: Access the class attributes and methods
        :return: A list of all the words in the person 2 messages
        """
        return self.__tokenized_person_2

    def get_name(self) -> str:
        """
        Returns the name of the object.

        :param self: Refer to the object itself
        :return: The name of the object
        """
        return self.__person_1_name

    def get_difference_words(self) -> list[str]:
        """
        Returns a list of words that are in the first text but not in the second.

        :param self: Access the attributes and methods of the class
        :return: A list of words that are unique to the first person document
        """
        return self.__difference_words
