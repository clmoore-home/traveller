import database as db



def test_StarportFacilities():
    """Test that the StarportFacilities class contains the correct attributes"""
    test_row = {'rating': 'A', 'quality': 'Excellent', 'berthing': '500Cr-1500Cr',
        'fuel': 'Refined', 'facilities': 'Shipyard (all); Repair'}
    starport = db.StarportFacilities(**test_row)
    for key, value in test_row.items():
        assert getattr(starport, key) == value


def test_Size():
    """Test that the Size class contains the correct attributes"""
    test_row = {'rating': 1, 'examples': 'Triton', 'gravity': '0.05'}
    size = db.Size(**test_row)
    for key, value in test_row.items():
        assert getattr(size, key) == value
    assert size.diameter == '1600km'


def test_Atmosphere():
    """Test that the Atmosphere class contains the correct attributes"""
    test_row = {'rating': 1, 'composition': 'Trace', 'examples': 'Mars',
        'pressure': '0.0001 to 0.09', 'survivalgear': 'Vacc Suit'}
    atmosphere = db.Atmosphere(**test_row)
    for key, value in test_row.items():
        assert getattr(atmosphere, key) == value


def test_Hydrography():
    """Test that the Hydrography class contains the correct attributes"""
    test_row = {'rating': 1, 'description': 'Desert'}
    hydrography = db.Hydrography(**test_row)
    assert hydrography.rating == 1
    assert hydrography.description == 'Desert'
    assert hydrography.water_percentage == '6% - 15%'


def test_Government():
    """Test that the Government class contains the correct attributes"""
    test_row = {'rating': 1, 'government_type': 'Technocracy', 'description': 'All the tech',
        'examples': 'An example', 'contraband': 'Travellers, Drugs'}
    government = db.Government(**test_row)
    for key, value in test_row.items():
        assert getattr(government, key) == value


def test_LawLevel():
    """Test that the LawLevel class contains the correct attributes"""
    test_row = {'rating': 1, 'restricted_arms': 'Poison gas, explosives, undetectable weapons, WMD',
        'restricted_armor': 'Battle dress'}
    lawlevel = db.LawLevel(**test_row)
    assert lawlevel.rating == 1
    assert lawlevel.restricted_arms == 'Poison gas, explosives, undetectable weapons, WMD'
    assert lawlevel.restricted_armor == 'Battle dress'

