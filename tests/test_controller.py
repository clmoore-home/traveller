import world_profile.controller as controller

def test_process_decode_request():
    """Test that process_decode_request returns a world profile"""
    profile = controller.process_decode_request('C9A7436-12')
    assert profile.__str__() == "WorldProfile(code='C9A7436-12', starport_rating='C')"
    assert profile.starport ==  {
            'Quality': 'Routine',
            'Berthing Cost': 'Cr100-Cr600',
            'Fuel': 'Unrefined',
            'Facilities': 'Shipyard (small craft); Repair'
            }


def test_get_starport():
    """Test that starport dictionary is returned"""
    profile = controller.process_decode_request('C9A7436-12')
    starport = controller.get_starport(profile)
    assert starport == {
            'Quality': 'Routine',
            'Berthing Cost': 'Cr100-Cr600',
            'Fuel': 'Unrefined',
            'Facilities': 'Shipyard (small craft); Repair'
            }