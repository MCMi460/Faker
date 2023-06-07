# generator.py
from . import *
import random

# Example letter schema:
# ('consonant', 'vowel', 'consonant')
# == ('c', 'v', 'c')
# MUST: len(schema[:length]) == length

# Length:
# 3 <= length <= 10

class Generator_Exception(Exception):
    pass

class Generator:
    def generate_word(self, *,
        length:int = random.randint(3, 10),
        schema:tuple = None,
    ):
        if not schema:
            schema = self.random_schema(length)
        if not len(schema[:length]) == length:
            raise Generator_Exception('schema does not equal length')

        return String(tuple( random.choice(vowels) if type in ('v', 'vowel') else random.choice(consonants) for type in schema ))

    def random_schema(self, length:int):
        i = length
        order = []
        while i > 0:
            for n in range(random.randint(1, 4 if i >= 4 else i)): # consonant
                if random.randint(0, 10) >= 9:
                    order.append('v')
                else:
                    order.append('c')
                i -= 1
        if order.count('c') == length:
            order[random.randint(0, length - 1)] = 'v'
        return tuple(order)

    def mass_generate(self, *,
        length:int,
        schema:tuple,
        iterations:int = 100,
        leading:Letter = None,
        trailing:Letter = None,
        repeats:bool = True, # If False, can lead to infinite freezes with lots of constraints
    ):
        if leading:
            if not isinstance(leading, Letter):
                leading = Letter(leading)
            if ('v' if leading.vowel else 'c') != schema[0][0]:
                raise Generator_Exception('failure in leading type')
        if trailing:
            if not isinstance(trailing, Letter):
                trailing = Letter(trailing)
            if ('v' if trailing.vowel else 'c') != schema[-1][0]:
                raise Generator_Exception('failure in trailing type')

        out = []
        while len(out) < iterations:
            ret = self.generate_word(length = length, schema = schema)
            if leading and str(leading) != str(ret.text[0]):
                continue
            if trailing and str(trailing) != str(ret.text[-1]):
                continue
            if not repeats and str(ret) in map(str, out): # WARNING: THIS COULD LEAD TO INFINITE FREEZES IF REPEATS = FALSE
                continue
            out.append(ret)
        return out
