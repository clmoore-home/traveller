from collections import namedtuple

import textwrap

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

size = {
    '0': ['Example(s): Asteroid, orbital complex',
        'Surface Gravity (Gs): Negligible'],
    '1': [
        'Example(s): Triton',
        'Surface Gravity (Gs): 0.05'],
    '2': [
        'Example(s): Luna, Europa',
        'Surface Gravity (Gs): 0.15'],
    '3': 
        ['Example(s): Mercury, Ganymede',
        'Surface Gravity (Gs): 0.25'],
    '4': 
        ['Surface Gravity (Gs): 0.35'],
    '5': 
        ['Example(s): Mars',
        'Surface Gravity (Gs): 0.45'],
    '6': 
        ['Surface Gravity (Gs): 0.7'],
    '7': 
        ['Surface Gravity (Gs): 0.9'],
    '8': 
        ['Example(s): Earth',
        'Surface Gravity (Gs): 1.0'],
    '9': 
        ['Surface Gravity (Gs): 1.25'],
    'A': 
        ['Surface Gravity (Gs): 1.4'],
    
}


def atmosphere_variables(comp, examples, pressure, survival):
    return [f'Composition: {comp}', f'Example(s): {examples}', 
        f'Pressure: {pressure}', f'Survival Gear: {survival}']


atmosphere = [
    atmosphere_variables('None', 'Moon', '0.00', 'Vacc Suit'),
    atmosphere_variables('Trace', 'Mars', '0.0001 to 0.09', 'Vacc Suit'),
    atmosphere_variables('Very Thin, Tainted', '-', '0.1 to 0.42', 'Respirator, Filter'),
    atmosphere_variables('Very Thin', '-', '0.1 to 0.42', 'Respirator'),
    atmosphere_variables('Thin, Tainted', '-', '0.42 to 0.7', 'Filter'),
    atmosphere_variables('Thin', '-', '0.42 to 0.7', '-'),
    atmosphere_variables('Standard', 'Earth', '0.71 to 1.49', '-'),
    atmosphere_variables('Standard, Tainted', '-', '0.71 to 1.49', 'Filter'),
    atmosphere_variables('Dense', '-', '1.5 to 2.49', '-'),
    atmosphere_variables('Dense, Tainted', '-', '1.5 to 2.49', 'Filter'),
    atmosphere_variables('Exotic', '-', 'Varies', 'Air supply'),
    atmosphere_variables('Corrosive', 'Venus', 'Varies', 'Vacc Suit'),
    atmosphere_variables('Insidious', '-', 'Varies', 'Vacc Suit'),
    atmosphere_variables('Very Dense', '-', '2.5+', '-'),
    atmosphere_variables('Low', '-', '0.5 or less', '-'),
    atmosphere_variables('Unusual', '-', 'Varies', 'Varies'),

]

def water_calculation(code):
    """
    >>> water_calculation(1)
    (6, 15)

    >>> water_calculation(2)
    (16, 25)

    >>> water_calculation(3)
    (26, 35)

    >>> water_calculation(4)
    (36, 45)

    >>> water_calculation(5)
    (46, 55)

    >>> water_calculation(10)
    (96, 100)

    >>> water_calculation(0)
    (0, 5)

    """
    start = code * 10 - 4
    end = code * 10 + 5
    if start < 0:
        start = 0
    if end > 100:
        end = 100
    return f'{start}% - {end}%'

hydrography = (
    'Desert world',
    'Dry world',
    'A few small seas',
    'Small seas and oceans.',
    'Wet world',
    'Large oceans',
    'Large oceans and seas',
    'Earth like',
    'Water world',
    'Only a few small islands and archipelagos.',
    'Almost entirely water'
)

def government_variables(gtype, description, examples, contraband):
    """Formatting for input args"""
    return [f'Government Type: {gtype}', f'Description: {textwrap.fill(description)}', 
        f'Example(s): {examples}', f'Common contraband: {contraband}']

government = [
    government_variables('None', 'No government structure. In many cases, family bonds predominate', 'Family, Clan, Anarchy', 'None'),
    government_variables('Company/Corporation', 
        """Ruling functions are assumed by a company managerial elite, and most citizenry are company employees or dependants""",
        """Corporate outpost, asteroid mine, feudal domain""", 'Weapons, Drugs, Travellers'),
    government_variables('Participating democracy', 'TBD', 'TBD', 'TBD'),
    government_variables('Self-perpetuating oligarchy', 'TBD', 'TBD', 'TBD'),
    government_variables('Representative democracy', 'TBD', 'TBD', 'TBD'),
    government_variables('Feudal technocracy', 'TBD', 'TBD', 'TBD'),
    government_variables('Captive government', 'TBD', 'TBD', 'TBD'),
    government_variables('Balkanisation', 'TBD', 'TBD', 'TBD'),
    government_variables('Civil service bureaucracy', 'TBD', 'TBD', 'TBD'),
    government_variables('Impersonal bureacracy', 'TBD', 'TBD', 'TBD'),
    government_variables('Charismatic dictator', 'TBD', 'TBD', 'TBD'),
    government_variables('Non-charismatic leader', 'TBD', 'TBD', 'TBD'),
    government_variables('Charismatic oligarchy', 'TBD', 'TBD', 'TBD'),
    government_variables('Religious dictatorship', 'TBD', 'TBD', 'TBD'),
    government_variables('Religious autocracy', 'TBD', 'TBD', 'TBD'),
    government_variables('Totalitarian oligarchy', 'TBD', 'TBD', 'TBD')    
]

law = [
    ('Poison gas, explosives, undetectable weapons, WMD', 'Battle dress'),
    ('Portable energy and laser weapons', 'Combat armour'),
    ('Military weapons', 'Flak'),
    ('Light assault weapons and submachine guns', 'Cloth'),
    ('Personal concealable weapons', 'Mesh'),
    ('All firearms except shotguns & stunners; carrying weapons discouraged', ''),
    ('Shotguns', ''),
    ('All bladed weapons, stunners', 'All visible armour'),
]




"""
"""
if __name__ == '__main__':
    import doctest
    doctest.testmod()

"""
Hydrographics
Hydrographic
Percentage Description
0 0%-5% Desert world
1 6%-15% Dry world
2 16%-25% A few small seas.
3 26%-35% Small seas and
oceans.
4 36%-45% Wet world
5 46%-55% Large oceans
6 56%-65%
7 66%-75% Earth-like world
8 76%-85% Water world
9 86%-95% Only a few small
islands and
archipelagos.
10 (A) 96-100% Almost entirely water.
"""