from dataclasses import dataclass

class Descriptor:

    # def __init__(self, code):
    #     self.code = code

    def __get__(self, obj, type=None):
        return obj.code


class DeepThought:

    attribute1 = Descriptor()

    def __init__(self, code):
        self.code = code


# d = DeepThought('hello')

# print(d.attribute1)

class StarPort:
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
        },
    'D': {
        'Quality': 'Poor',
        'Berthing Cost': 'Cr10-Cr60',
        'Fuel': 'Unrefined',
        'Facilities': 'Limited repair'
        },
    'E': {
        'Quality': 'Frontier',
        'Berthing Cost': '0',
        'Fuel': 'None',
        'Facilities': 'None'
        },
    }

    def __get__(self, obj, type=None):
        return self.starport_facilities[obj.sp]


@dataclass
class WorldProfile:
    starport: StarPort()

    # @classmethod
    # def decode(cls, code):
    #     self.sp = code

    def __init__(self, code):
        self.sp = code


p = WorldProfile('A')

print(p.starport)