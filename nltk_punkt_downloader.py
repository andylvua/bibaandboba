"""
Important! This module downloads the punkt tokenizer from NLTK.
"""
import nltk
import ssl


def download_punkt():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    nltk.download("punkt")


if __name__ == "__main__":
    download_punkt()
    print("Downloaded punkt tokenizer from NLTK.")
