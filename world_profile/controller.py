import world_profile.world_profile as wp

def process_decode_request(code):
    return wp.WorldProfile.from_code(code)


def get_starport(profile):
    """Return the starport facility dictionary. Abstracted to controller
    for flexibility"""
    return profile.starport