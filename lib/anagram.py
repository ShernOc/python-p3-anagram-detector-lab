# your code goes here 
class Anagram: 
    words = ['listen','google', 'inlets', 'banana']
    
    def __init__(self, word):
        self.word = word
    
    def match(self,words):
        match = [letter for letter in words if sorted  (letter) == sorted(self.word)]
        return match 
    
    
    