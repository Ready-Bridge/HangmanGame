from hangman import Hangman
from word import Word

class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.guessedChars = []
        self.numTries = 0
        self.currentStatus = '' * len(word)
        self.guess('')


    def display(self):
        print('Current: ' + self.currentStatus)
        print('Tries: ' + str(self.numTries))




    def guess(self, character):
        self.guessedChars.append(character)
        if not character in self.secretWord :
            self.numTries += 1
            return False

        else :
            currentStatus =''
            for i in self.secretWord :
                if i in self.guessedChars :
                    currentStatus += i

                else :
                    currentStatus += '_'

            self.currentStatus = currentStatus

            if self.currentStatus == self.secretWord:
                return True
            else:
                return False







