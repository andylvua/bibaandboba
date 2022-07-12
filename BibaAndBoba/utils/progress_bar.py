def progress_bar(iterable, prefix: str = '', suffix: str = '', decimals: int = 1,
                 length: int = 50, fill: str = '█', print_end: str = "") -> list:
    """
    Takes an iterable as input, which is the object that will be looped over.
    The prefix and suffix arguments are strings that will be displayed before and after the progress bar, respectively.

    :param iterable: Define the iterable object that is passed to the loop
    :param prefix: str: Define a string that will be printed before the progress bar. Default is an empty string.
    :param suffix: str: A string that will be printed after the progress bar. Default is an empty string.
    :param decimals: Specify the number of decimals to be shown in the progress bar. Default is 1.
    :param length: Define the length of the progress bar. Default length is 50.
    :param fill: str: Define the character that fills up the progress bar. Default is a '█' character.
    :param print_end: str: Define the character that will be printed at the end. Default is an empty string.

    :return: A generator
    """

    total = len(iterable)

    def print_progress_bar(iteration: int) -> None:
        """
        Prints a progress bar to the console.
        Takes an integer as input, which is the current iteration of a loop.
        The total number of iterations is defined by another variable.

        :param iteration: Keep track of the current iteration
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)

    print_progress_bar(0)
    for i, item in enumerate(iterable):
        yield item
        print_progress_bar(i + 1)

    print("Done!")
