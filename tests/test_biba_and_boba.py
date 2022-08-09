import pandas as pd
from pandas.testing import assert_frame_equal


def test_freq_dist(biba_and_boba):
    freq_dist_actual = biba_and_boba.parasite_words()
    freq_dist_expected = pd.DataFrame(
        {
            'Word': ["hi", "павло"],
            'Count': [1, 1],
            'Quotient': [0.5, 0.5],
        }
    )

    assert isinstance(freq_dist_actual, pd.DataFrame)
    assert_frame_equal(freq_dist_actual, freq_dist_expected)


def test_get_tokenized_words_person_1(biba_and_boba):
    tokenized_words_actual = biba_and_boba.get_tokenized_words_person_1()
    tokenized_words_expected = ["hi", "павло"]

    assert tokenized_words_actual == tokenized_words_expected


def test_get_tokenized_words_person_2(biba_and_boba):
    tokenized_words_actual = biba_and_boba.get_tokenized_words_person_2()
    tokenized_words_expected = ["дороу"]

    assert tokenized_words_actual == tokenized_words_expected


def test_get_name(biba_and_boba):
    name_actual = biba_and_boba.get_name()
    name_expected = "Андрій"

    assert name_actual == name_expected


def test_get_difference_words(biba_and_boba):
    difference_words_actual = biba_and_boba.get_difference_words()
    difference_words_expected = ["hi", "павло"]

    assert difference_words_actual == difference_words_expected
