def progress_bar(iterable, prefix: str = '', suffix: str = '', decimals=1,
                 length=50, fill: str = '█', print_end: str = ""):

    total = len(iterable)

    def print_progress_bar(iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)

    print_progress_bar(0)
    for i, item in enumerate(iterable):
        yield item
        print_progress_bar(i + 1)

    print("Done!")
