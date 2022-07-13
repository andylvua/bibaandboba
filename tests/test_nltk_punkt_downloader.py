import logging
import nltk

from BibaAndBoba.utils.nltk_punkt_downloader import download_punkt


def test_download_punkt(caplog):
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        with caplog.at_level(logging.WARNING):
            download_punkt()
        assert 'Successfully downloaded punkt tokenizer from NLTK.' in caplog.text
