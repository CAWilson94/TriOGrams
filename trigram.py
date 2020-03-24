from pprint import pprint
import logging
import random 

class Trigram:

    def __init__(self, input_path):
        self.input_path = input_path

    def get_trigrams_from_input(self): 
        triDict = {}
        
        with open(self.input_path, encoding="utf8") as input: 
            for line in input: 
                for word in range(len(line.split()) -2):
                    triDict.update(self.get_trigrams(line, word, triDict))
        return triDict

    def find_trigrams(self):
        """ Find all the trigrams in a given input """
        triDict = {}
        input_list = self.input_path.split(" ")
        for word in range(len(input_list) - 2):
            bigram = f"{input_list[word]} {(input_list[word+1])}"
            if triDict.get(bigram)==None:
                triDict[bigram] = [input_list[word+2]]
            else:
                triDict[bigram].append(input_list[word+2])
        return (triDict)

    def get_trigrams(self, line, word, triDict):
        line = line.split()
        bigram = f"{line[word]} {line[word+1]}"
        if triDict.get(bigram)==None: 
            triDict[bigram] = [line[word+2]]
        else:
            triDict[bigram].append(line[word+2])
        return triDict


    def text_generator(self): 
        """ probably want to use a generator for this... """ 
        new_text = []
        text_dictionary = self.get_trigrams_from_input()
        value_pair = random.choice(list(text_dictionary.keys()))
        new_text.append(value_pair)
        try: 
            while(text_dictionary[value_pair] != "THE END"):     
                if(value_pair in text_dictionary.keys()):        
                    new_text.append(text_dictionary[value_pair][-1])
                    value_pair = value_pair.split(" ")[-1] + " " + new_text[-1]
                final_text = " ".join(new_text)
        except Exception as e: 
            logging.warning("wit is going on: %s", e)
        return final_text.split()

    def text_generator_search_longest(self): 
        best_results = self.text_generator()
        for i in range(10):
            results = self.text_generator() 
            if len(results) > len(best_results):
                best_results = results
        print(f"The best results are length {len(best_results)}: {best_results}")

def main():
    #input = "I wish I may I wish I might"
    input_book = "book.txt"
    tri_o_gram = Trigram(input_book)
    #tri_o_gram.text_generator_search_longest()
    generated_text = tri_o_gram.text_generator()
    print(generated_text)
    #print(generated_text)
    #tri_o_gram.get_trigrams_from_input()

if __name__ == '__main__':
    main()

