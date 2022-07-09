with open("BibaAndBoba/base.lst.txt", "r") as dictionary:
    with open("../base_ua.txt", "w") as base:
        for line in dictionary:
            word = line.split()[0]
            base.write(word + "\n")
