# These are all the settings that are specific to a jurisdiction

###############################
# These settings are required #
###############################

OCD_JURISDICTION_ID = '{{cookiecutter.ocd_jurisdiction_id}}'
OCD_CITY_COUNCIL_ID = '{{cookiecutter.ocd_city_council_id}}'
CITY_COUNCIL_NAME = '{{cookiecutter.city_council_name}}'
LEGISLATIVE_SESSIONS = {{cookiecutter.legislative_sessions.years}}
CITY_NAME = '{{cookiecutter.city_name}}'
CITY_NAME_SHORT = '{{cookiecutter.city_name_short}}'

# VOCAB SETTINGS FOR FRONT-END DISPLAY
CITY_VOCAB = {
    'MUNICIPAL_DISTRICT': '{{cookiecutter.city_vocab_municipal_district}}',
    'SOURCE': '{{cookiecutter.city_vocab_source}}',
    'COUNCIL_MEMBER': '{{cookiecutter.city_vocab_council_member}}',
    'COUNCIL_MEMBERS': '{{cookiecutter.city_vocab_council_members}}',
    'EVENTS': '{{cookiecutter.city_vocab_events}}',
}

APP_NAME = '{{cookiecutter.city}}'


#########################
# The rest are optional #
#########################

# this is for populating meta tags
SITE_META = {
    'site_name': '{{cookiecutter.site_meta_site_name}}',
    'site_desc': '{{cookiecutter.site_meta_site_desc}}',
    'site_author': '{{cookiecutter.site_meta_site_author}}',
    'site_url': '{{cookiecutter.site_meta_site_url}}',
    'twitter_site': '{{cookiecutter.site_meta_twitter_site}}',
    'twitter_creator': '{{cookiecutter.site_meta_twitter_creator}}',
}

LEGISTAR_URL = ''           # e.g. 'https://chicago.legistar.com/Legislation.aspx'


# this is for the boundaries of municipal districts, to add
# shapes to posts & ultimately display a map with the council
# member listing. the boundary set should be the relevant
# slug from the ocd api's boundary service
# available boundary sets here: http://ocd.datamade.us/boundary-sets/
BOUNDARY_SET = ''           # e.g. 'chicago-wards-2015'

# this is for configuring a map of council districts using data from the posts
# set MAP_CONFIG = None to hide map
MAP_CONFIG = {
    'center': [41.8369, -87.6847],
    'zoom': 10,
    'color': "#54afe8",
    'highlight_color': "#C00000",
}


FOOTER_CREDITS = [
    {
        'name':     '', # e.g. 'DataMade'
        'url':      '', # e.g. 'http://datamade.us'
        'image':    '', # e.g. 'datamade-logo.png'
    },
]

# this is the default text in search bars
SEARCH_PLACEHOLDER_TEXT = '' # e.g. 'police, zoning, O2015-7825, etc.'


# these should live in APP_NAME/static/
IMAGES = {
    'favicon': 'images/favicon.ico',
    'logo': 'images/logo.png',
}


# THE FOLLOWING ARE VOCAB SETTINGS RELEVANT TO DATA MODELS, LOGIC
# (this is diff from VOCAB above, which is all for the front end)

# this is the name of the meetings where the entire city council meets
# as stored in legistar
CITY_COUNCIL_MEETING_NAME = 'City Council'

# this is the name of the role of committee chairs, e.g. 'CHAIRPERSON' or 'Chair'
# as stored in legistar
# if this is set, committees will display chairs
COMMITTEE_CHAIR_TITLE = 'Chairman'

# this is the anme of the role of committee members,
# as stored in legistar
COMMITTEE_MEMBER_TITLE = 'Member'


# this is for convenience, & used to populate a table
# describing legislation types on the default about page template
LEGISLATION_TYPE_DESCRIPTIONS = [
    {
        'name': 'Ordinance',
        'search_term': 'Ordinance',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': '',
    },
    {
        'name': 'Claim',
        'search_term': 'Claim',
        'fa_icon': 'dollar',
        'html_desc': True,
        'desc': '',
    },
]

# these keys should match committee slugs
COMMITTEE_DESCRIPTIONS = {
    # e.g. "committee-on-aviation" : "The Committee on Aviation has jurisdiction over matters relating to aviation and airports.",
}

# these blurbs populate the wells on the committees, events, & council members pages
ABOUT_BLURBS = {
    "COMMITTEES" :      "",
    "EVENTS":           "",
    "COUNCIL_MEMBERS":  "",
}

# these override the headshots that are automatically populated
# the keys should match a person's slug
MANUAL_HEADSHOTS = {
    # e.g. 'emanuel-rahm': {'source': 'cityofchicago.org', 'image': 'manual-headshots/emanuel-rahm.jpg' },
}

# notable positions that aren't district representatives, e.g. mayor & city clerk
# keys should match person slugs
EXTRA_TITLES = {
    # e.g. 'emanuel-rahm': 'Mayor',
}
