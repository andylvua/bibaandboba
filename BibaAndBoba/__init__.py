from BibaAndBoba.comparator import Comparator
from BibaAndBoba.biba_and_boba import BibaAndBoba
from BibaAndBoba.utils.reader import Reader

import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

try:
    import nltk
    nltk.data.find('tokenizers/punkt')
except LookupError:
    logging.warning("NLTK punkt tokenizer is not installed. Downloading...")

    from BibaAndBoba.utils.nltk_punkt_downloader import download_punkt
    download_punkt()
