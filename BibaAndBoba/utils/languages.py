from googletrans import Translator
from googletrans.constants import LANGUAGES

NLTK_SUPPORTED_LANGUAGES = ['czech',
                            'danish',
                            'dutch',
                            'english',
                            'estonian',
                            'finnish',
                            'french',
                            'german',
                            'greek',
                            'italian',
                            'norwegian',
                            'polish',
                            'portuguese',
                            'russian',
                            'slovene',
                            'spanish',
                            'swedish',
                            'turkish',
                            ]


def __get_language(messages: list[str]):
    """
    Returns the language of the messages.
    """
    translator = Translator()

    language_sample = ' '.join(messages[:50])
    language = translator.detect(language_sample).lang

    return language


def get_supported_language(messages: list[str]):
    """
    Returns the language if it's supported by NLTK, otherwise returns 'english'.
    """
    language = __get_language(messages)

    if LANGUAGES.get(language) in NLTK_SUPPORTED_LANGUAGES:
        return LANGUAGES[language]
    else:
        print(f'Detected language of your messages - [{language}] is not supported by BibaAndBoba. '
              f'English will be used by default.')

        return 'english'
