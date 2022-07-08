from nltk_analyzer import NLTKAnalyzer
from comparator import Comparator


def main():
    pavlo = NLTKAnalyzer("recources/pavlo.json", "recources/roma.json")
    print(pavlo.freq_dist())
    pavlo1 = NLTKAnalyzer("recources/pavlo.json", "recources/roma.json")

    print(Comparator(pavlo, pavlo).get_correlation())


if __name__ == "__main__":
    main()

# print("Андрій️ and Павло are {}% biba and boba".format(correlation(pavlo_fdist, andrii_fdist)[0]),
#       "with same words:", correlation(pavlo_fdist, andrii_fdist)[1])
