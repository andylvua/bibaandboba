from BibaAndBoba.biba_and_boba import BibaAndBoba


def _max_correlation(n: int) -> float:
    """
    The max_correlation function computes the maximum correlation between two frequency distributions.

    :param n: :obj:`int`: Specify the length of the frequency distributions
    :return: The maximum correlation
    """
    s = 0

    for i in range(1, n + 1):
        s += 1 / i
    return s


class Comparator:
    """
    Comparator class is used to compare two people. It provides methods to get the correlation percentage of the two
    people and the words that are the same for both of them.
    """

    def __init__(
            self,
            person1: BibaAndBoba,
            person2: BibaAndBoba,
            limit: int = 10,
    ):
        if not isinstance(person1, BibaAndBoba) or not isinstance(person2, BibaAndBoba):
            raise TypeError("You must pass the BibaAndBoba objects as the arguments")

        self.__person1_freq_dist = person1.parasite_words(limit=limit)
        self.__person2_freq_dist = person2.parasite_words(limit=limit)
        self.__same_words = self.__find_same_words()

    def __correlation(self) -> float:
        """
        The __correlation function calculates the correlation between two people.
        It does this by calculating the number of same words in both person's word list,
        based on their place in frequency distributions.

        :param self: Access variables that belongs to the class
        :return: The correlation between two people
        """
        corr = 0
        quotients_person1 = self.__person1_freq_dist["Quotient"]
        quotients_person2 = self.__person2_freq_dist["Quotient"]

        for i, word_1 in enumerate(self.__person1_freq_dist["Word"]):
            for j, word_2 in enumerate(self.__person2_freq_dist["Word"]):
                if word_1 == word_2:
                    quotient_diff = abs(quotients_person1[i] - quotients_person2[j])
                    if quotient_diff > 0.15:
                        corr += (1 / (i + 1)) - quotient_diff
                    else:
                        corr += 1 / (i + 1)
                else:
                    continue

        max_corr = _max_correlation(len(self.__person1_freq_dist["Word"]))
        result = (corr / max_corr)
        return result

    def __alternate_correlation(self) -> float:
        """
        The alternate_correlation function calculates the correlation between two people.
        It does this by calculating the number of same words in both person's word list,
        based on their place in frequency distributions.
        The weight is the quotient of the frequency of the word in the frequency distribution.
        The weight is calculated by dividing the frequency of the word in the frequency distribution by the sum of all
        the frequencies in the frequency distribution.

        :param self: Access the class attributes
        :return: The correlation between the two people
        """
        corr = 0
        for row in self.__person1_freq_dist.itertuples(index=False):
            if row.Word in self.__person2_freq_dist["Word"].values:
                corr += row.Quotient
        for row in self.__person2_freq_dist.itertuples(index=False):
            if row.Word in self.__person1_freq_dist["Word"].values:
                corr += row.Quotient

        return corr / 2

    def __find_same_words(self) -> set:
        """
        The find_same_words function finds the words that are the same for both people.

        :param self: Access the attributes and methods of the class in which it is used
        :return: A set of words that are the same as the word in question
        """
        same_words = set(self.__person1_freq_dist["Word"]) & set(self.__person2_freq_dist["Word"])

        return same_words

    def get_correlation(self, use_alternate_correlation: bool = True) -> float:
        """
        The get_correlation function returns the correlation between two people.

        :param use_alternate_correlation: Use the alternate correlation method
        :param self: Access the class attributes
        :return: The correlation between the two columns
        """
        if use_alternate_correlation:
            return self.__alternate_correlation()
        else:
            return self.__correlation()

    def get_same_words(self) -> set:
        """
        The get_same_words function returns a set of words that are the same for both people.

        :param self: Access the attributes and methods of the class in which it is used
        :return: A list of words that are the same as the word in question
        """
        return self.__same_words
