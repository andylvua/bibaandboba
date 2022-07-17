import logging
import pickle
import os
from functools import wraps
from pathlib import Path

# Creates a cache directory called BibaAndBoba/cache.
CACHE_DIR_PATH = Path("BibaAndBoba/cache")
CACHE_DIR_PATH.mkdir(parents=True, exist_ok=True)


def cache_file_path(companion_id: str) -> Path:
    """
    The function returns the path to a file that will be used
    to cache data for a given companion. The returned path is based on the
    companion_id parameter, which should be a string representing the id of
    the companion in question. For example, if we have a Companion with an ID
    of 12345 and call cache_file_path(companion_id=12345), then this function would return:

        CACHE_DIR/cache_12345.pickle

    :param companion_id: Create a unique filename for each cache file
    :return: A path object with the path to a cache file
    """
    cache_file = Path(CACHE_DIR_PATH) / f"cache_{companion_id}.pickle"
    cache_file.touch(exist_ok=True)
    return cache_file


def check_chache_file(companion_id: str) -> bool:
    """
    Checks if the cache file is not empty.
    If it's not empty, it returns True. If not, it returns False.

    :param companion_id: str: Determine the companion_id of the cache file
    :return: A boolean value
    """
    cache_file = cache_file_path(companion_id)
    return os.stat(cache_file).st_size != 0


def get_cache(companion_id: str) -> list:
    """
    Returns a dictionary of the cache for a given companion id.
    If there is no cache, it returns an empty dictionary.

    :param companion_id: str: Specify the id of the companion that is being cached
    :return: A dictionary
    """
    cache_file = cache_file_path(companion_id)

    if check_chache_file(companion_id):
        with open(cache_file, "rb") as cf:
            cache = pickle.load(cf)
    else:
        cache = []
    return cache


def save_cache(cache: list, companion_id: str) -> None:
    """
    Saves the cache to a file.

    :param cache: list: Information to be saved to a file
    :param companion_id: str: Create the cache_file based on the companion_id
    :return: None
    """
    cache_file = cache_file_path(companion_id)

    with open(cache_file, "wb") as cf:
        pickle.dump(cache, cf)


def cache_to_file() -> callable:
    def caching(func) -> callable:
        """
        The caching function is a decorator that allows the function to use a cache.
        If the cache is empty, it will run normally and save its output in the cache.
        If there is already something in the cache, it will return what's inside it instead of running again.

        :param func: Call the function that is being wrapped
        :return: A function that uses a cache
        """
        @wraps(func)
        def wrapper(*args, **kwargs) -> list:
            """
            The wrapper function is used to cache the tokenized messages from a specific companion.
            If use_cache is set to False, then the function will not attempt to load or save any cached data.
            If flush_cache is set to True, then all cached data for that particular companion will be deleted.

            :return: The tokenized_messages from the function
            """
            use_cache = kwargs.get("use_cache", True)
            flush_cache = kwargs.get("flush_cache", False)

            if not use_cache:
                return func(*args, **kwargs)

            companion_id = args[1]
            companion_name = args[2]

            cache = get_cache(companion_id)

            if flush_cache:
                logging.info(f"Flushing cache...\n")
                cache = []

            if cache:
                logging.info(f"Messages from {companion_name} are already analyzed. Using cache."
                             f"\nIf you want to clear the cache, please specify flush_cache=True "
                             f"when creating an instance of BibaAndBoba.\n")
                return cache

            tokenized_messages = func(*args, **kwargs)

            save_cache(tokenized_messages, companion_id)

            return tokenized_messages

        return wrapper

    return caching
