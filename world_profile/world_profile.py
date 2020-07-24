from collections import namedtuple
from dataclasses import dataclass, field

import world_profile.data as data
import textwrap


# Create one class for each property which is instantiated by the WorldProfile when WP receives a request.
@dataclass
class StarPort:
    """Starport component of a world profile"""
    rating: chr

    starport_class = {
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

    def __post_init__(self):
        self.rating = self.rating.upper()
        return self.starport_class.get(self.rating)

    @property
    def facilities(self):
        return self.starport_class.get(self.rating)


@dataclass
class Size:
    """Size component of a world profile"""
    rating: chr

    size_characteristics = [
            {'Example(s)': 'Asteroid, orbital complex',
                'Surface Gravity' : 'Negligible'},
            {'Example(s)': 'Triton',
                'Surface Gravity': '0.05Gs'},
            {'Example(s)': 'Luna, Europa',
                'Surface Gravity': '0.15Gs'}, 
            {'Example(s)': 'Mercury, Ganymede',
                'Surface Gravity': '0.25Gs'},
            {'Surface Gravity (Gs): 0.35Gs'},
            {'Example(s)': 'Mars',
                'Surface Gravity': '0.45Gs'},
            {'Surface Gravity': '0.7Gs'},
            {'Surface Gravity': '0.9Gs'},
            {'Example(s)': 'Earth',
                'Surface Gravity' : '1.0Gs'},
            {'Surface Gravity': '1.25Gs'},
            {'Surface Gravity': '1.4Gs'},
        ]

    @property
    def characteristic(self):
        size_data = self.size_characteristics[int(self.rating, base=16)]
        size_data['Diameter'] = f'{str(int(self.rating, base=16) * 1600)}km'
        return size_data

@dataclass
class WorldProfile:
    code: str
    starport: None
    size: None

    @classmethod
    def from_code(cls, code):
        return cls(code, StarPort(code[0]), Size(code[1]))



profile = WorldProfile.from_code('C938264-12')
print(profile)
print(profile.starport.facilities)
print(profile.size.characteristic)

# Recast all names/properties using the Traveller nomenclature
# @dataclass
# class WorldProfile:
#     """A class to hold the decoded planet profile

#     >>> WorldProfile('C9A7436-12')
#     WorldProfile(code="C9A7436-12",starport_rating="C",size="9",atmosphere="A",waterpercent="7",population="4",govtype="3",lawlevel="6",techlevel="12")


#     >>> WorldProfile.decode(code) # self hosting factory method
#     WorldProfile(code="C9A7436-12",starport_rating="C",size="9",atmosphere="A",waterpercent="7",population="4",govtype="3",lawlevel="6",techlevel="12")

#     """
#     code: str
#     starport_rating: StarPort # change these to instances of the descriptor classes
#     size: str
#     atmosphere: str
#     waterpercent: str
#     population: str
#     govtype: str
#     lawlevel: str
#     techlevel: str

#     @classmethod
#     def decode(cls, code):
#         """Breaks up the code string, pass the parsed values into """
#         # (static parse method to call) validation on string length happens here - raise exception
#         code = cls.parse_code(code)
#         return cls(code, *code[:7], techlevel=code[8]) # caveat to using this is during inheritance the name will change

#     @staticmethod
#     def parse_code(code):
#         if len(code) != 9:
#             raise CodeLengthError(f'{code} is {len(code)}, needs to be 9')
#         return code
# # All the properties can be removed once we have the descriptor classes
#     @property
#     def starport(self):
#         """Return the dictionary of starport information"""
#         # Is it enough that if the data doesn't recognise the key then none is returned? Should the star port value be validated instead?
#         return data.starport_facilities.get(self.starport_rating)

#     @property
#     def planetary_size(self):
#         # size = self.numerical_codepoint(self.size)
#         size_data = data.size[int(size, base=16)]
#         size_data['Diameter'] = f'{str(int(size, base=16) * 1600)}km'
#         return size_data

#     @property
#     def atmosphere_info(self):
#         return '\n'.join(data.atmosphere[self.numerical_codepoint(self.atmosphere)])
    
#     @property
#     def hydrographic_info(self):
#         water = self.numerical_codepoint(self.waterpercent)
#         percentage_range = data.water_calculation(water)
#         description = data.hydrography[water]
#         return f'Hydrographic percentage: {percentage_range}\nDescription: {description}'
    
#     @property
#     def population_info(self):
#         start = f'1'.ljust(self.numerical_codepoint(self.population) + 1, '0')
#         end = f'9'.ljust(self.numerical_codepoint(self.population) + 1, '9') 
#         return f'{start}-{end}'
    
#     @property
#     def government_info(self):
#         """Planet style of government"""
#         return '\n'.join(data.government[self.numerical_codepoint(self.govtype)])
    
#     def determine_lawlevel_info(self, armour=False):
#         index = 0
#         if armour:
#             index = 1
#         info = namedtuple('Info', ['restricted', 'allowed'])
#         if self.lawlevel == '0':
#             return info('No restrictions', 'All')
#         elif self.lawlevel >= '9':
#             return info('Nothing permitted', 'All')
#         restricted = [i[index] for i in data.law[:self.numerical_codepoint(self.lawlevel)]]
#         allowed = [i[index] for i in data.law[self.numerical_codepoint(self.lawlevel):] if i[index]]
#         return info(textwrap.fill('; '.join(restricted), width=65), textwrap.fill('; '.join(allowed), width=65))

#     @property
#     def lawlevel_info_weapons(self):
#         return self.determine_lawlevel_info()
    
#     @property
#     def lawlevel_info_armour(self):
#         return self.determine_lawlevel_info(armour=True)


if __name__ == '__main__':
    import doctest
    doctest.testmod()