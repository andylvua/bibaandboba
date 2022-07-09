from BibaAndBoba.comparator import Comparator
from BibaAndBoba.nltk_analyzer import NLTKAnalyzer
from BibaAndBoba._reader import Reader

try:
    import nltk
    nltk.data.find('tokenizers/punkt')
except LookupError:
    print("NLTK punkt tokenizer is not installed. Downloading...")
    from BibaAndBoba._nltk_punkt_downloader import download_punkt
    download_punkt()
