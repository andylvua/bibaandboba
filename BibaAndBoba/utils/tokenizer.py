import pkgutil

from nltk.tokenize import word_tokenize

from BibaAndBoba.utils.cacher import cache_to_file
from BibaAndBoba.utils.progress_bar import progress_bar
from BibaAndBoba.utils.languages import get_supported_language

# from emoji.unicode_codes import EMOJI_UNICODE_ENGLISH

stopwords = pkgutil.get_data(__name__, '../dictionaries/stopwords.txt')
STOPWORDS = set(stopwords.decode('utf-8').split())
base_ua = pkgutil.get_data(__name__, "../dictionaries/base_ua.txt")
STOPWORDS_UA = set(base_ua.decode('utf-8').split())
# EMOJI = set(EMOJI_UNICODE_ENGLISH.values())


# noinspection PyUnusedLocal
@cache_to_file()
def tokenize(messages: list[str], companion_id, companion_name: str = "Undefined",
             use_cache: bool = True, flush_cache: bool = False) -> list[str]:
    """
    Takes a list of strings and returns a list of tokens.
    It also accepts two keyword arguments, use_cache and flush_cache.
    If you use_cache is False, the function will neither use the cache from previous runs nor create a new one.
    Default is True.
    If flush_cache is True, the function flushes old cached data and creates a new cache.

    :param messages: list[str]: Pass the list of messages to be tokenized
    :param companion_id: Identify the companion ID
    :param companion_name: str: Identify the companion name
    :param use_cache: bool: Determine whether to use the cache or not. Defaults to True.
    :param flush_cache: bool: Clear the cache of a given tokenizer. Defaults to False.
    :return: A list of tokens for each message
    """
    language = get_supported_language(messages)

    tokenized_list = []

    if not messages:
        return []

    for message in progress_bar(messages, prefix=f'Analyzing {companion_name} messages:'):
        tokenized = word_tokenize(message, language=language)
        for token in tokenized:
            token = token.lower()
            if token not in STOPWORDS_UA and not any(word in token for word in STOPWORDS):
                tokenized_list.append(token)

    return tokenized_list
