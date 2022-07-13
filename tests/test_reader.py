import pytest

from BibaAndBoba.utils.reader import Reader


@pytest.fixture()
def reader(chat_1_file):
    return Reader(file=chat_1_file)


def test_get_companion_id(reader):
    companion_id_actual = reader.get_companion_id()
    companion_id_expected = "483571608"

    assert companion_id_actual == companion_id_expected


def test_get_companion_name(reader):
    companion_name_actual = reader.get_companion_name()
    companion_name_expected = "Андрій"

    assert companion_name_actual == companion_name_expected


def test_get_messages(reader):
    messages_actual = reader.get_messages()
    messages_expected = ["Hi", "Павло"]

    assert messages_actual == messages_expected


def test_get_messages_dict(reader):
    messages_dict_actual = reader.get_messages_dict()

    assert isinstance(messages_dict_actual, list)
    assert isinstance(messages_dict_actual[0], dict)
    assert all(key in messages_dict_actual[0] for key in ["id", "type", "date", "from"])


def test_get_messages_count(reader):
    messages_count_actual = reader.get_messages_count()
    messages_count_expected = 2

    assert messages_count_actual == messages_count_expected
