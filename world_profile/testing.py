from functools import partialmethod

from dataclasses import dataclass, field

class StarPort:
    """A data descriptor to hold star port values.
    """
    d = {'10': 'Great'}

    def __get__(self, obj, objtype):
        return self.d[self.var]

    def __set__(self, obj, val):
        self.var = val


@dataclass
class WorldProfile(object):
    # starport: StarPort()
    code: str
    starport: StarPort()

    @classmethod
    def decode(cls, code):
        return cls(code, code)


class WorldProfile2:
    starport = StarPort()

    def __init__(self, code):
        self.starport = code


m = WorldProfile.decode('10')
print(m)
print(m.starport)

n = WorldProfile2('10')
print(n.starport)

test = {'Hello': 'yes', 'Goodbye': 'not'}
print('\n'.join([f'{k}: {v}' for k, v in test.items()]))