import world_profile.world_profile as wp

import pytest


def test_StarPort():
    sp = wp.StarPort('A')
    assert sp.__repr__() == "StarPort(rating='A')"
    assert sp.facilities == {
            'Quality': 'Excellent',
            'Berthing Cost': 'Cr1000-Cr6000',
            'Fuel': 'Refined',
            'Facilities': 'Shipyard (all); Repair'
            }
    lowercase = wp.StarPort('a')
    assert lowercase.facilities == {
            'Quality': 'Excellent',
            'Berthing Cost': 'Cr1000-Cr6000',
            'Fuel': 'Refined',
            'Facilities': 'Shipyard (all); Repair'
            }


def test_Size():
    size = wp.Size('9')
    assert size.__repr__() == "Size(rating='9')"
    assert size.characteristic == {
        'Diameter': '14400km',
        'Surface Gravity': '1.25Gs'
    }
    # Today I learned that assert can identify two dictionaries as equal regardless of key: value order.


def test_WorldProfile_hasa_starport():
    """Test each of the WP characteristics are accessible from instatiated WP object"""
    world = wp.WorldProfile.from_code('C9A7436-12')
    assert world.starport == {
            'Quality': 'Routine',
            'Berthing Cost': 'Cr100-Cr600',
            'Fuel': 'Unrefined',
            'Facilities': 'Shipyard (small craft); Repair'
            }

# def test_WorldProfile_hasa_size():
#     world = wp.WorldProfile.from_code('C9A7436-12')
#     assert world.size == {

#     }
