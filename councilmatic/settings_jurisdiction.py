# These are all the settings that are specific to a jurisdiction

###############################
# These settings are required #
###############################

OCD_JURISDICTION_ID = 'ocd-jurisdiction/country:us/state:pa/place:pittsburgh'
# OCD_CITY_COUNCIL_ID = 'ocd-organization/ef168607-9135-4177-ad8e-c1f7a4806c3a' -- no ID for Pittsburgh at present (2/14/19)
OCD_CITY_COUNCIL_NAME = 'Pittsburgh City Council'
CITY_COUNCIL_NAME = 'Pittsburgh City Council'
LEGISLATIVE_SESSIONS = ['2019'] # the last one in this list should be the current legislative session
CITY_NAME = 'Pittsburgh'
CITY_NAME_SHORT = 'Pittsburgh'

# VOCAB SETTINGS FOR FRONT-END DISPLAY
CITY_VOCAB = {
    'MUNICIPAL_DISTRICT': 'District',       # e.g. 'District'
    'SOURCE': 'Pittsburgh City Clerk',
    'COUNCIL_MEMBER': 'Council Member',       # e.g. 'Council Member'
    'COUNCIL_MEMBERS': 'Council Members',      # e.g. 'Council Members'
    'EVENTS': 'Meetings',    # label for the events listing, e.g. 'Events'
}

APP_NAME = 'pittsburgh'


#########################
# The rest are optional #
#########################

# this is for populating meta tags
SITE_META = {
    'site_name' : 'Pittsburgh Councilmatic',       # e.g. 'Pittsburgh Councilmatc'
    'site_desc' : 'City Council, demystified. Keep tabs on Pittsburgh legislation, votes, & hearings.',       # e.g. 'City Council, demystified. Keep tabs on Pittsburgh legislation, aldermen, & meetings.'
    'site_author' : 'Pittsburgh Digital Services Studio',     # e.g. 'DataMade'
    'site_url' : '',        # TODO--e.g. 'https://chicago.councilmatic.org'
    'twitter_site': '@PghDigitalStudio',     # e.g. '@DataMadeCo'
    'twitter_creator': '@PghDigitalStudio',  # e.g. '@DataMadeCo'
}

LEGISTAR_URL = 'https://pittsburgh.legistar.com/Legislation.aspx' # e.g. 'https://chicago.legistar.com/Legislation.aspx'


# this is for the boundaries of municipal districts, to add
# shapes to posts & ultimately display a map with the council
# member listing. the boundary set should be the relevant
# slug from the ocd api's boundary service
# available boundary sets here: http://ocd.datamade.us/boundary-sets/
BOUNDARY_SET = ''           # e.g. 'chicago-wards-2015'

# this is for configuring a map of council districts using data from the posts
# set MAP_CONFIG = None to hide map
MAP_CONFIG = {
    'center': [40.4406, -79.9959],
    'zoom': 10,
    'color': "#54afe8",
    'highlight_color': "#C00000",
}


FOOTER_CREDITS = [
    {
        'name':     'Pittsburgh Digital Services Studio', # e.g. 'DataMade'
        'url':      'https://www.youtube.com/watch?v=dQw4w9WgXcQ', # e.g. 'http://datamade.us'
        # 'image':    '', # e.g. 'datamade-logo.png'
    },
]

# this is the default text in search bars
SEARCH_PLACEHOLDER_TEXT = 'Search council' # e.g. 'police, zoning, O2015-7825, etc.'



# these should live in APP_NAME/static/
IMAGES = {
    'favicon': 'images/favicon.ico',
    'logo': 'images/2000px-Flag_of_Pittsburgh,_Pennsylvania.svg.png',
}




# THE FOLLOWING ARE VOCAB SETTINGS RELEVANT TO DATA MODELS, LOGIC
# (this is diff from VOCAB above, which is all for the front end)

# this is the name of the meetings where the entire city council meets
# as stored in legistar
CITY_COUNCIL_MEETING_NAME = 'City Council'

# this is the name of the role of committee chairs, e.g. 'CHAIRPERSON' or 'Chair'
# as stored in legistar
# if this is set, committees will display chairs
COMMITTEE_CHAIR_TITLE = 'Chairperson'

# this is the anme of the role of committee members,
# as stored in legistar
COMMITTEE_MEMBER_TITLE = 'Member'

# this is for convenience, & used to populate a table
# describing legislation types on the default 'About' page template
LEGISLATION_TYPE_DESCRIPTIONS = [
    {
        'name': 'Appointment-Informing',
        'search_term': 'Appointment',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': '',
    },
    {
        'name': 'Appointment-Requiring Vote',
        'search_term': 'Appointment',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': '',
    },
    {
        'name': 'Certificate of Election',
        'search_term': 'Election',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': '',
    },
    {
        'name': 'Communication',
        'search_term': 'Communication',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': '',
    },
    {
        'name': 'Executive Order',
        'search_term': 'Executive Order',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': '',
    },
    {
        'name': 'Invoices',
        'search_term': 'Invoices',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': '',
    },
    {
        'name': 'Report',
        'search_term': 'Report',
        'fa_icon': 'dollar',
        'html_desc': True,
        'desc': 'Submissions of official reports by departments, boards and sister agencies.',
    },
    {
        'name': 'Petition',
        'search_term': 'Petition',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': '',
    },
    {
        'name': 'Post Agenda',
        'search_term': 'Post Agenda',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': '',
    },
    {
        'name': 'Proclamation',
        'search_term': 'Proclamation',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': ''
    },
    {
        'name': 'Public Hearing',
        'search_term': 'Public Hearing',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': ''
    },
    {
        'name': 'Remarks',
        'search_term': 'Remarks',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': ''
    },
    {
        'name': 'Report',
        'search_term': 'Report',
        'fa_icon': 'dollar',
        'html_desc': True,
        'desc': 'Submissions of official reports by departments, boards and sister agencies.',
    },
    {
        'name': 'Resolution',
        'search_term': 'Resolution',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': ''
    },
    {
        'name': 'Sister City Inventory',
        'search_term': 'Sister City',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': ''
    },
    {
        'name': 'Small Games of Chance',
        'search_term': 'Small Games of Chance',
        'fa_icon': 'dollar',
        'html_desc': True,
        'desc': ''
    },
    {
        'name': 'Transcripts - Public Hearing',
        'search_term': 'Transcripts - Public Hearing',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': ''
    },
    {
        'name': 'Transcripts - Regular Meeting',
        'search_term': 'Transcripts - Regular Meeting',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': ''
    },
    {
        'name': 'Transcripts - Special Council Meeting',
        'search_term': 'Transcripts - Special Council Meeting',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': ''
    },
    {
        'name': 'Veto Message',
        'search_term': 'Veto Message',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': ''
    },
    {
        'name': 'Will of Council',
        'search_term': 'Will of Council',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': ''
    }
]

# these keys should match committee slugs
COMMITTEE_DESCRIPTIONS = {
    # e.g. "committee-on-aviation" : "The Committee on Aviation has jurisdiction over matters relating to aviation and airports.",
    "committee-on-finance-and-law" : "The Committee on Finance and Law has charge of and jurisdiction over all ordinances, resolutions, bills, papers and other matters relating to: Bonds and Debt Issuance; City Banking/Investment; Creation of Offices or Positions of any kind; Department of Finance; Enterprise Resource System; Equal Opportunity Review Commission (EORC); Ethics; Law Department; Multi-year Capital Improvement Program; Office of Management and Budget (OMB) Operating & Capital Budgets; Pension Fiscal; Real Estate; Taxation; Treasurer and such other business as may be referred to it by the Council, provided, however, that where money has been specifically appropriated by the Council for any of the purposes of the departments of the City government, that said committee shall then have complete charge and jurisdiction. Council Chairperson: Rev. Ricky V. Burgess",
    "committee-on-public-safety-services": "The Committee on Public Safety Services has charge of and jurisdiction over all ordinances, resolutions, bills, papers, and other matters of every kind pertaining to: Bureau of Animal Control; Permits; Licenses & Inspections; Bureau of Fire; Bureau of Police; Citizens Police Review Board (CPRB); Department of Public Safety; Emergency Management Agency (EMA); Emergency Medical Services (EMS); Emergency Operations and Communications; Homeland Security; Weed and Seed. Council Chairperson: R. Daniel Lavelle",
    "committee-on-public-works": "The Committee on Public Works has charge of and jurisdiction over all ordinances, resolutions, bills, or papers affecting or pertaining to: Bureau of Administration; Bureau of Engineering, Bureau of Environmental Services, Bureau of Operations, Construction, Department of Public Works, Environmental Services and Control, Facilities Operation and Maintenance (Not Parks or Recreation related), Forestry, Franchises and Rights of Way to Corporations, Public Right-of-Way Maintenance, Shade Tree, Streets Lighting. Council Chairperson: Theresa Kail-Smith",
    "committee-on-human-resources": "The Committee on Human Resources has charge of and jurisdiction over all ordinances, resolutions, bills, or papers affecting or pertaining to: Benefits; Department of Personnel and Civil Service; Equal Employment Opportunity Commission (EEOC); Human Relations Commission (HRC); Job Training Partnership Act (JTPA); Office of Municipal Investigation (OMI); Payroll Administration/System; Pension Benefits Administration; Personnel (inclusive of Salaries and Employment Numbers). Council Chairperson: Darlene Harris",
    "committee-on-urban-recreation": "The Committee on Urban Recreation has charge of and jurisdiction over all ordinances, resolutions, bills, or papers pertaining to: Department of Parks and Recreation (CitiParks); Greenways; Libraries; Park Programming; Recreation Facilities Maintenance; Senior Centers; Programming and Advisory Council; Special Events; Trails; Youth Policy. Council Chairperson: Anthony Coghill",
    "committee-on-innovation-performance-and-management": "The Committee on Innovation, Performance and Asset Management has charge of and jurisdiction over all ordinances, resolutions, bills, papers, and other matters relating to: 311 Mayor's Response Center; City Cable Channel; Department of Innovation & Performance; Facilities Inventory and Management; Fleet Maintenance, Repair, and Alteration; Purchasing and B Contracts; Information Technology; Data Collection and Analysis; Operational Performance Targets; Sustainabillity Initiatives; Professional Management Systems. Council Chairperson: Erika Strassburger",
    "committee-on-intergovernmental-affairs": "The Committee on Intergovernmental Affairs has charge of and jurisdiction over all ordinances, resolutions, bills, or papers affecting or pertaining to: Allegheny Regional Assets District (ARAD); Authorities - Agreements; County; Federal; Local governmental cooperation agreements; Liquor Licenses; Pennsylvania League of Cities and Municipalities; Port of Pittsburgh; School Boards; State; Tourism - Visit Pittsburgh. Council Chairperson: Corey O'Connor",
    "committee-on-hearings": "The Committee on Hearings has charge of the jurisdiction and scheduling of: Appointments and Reappointments; Executive Sessions; Public Hearings; Public Meetings. Council Chairperson: Bruce Kraus",
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
    'peduto-bill': {'source': 'pittsburghpa.gov', 'image': 'http://pittsburghpa.gov/images/mayor-profile/peduto.jpg'},
    'burgess-ricky': {'source': 'pittsburghpa.gov', 'image': 'manual-headshots/burgess-ricky.jpg'},
    'coghill-anthony': {'source': 'pittsburghpa.gov', 'image': 'manual-headshots/coghill-anthony.jpg'},
    'gross-deb': {'source': 'pittsburghpa.gov', 'image': 'manual-headshots/gross-deb.jpg'},
    'harris-darlene': {'source': 'pittsburghpa.gov', 'image': 'manual-headshots/harris-darlene.jpg'},
    'kail-smith-theresa': {'source': 'pittsburghpa.gov', 'image': 'manual-headshots/kail-smith-theresa.jpg'},
    'kraus-bruce': {'source': 'pittsburghpa.gov', 'image': 'manual-headshots/kraus-bruce.jpg'},
    'lavelle-daniel-r': {'source': 'pittsburghpa.gov', 'image': 'manual-headshots/lavelle-daniel-r.jpg'},
    'oconnor-corey': {'source': 'pittsburghpa.gov', 'image': 'manual-headshots/oconnor-corey.jpg'},
    'strassburger-erika': {'source': 'pittsburghpa.gov', 'image': 'manual-headshots/strassburger-erika.jpg'},
}


CONTACT_INFO = {
    'peduto-bill': {'twitter': {'handle': '@billpeduto', 'url': 'https://twitter.com/billpeduto'}, 'phone': '', 'email': ''},
    'burgess-ricky': {'twitter': {'handle': '@RevBurgessPgh', 'url': 'https://twitter.com/RevBurgessPgh'}, 'phone': '412-255-2137/412-255-8658', 'email': 'reverend.burgess@pittsburghpa.gov'},
    'coghill-anthony': {'twitter': {'handle': '@CoghillAnthony', 'url': 'https://twitter.com/CoghillAnthony'}, 'phone': '412-255-2131', 'email': 'kaitlyn.fisher@pittsburghpa.gov'},
    'gross-deb': {'twitter': {'handle': '@DebGrosspgh', 'url': 'https://twitter.com/DebGrosspgh'}, 'phone': '412-255-2140', 'email': 'district7@pittsburghpa.gov'},
    'harris-darlene': {'twitter': {'handle': '@Darlene4Pgh', 'url': 'https://twitter.com/Darlene4Pgh'}, 'phone': '412-255-2135', 'email': ''},
    'kail-smith-theresa': {'twitter': {'handle': '@tkailsmith', 'url': 'https://twitter.com/tkailsmith'}, 'phone': '412-255-8963', 'email': 'jill.harris@pittsburghpa.gov'},
    'kraus-bruce': {'twitter': {'handle': '@BruceKraus', 'url': 'https://twitter.com/BruceKraus'}, 'phone': '412-255-2130', 'email': 'robert.charland@pittsburghpa.gov'},
    'lavelle-daniel-r': {'twitter': {'handle': '@RDLavelle', 'url': 'https://twitter.com/RDLavelle'}, 'phone': '412-255-2134', 'email': 'cassandra.williams@pittsburghpa.gov'},
    'oconnor-corey': {'twitter': {'handle': '@CoreyOConnorPGH', 'url': 'https://twitter.com/CoreyOConnorPGH'}, 'phone': '412-255-8965', 'email': 'connie.sukernek@pittsburghpa.gov'},
    'strassburger-erika': {'twitter': {'handle': '@erikastrassbrgr', 'url': 'https://twitter.com/erikastrassbrgr'}, 'phone': '412-255-2133', 'email': 'erika.strassburger@pittsburghpa.gov'},
}
# notable positions that aren't district representatives, e.g. mayor & city clerk
# keys should match person slugs
EXTRA_TITLES = {
    'peduto-bill': 'Mayor',
}

USING_NOTIFICATIONS = False

