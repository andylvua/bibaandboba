from pathlib import Path

import pytest

from BibaAndBoba import BibaAndBoba

TEST_DATA_PATH = Path(__file__).parent.resolve() / "data"


def data_file(filename: str):
    return TEST_DATA_PATH / filename


@pytest.fixture(scope="session")
def chat_1_file():
    return data_file("test_chat_1.json").open("rb").read()


@pytest.fixture(scope="session")
def chat_2_file():
    return data_file("test_chat_2.json").open("rb").read()


@pytest.fixture(scope="session")
def biba_and_boba(chat_1_file, chat_2_file):
    return BibaAndBoba(chat_1_file, chat_2_file)