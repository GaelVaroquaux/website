#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ga\xebl Varoquaux'
SITENAME = u'Ga\xebl Varoquaux'
SITEURL = 'http://gael-varoquaux.info'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# global metadata to all the contents
DEFAULT_METADATA = (('email', 'gael.varoquaux@normalesup.org'),)

AUTHOR_EMAIL = 'gael.varoquaux@normalesup.org'

STATIC_PATHS = ['images']

###############################################################################
# For the pure theme

# The theme itself
THEME = "pure"

# Links in the sidebar: this is not standard, it is for my own modified
# theme, as it has 3 entries per item:
# - The link title
# - The icon name on http://fontawesome.io/icons/ after stripping 'fa-'
# - The link itself
SOCIAL = (
    ('Google scholar', 'graduation-cap',
     'http://scholar.google.fr/citations?user=OGGu384AAAAJ'),
    ('twitter', 'twitter-square', 'https://twitter.com/GaelVaroquaux'),
    ('Github', 'github', 'https://github.com/GaelVaroquaux/'),
    ('flickr', 'flickr', 'https://www.flickr.com/photos/GaelVaroquaux'),
)
# Linkedin, slideshare

# My gravatar
PROFILE_IMAGE_URL = 'images/gael.png'

# The pretty picture for the sidebar
COVER_IMG_URL = 'images/cover_img.jpg'

TAGLINE = "computer / data / brain science"
