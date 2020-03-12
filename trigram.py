from pprint import pprint

class Trigram:

    def __init__(self, input):
        self.input = input

    def findTrigrams(self):
        """ Find all the trigrams in a given input """
        triDict = {}
        input_list = self.input.split(" ")
        for word in range(len(input_list) - 2):
            bigram = f"{input_list[word]} {(input_list[word+1])}"
            if triDict.get(bigram)==None:
                triDict[bigram] = [input_list[word+2]]
            else:
                triDict[bigram].append(input_list[word+2])
        pprint(triDict)
        return (triDict)


def main():
    input = "I wish I may I wish I might"
    tri_o_gram = Trigram(input)
    tri_o_gram.findTrigrams()

if __name__ == '__main__':
    main()

