# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
        
        
    def match(self, liste):
        new_list = list()
        
        for words in liste:
            if sorted(words) == sorted(self.word):
                new_list.append(words)
                
        return new_list
        