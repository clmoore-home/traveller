import world_profile.world_profile as wp

# You would normally have one controller per model, so this should be renamed/stored to make it clear that this is the controller for world profile.
# You would also have one view implementation per view you're exposing.

def process_decode_request(code):
    return wp.WorldProfile.from_code(code)


def get_starport(profile):
    """Return the starport facility dictionary. Abstracted to controller
    for flexibility"""
    return profile.starport