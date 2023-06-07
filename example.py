# example.py
from faker import Generator

def test():
    print('[Generate test]')
    single = Generator().generate_word(
        length = 3,
        schema = None, # Leave empty or None for random schema
    )
    print(single) # Print response
    print('[Mass generate test]')
    mass = Generator().mass_generate(
        length = 3,
        schema = ('c', 'v', 'c'), # Required to be inputted
        iterations = 10,
        leading = 'd',
        trailing = '',
        repeats = True, # If False, can lead to infinite freezes with lots of constraints
    )
    for string in mass:
        print(string) # Print response

if __name__ == '__main__':
    test()
