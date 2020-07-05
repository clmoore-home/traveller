from collections import namedtuple
from dataclasses import dataclass, field

import data
import textwrap

# Add a class method that takes the string
@dataclass
class Planet:
    """A class to hold the decoded planet profile
    
    >>> Planet('C9A74369-12')
    Planet(code="C9A74369-12",starport_rating="C",size="9",atmosphere="A",waterpercent="7",population="4",govtype="3",lawlevel="6",techlevel="9-12")


    >>> Planet.decode(code) # self hosting factory method
    Planet(code="C9A74369-12",starport_rating="C",size="9",atmosphere="A",waterpercent="7",population="4",govtype="3",lawlevel="6",techlevel="9-12")

    """
    code: str
    # define other attributes here that are filled by the class method


    def __post_init__(self):
        # validation of components happens here?
        self.starport_rating = self.code[0]
        self.size = self.code[1]
        self.atmosphere = self.code[2]
        self.waterpercent = self.code[3]
        self.population = self.code[4]
        self.govtype = self.code[5]
        self.lawlevel = self.code[6]
        self.techlevel = self.code[7:]

    # Can be removed after refactor
    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(code="{self.code}",' 
                f'starport_rating="{self.starport_rating}",'
                f'size="{self.size}",'
                f'atmosphere="{self.atmosphere}",'
                f'waterpercent="{str(self.waterpercent)}",'
                f'population="{self.population}",'
                f'govtype="{self.govtype}",'
                f'lawlevel="{self.lawlevel}",'
                f'techlevel="{self.techlevel}"'
                ')')

    @classmethod
    def decode(cls, code):
        """Breaks up the code string, pass the parsed values into """
        # (static parse method to call) validation on string length happens here - raise exception
        # (static validate method to call)
        return Planet(code='string', starport_rating='sr' etc)

    def numerical_codepoint(self, codepoint):
        codepoint_map = {'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}
        try:
            return int(codepoint_map[codepoint])
        except KeyError:
            return int(codepoint)
    
    @property
    def starport_info(self):
        if self.starport_rating == 'X':
            return 'No Starport'
        return '\n'.join([f'{k}: {v}' for k, v in 
            data.starport_facilities[self.starport_rating].items()])
    
    @property
    def planet_size_info(self):
        size = self.numerical_codepoint(self.size)
        size_info = '\n'.join(data.size[size])
        diameter = size * 1600
        return f'Diameter: {str(diameter)}km\n{size_info}'
    
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