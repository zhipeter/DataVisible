'''Get country codes'''
from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    '''return country code based on name'''
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None
