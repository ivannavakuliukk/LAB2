import os

class Counter:
    def __init__(self, fname):
        self.fname = fname
        self.num_words = 0
        self.num_lines = 0
        self.num_charc = 0
        self.num_spaces = 0

    def count_lines(self):
        with open(self.fname, 'r') as f:
            for line in f:
                self.num_lines = self.num_lines + 1
        print("Number of lines in text file: ", self.num_lines)

    def count_words(self):
        with open(self.fname, 'r') as f:
            for line in f:
                wordslist = line.split()
                self.num_words = self.num_words + len(wordslist)
        print("Number of words in text file: ", self.num_words)

    def count_charc(self):
        with open(self.fname, 'r') as f:
            for line in f:
                # separating a line from \n character
                line = line.strip(os.linesep)
                self.num_charc = self.num_charc + sum(1 for c in line if c not in (os.linesep, ' '))
        print("Number of characters in text file: ", self.num_charc)

    def count_spaces(self):
        with open(self.fname, 'r') as f:
            for line in f:
                self.num_spaces = self.num_spaces + sum(1 for s in line if s in (os.linesep, ' '))
        print("Number of spaces in text file: ", self.num_spaces)


try:
    file1 = Counter('File1.txt')
    file1.count_lines()
    file1.count_words()
    file1.count_charc()
    file1.count_spaces()
except:
    print("File not found")