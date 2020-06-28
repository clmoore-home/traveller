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
    return [f'Government Type: {gtype}', f'Description: {textwrap.fill(description, width=65)}', 
        f'Example(s): {textwrap.fill(examples, width=65)}', f'Common contraband: {textwrap.fill(contraband, width=65)}']

government = [
    government_variables('None', 'No government structure. In many cases, family bonds predominate', 'Family, Clan, Anarchy', 'None'),
    government_variables('Company/Corporation', 
        """Ruling functions are assumed by a company managerial elite, and most citizenry are company employees or dependants""",
        """Corporate outpost, asteroid mine, feudal domain""", 'Weapons, Drugs, Travellers'),
    government_variables('Participating democracy', 'Ruling functions are reached by the advice and consent of the citizenry directly', """Collective, tribal
council, commlinked
consensus""", 'Drugs'),
    government_variables('Self-perpetuating oligarchy', """Ruling functions are performed by a
restricted minority, with little or no input
from the mass of citizenry""", """Plutocracy,
hereditary ruling
caste""", """Technology,
Weapons,
Travellers"""),
    government_variables('Representative democracy', """Ruling functions are performed by elected
representatives""", """Republic,
democracy""", """Drugs, Weapons,
Psionics"""),
    government_variables('Feudal technocracy', """Ruling functions are performed by specific
individuals for persons who agree to be
ruled by them. Relationships are based
on the performance of technical activities
which are mutually beneficial""", """Those with
access to higher
technology tend to
have higher social
status""", """Technology,
Weapons,
Computers"""),
    government_variables('Captive government', """Ruling functions are performed by an
imposed leadership answerable to an
outside group""", """A colony or
conquered area""", """Weapons,
Technology,
Travellers"""),
    government_variables('Balkanisation', """No central authority exists; rival
governments complete for control. Law
level refers to the government nearest the
starport""", """Multiple
governments, civil
war""", 'Varies'),
    government_variables('Civil service bureaucracy', """Ruling functions are performed by
government agencies employing
individuals selected for their expertise""", """Technocracy,
Communism""", 'Drugs, Weapons'),
    government_variables('Impersonal bureacracy', """Ruling functions are performed by
agencies which have become insulated
from the governed citizens""", """Entrenched castes
of bureaucrats,
decaying empire""", """Technology,
Weapons, Drugs,
Travellers,
Psionics"""),
    government_variables('Charismatic dictator', """Ruling functions are performed by
agencies directed by a single leader who
enjoys the overwhelming confidence of the
citizens""", """Revolutionary
leader, messiah,
emperor""", 'None'),
    government_variables('Non-charismatic leader', """A previous charismatic dictator has been
replaced by a leader through normal
channels""", """Military
dictatorship,
hereditary kingship""", """Weapons,
Technology,
Computers"""),
    government_variables('Charismatic oligarchy', """Ruling functions are performed by a select
group of members of an organisation or
class which enjoys the overwhelming
confidence of the citizenry""", """Junta, revolutionary
council""", 'Weapons'),
    government_variables('Religious dictatorship', """Ruling functions are performed by a
religious organisation without regard to the
specific individual needs of the citizenry""", """Cult, transcendent
philosophy, psionic
group mind""", 'Varies'),
    government_variables('Religious autocracy', """Government by a single religious leader
having absolute power over the citizenry""", """Messiah""", 'Varies'),
    government_variables('Totalitarian oligarchy', """Government by an all-powerful minority
which maintains absolute control through
widespread coercion and oppresion""", """World church,
Ruthless
corporation""", 'Varies')    
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