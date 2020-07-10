from collections import namedtuple
from dataclasses import dataclass, field

import data
import textwrap


class CodeLengthError(Exception):
    pass

# Recast all names/properties using the Traveller 
@dataclass
class WorldProfile:
    """A class to hold the decoded planet profile
    
    >>> WorldProfile('C9A74369-12')
    WorldProfile(code="C9A74369-12",starport_rating="C",size="9",atmosphere="A",waterpercent="7",population="4",govtype="3",lawlevel="6",techlevel="9-12")


    >>> WorldProfile.decode(code) # self hosting factory method
    WorldProfile(code="C9A74369-12",starport_rating="C",size="9",atmosphere="A",waterpercent="7",population="4",govtype="3",lawlevel="6",techlevel="9-12")

    """
    code: str
    starport_rating: str
    size: str
    atmosphere: str
    waterpercent: str
    population: str
    govtype: str
    lawlevel: str
    techlevel: str

    @classmethod
    def decode(cls, code):
        """Breaks up the code string, pass the parsed values into """
        # (static parse method to call) validation on string length happens here - raise exception
        # (static validate method to call)
        code = cls.parse_code(code)
        return cls(code, *code[:7], techlevel=code[8]) # caveat to using this is during inheritance the 

    @staticmethod
    def parse_code(code):
        if len(code) != 9:
            raise CodeLengthError(f'{code} is {len(code)}, needs to be 9')
        return code

    # def numerical_codepoint(self, codepoint):
        
        # 
        # codepoint_map = {'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}
        # try:
        #     return int(codepoint_map[codepoint])
        # except KeyError:
        #     return int(codepoint)
    
    @property
    def starport_info(self):
        """Return the dictionary of starport information"""
        # Is it enough that if the data doesn't recognise the key then none is returned? Should the star port value be validated instead?
        return data.starport_facilities.get(self.starport_rating)


    # @property
    # def starport_info(self):
    #     if self.starport_rating == 'X':
    #         return 'No Starport'
    #     return '\n'.join([f'{k}: {v}' for k, v in 
    #         data.starport_facilities[self.starport_rating].items()])
    
    # @property
    # def planet_size_info(self):
    #     size = self.numerical_codepoint(self.size)
    #     size_info = '\n'.join(data.size[size])
    #     diameter = size * 1600
    #     return f'Diameter: {str(diameter)}km\n{size_info}'

    @property
    def size_info(self):
        # size = self.numerical_codepoint(self.size)
        size_data = data.size[int(size, base=16)]
        size_data['Diameter'] = f'{str(size * 1600)}km'
        return size_data


    @property
    def atmosphere_info(self):
        return '\n'.join(data.atmosphere[self.numerical_codepoint(self.atmosphere)])
    
    @property
    def hydrographic_info(self):
        water = self.numerical_codepoint(self.waterpercent)
        percentage_range = data.water_calculation(water)
        description = data.hydrography[water]
        return f'Hydrographic percentage: {percentage_range}\nDescription: {description}'
    
    @property
    def population_info(self):
        start = f'1'.ljust(self.numerical_codepoint(self.population) + 1, '0')
        end = f'9'.ljust(self.numerical_codepoint(self.population) + 1, '9') 
        return f'{start}-{end}'
    
    @property
    def government_info(self):
        """Planet style of government"""
        return '\n'.join(data.government[self.numerical_codepoint(self.govtype)])
    
    def determine_lawlevel_info(self, armour=False):
        index = 0
        if armour:
            index = 1
        info = namedtuple('Info', ['restricted', 'allowed'])
        if self.lawlevel == '0':
            return info('No restrictions', 'All')
        elif self.lawlevel >= '9':
            return info('Nothing permitted', 'All')
        restricted = [i[index] for i in data.law[:self.numerical_codepoint(self.lawlevel)]]
        allowed = [i[index] for i in data.law[self.numerical_codepoint(self.lawlevel):] if i[index]]
        return info(textwrap.fill('; '.join(restricted), width=65), textwrap.fill('; '.join(allowed), width=65))

    @property
    def lawlevel_info_weapons(self):
        return self.determine_lawlevel_info()
    
    @property
    def lawlevel_info_armour(self):
        return self.determine_lawlevel_info(armour=True)


if __name__ == '__main__':
    import doctest
    doctest.testmod()