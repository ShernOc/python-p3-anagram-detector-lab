# your code goes here 
class Anagram: 
    words = ['listen','google', 'inlets', 'banana']
    
    def __init__(self, word):
        self.word = word
    
    #pass in the words as the argument. 
    def match(self,words):
        match = [lists for lists in words if sorted(lists) == sorted(self.word)]
        return match 
    
    
    