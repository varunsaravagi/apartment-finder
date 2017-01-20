import os

WORK_COORDS = [37.786889, -122.399951]

FILTERS = [
    dict(
        max_price=5000,
        bedrooms=3,
        bathrooms=2,
        has_image=True,
        search_distance=5,
        zip_code=94105,
    ),
    dict(
        max_price=5000,
        bedrooms=3,
        bathrooms=3,
        has_image=True,
        search_distance=5,
        zip_code=94105,
    ),
    dict(
        max_price=3000,
        bedrooms=2,
        bathrooms=2,
        has_image=True,
        search_distance=5,
        zip_code=94105,
    ),
    dict(
        max_price=3000,
        bedrooms=2,
        bathrooms=1,
        has_image=True,
        search_distance=5,
        zip_code=94105,
    ),
]
## Location preferences

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'sfbay'

# What Craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
AREA = "sfc"

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {
    "pac_heights": [
        [37.79124, -122.42381],
        [37.79850, -122.44784],
    ],
    "lower_pac_heights": [
        [37.78554, -122.42878],
        [37.78873, -122.44544],
    ],
    "presidio": [
        [37.77805, -122.43959],
        [37.78829, -122.47151],
    ],
    "bayview": [
        [37.710035,-122.408073],
        [137.752258, -122.355251],
    ]
}

# A list of neighborhood names to look for in the Craigslist neighborhood name field. If a listing doesn't fall into
# one of the boxes you defined, it will be checked to see if the neighborhood name it was listed under matches one
# of these.  This is less accurate than the boxes, because it relies on the owner to set the right neighborhood,
# but it also catches listings that don't have coordinates (many listings are missing this info).
NEIGHBORHOODS = ["cow hollow", "pac hts", "pacific heights", "lower haight", "presidio", "twin peaks", "bayview", "bay view", "mission district", "potrero hill", "dogpatch", "chinatown", "china town", "japan town", "japantown"]

## Transit preferences

# The farthest you want to live from a transit stop.
MAX_TRANSIT_DIST = 1 # miles

# Transit stations you want to check against.  Every coordinate here will be checked against each listing,
# and the closest station name will be added to the result and posted into Slack.
TRANSIT_STATIONS = {
    "montgomery_st": [37.7893476,-122.4011439],
    "embarcadero": [37.793185, -122.397027],
    "16th_st_mission": [37.765270, -122.419705],
    "24th_st_mission": [37.752731, -122.418114],
    "glen_park": [37.736106, -122.433054],
    "balboa_park": [37.721809, -122.447468],
    "powell_st": [37.784706, -122.407976],
    "civic_center": [37.779985, -122.414086],
}

## Search type preferences

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
CRAIGSLIST_HOUSING_SECTION = 'apa'

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 20 * 60 # 20 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#housing"

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")

# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass
