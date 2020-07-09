import planet as p

from planet import Planet

import pytest

def test_planet():
    """Test the Planet class"""
    p = Planet.decode('CA6A643-9')
    assert p.__repr__() == "Planet(code='CA6A643-9', starport_rating='C', size='A', atmosphere='6', waterpercent='A', population='6', govtype='4', lawlevel='3', techlevel='9')"

def test_planet_raises_exception_for_short_code():
    with pytest.raises(p.CodeLengthError):
        Planet.decode('CA643-9')

def test_planet_returns_starport_info():
    """The planet object should have a method for retrieving the starport information"""
    p = Planet.decode('CA6A643-9')
    assert p.starport_info == {
        'Quality': 'Routine',
        'Berthing Cost': 'Cr100-Cr600',
        'Fuel': 'Unrefined',
        'Facilities': 'Shipyard (small craft); Repair'
        }

def test_starport_info_handles_x():
    p = Planet.decode('XA6A643-9')
    assert p.starport_info == None


def test_size_info():
    """Testing the method for retrieving size information"""
    p = Planet.decode('CA6A643-9')
    assert p.size_info == {
        'Surface Gravity': '1.4Gs',
        'Diameter': '16000km'}

# next what if size gets an out of range value?

