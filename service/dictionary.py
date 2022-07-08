with open("src/base.lst.txt", "r") as dictionary:
    with open("../dictionaries/base_ua.txt", "w") as base:
        for line in dictionary:
            word = line.split()[0]
            base.write(word + "\n")
