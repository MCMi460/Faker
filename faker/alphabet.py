# alphabet.py

letters = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
]

vowels = [
    'a',
    'e',
    'i',
    'o',
    'u',
]

consonants = [ letter for letter in letters if not letter in vowels ]

special_vowel = 'y'

class Letter_Exception(Exception):
    pass

class String_Exception(Letter_Exception):
    pass

class Letter:
    def __init__(self, char:str):
        self.char = char.lower()
        if len(self.char) != 1 or not self.char in letters:
            raise Letter_Exception('%s is not a real letter!' % char)
        self.vowel = False if not self.char in vowels else True
        self.consonant = False if self.char in vowels else True
        self.special = True if self.char == special_vowel else False

    def __str__(self):
        return self.char

    def is_vowel(self):
        return self.vowel

    def is_consonant(self):
        return self.consonant

    def is_special(self):
        return self.special

class String:
    def __init__(self, text:str):
        self.text = []
        try:
            for i in range(len(text)):
                self.text.append(Letter(text[i]))
        except Letter_Exception as e:
            raise String_Exception('char at index %s: %s' % (i, str(e)))

    def __str__(self):
        return ''.join(map(str, self.text))

    def generate_schema(self):
        return tuple( 'c' if char.consonant else 'v' for char in self.text )
