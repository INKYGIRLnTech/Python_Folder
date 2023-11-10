
# Sentence is the class
class Sentence:

    #create an init method pass self and sentence
    def __init__(self, sentence):
       
        self.sentence = sentence
        #iterator is a object with a state so
        #that  it remembers where it is during its iteration
        self.index = 0
        #list of words to iterate over
        #splits the screen by spaces
        self.words = self.sentence.split()

    # create a iter method
    def __iter__(self):
        return self
    
    def __next__(self):
        #if true returns next word in a sentence til there are no more
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words



my_sentence = Sentence('This is a test')

for word in my_sentence:
    print(word)