import world_profile.planet as p

from world_profile.planet import WorldProfile

import pytest

def test_planet():
    """Test the Planet class"""
    p = WorldProfile.decode('CA6A643-9')
    assert p.__repr__() == "WorldProfile(code='CA6A643-9', starport_rating='C', size='A', atmosphere='6', waterpercent='A', population='6', govtype='4', lawlevel='3', techlevel='9')"

@pytest.mark.xfail
def test_planet_raises_exception_for_short_code():
    with pytest.raises(p.CodeLengthError):
        WorldProfile.decode('CA643-9')

@pytest.mark.xfail
def test_planet_returns_starport_info():
    """The planet object should have a method for retrieving the starport information"""
    p = WorldProfile.decode('CA6A643-9')
    assert p.starport_info == {
        'Quality': 'Routine',
        'Berthing Cost': 'Cr100-Cr600',
        'Fuel': 'Unrefined',
        'Facilities': 'Shipyard (small craft); Repair'
        }

@pytest.mark.xfail
def test_starport_handles_x():
    p = WorldProfile.decode('XA6A643-9')
    assert p.starport == None


@pytest.mark.xfail
def test_size_info():
    """Testing the method for retrieving size information"""
    p = WorldProfile.decode('CA6A643-9')
    assert p.planetary_size == {
        'Surface Gravity': '1.4Gs',
        'Diameter': '16000km'}


def test_starport_descriptor():
    starport = p.StarPort('A')
    print(starport)
    assert starport == {'Quality': 'Excellent',
        'Berthing Cost': 'Cr1000-Cr6000',
        'Fuel': 'Refined',
        'Facilities': 'Shipyard (all); Repair'}

# next what if size gets an out of range value?

