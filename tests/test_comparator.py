import pytest

from BibaAndBoba.comparator import Comparator


@pytest.fixture(scope="module")
def biba_and_boba_comparator(biba_and_boba):
    return Comparator(biba_and_boba, biba_and_boba)


def test_type_error():
    with pytest.raises(Exception) as e_info:
        # noinspection PyTypeChecker
        Comparator("", "")
    assert "You must pass a BibaAndBoba object as the argument" in str(e_info.value)


def test_get_correlation(biba_and_boba_comparator):
    correlation_actual = biba_and_boba_comparator.get_correlation()
    correlation_expected = 100

    assert correlation_actual == correlation_expected


def test_get_same_words(biba_and_boba_comparator):
    same_words_actual = biba_and_boba_comparator.get_same_words()
    same_words_expected = ["hi", "павло"]

    assert all(word in same_words_actual for word in same_words_expected)
