from functools import partialmethod

from dataclasses import dataclass, field

class StarPort:
    """A data descriptor to hold star port values.
    """
    # convert data to use namedtuples
    starport_facilities = {
        'A': {
            'Quality': 'Excellent',
            'Berthing Cost': 'Cr1000-Cr6000',
            'Fuel': 'Refined',
            'Facilities': 'Shipyard (all); Repair'
            },
        'B': {
            'Quality': 'Good',
            'Berthing Cost': 'Cr500-Cr3000',
            'Fuel': 'Refined',
            'Facilities': 'Shipyard (spacecraft), Repair'
            },
        'C': {
            'Quality': 'Routine',
            'Berthing Cost': 'Cr100-Cr600',
            'Fuel': 'Unrefined',
            'Facilities': 'Shipyard (small craft); Repair'
            }}

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype):
        value = obj.__dict__[self.name]
        # return obj.__dict__.get(self.name)
        return self.starport_facilities[value]

    def __set__(self, obj, value):
        obj.__dict__[self.name] = self.starport_facilities[value]
        obj.__dict__.update({'Starport Rating':})
        # obj.__dict__[self.name] = value


class WorldProfile:
    starport = StarPort()

    def __init__(self, code):
        self.starport = code


n = WorldProfile('A')
print(n.starport)
print(n.__dict__)