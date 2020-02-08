#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ga\xebl Varoquaux'
SITENAME = u'Ga\xebl Varoquaux'
SITEURL = 'http://gael-varoquaux.info'
AUTHOR_EMAIL = 'gael.varoquaux@normalesup.org'
GITHUB_URL = 'https://github.com/GaelVaroquaux/'
TWITTER_USERNAME = 'GaelVaroquaux'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Posts in the future get assigned a draft status
WITH_FUTURE_DATES = True


# Blogroll
MENUITEMS =  (
          ('Selected posts', 'tag/selected.html'),
          ('Latest posts', 'index.html#posts'),
          ('About me', 'about.html'),
          )

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'


PAGE_URL = '{slug}.html'
URL = '{category}/{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 50

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = ['images', 'science/attachments', 'programming/attachments',
                'personnal/attachments', 'pages/attachments']

IGNORE_FILES = ['content/science/attachments/citations.html',
                '.#*',]

# apply the typogrify post-processing
TYPOGRIFY = False

# Better settings for the rst generation
DOCUTILS_SETTINGS = dict(smart_quotes=True)

USE_FOLDER_AS_CATEGORY = True

import logging
LOG_FILTER = [(logging.WARN, 'Empty alt attribute for image.*'),
              (logging.ERROR, 'Skipping science/attachments/citations.html')]

import sys
sys.path.append('.')
# https://raw.githubusercontent.com/getpelican/pelican-plugins/master/readtime/readtime.py
import readtime
PLUGINS=[readtime]

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
     'http://scholar.google.fr/citations?user=OGGu384AAAAJ', ''),
    ('twitter', 'twitter-square', 'https://twitter.com/GaelVaroquaux', ''),
    ('GitHub', 'github', GITHUB_URL, ''),
    ("Artwork", 'camera-retro',
     'http://www.flickriver.com/photos/gaelvaroquaux/popular-interesting/',
"""<div class="extra"><div id="flickrstream"></div></div>"""),
)
# Linkedin, slideshare

# My gravatar
PROFILE_IMAGE_URL = 'http://gael-varoquaux.info/images/gael.png'

# The pretty picture for the sidebar
# Now done in the CSS, "pure.css", to enable overide in given pages.
#COVER_IMG_URL = 'http://gael-varoquaux.info/images/cover_img.jpg'

TAGLINE = "computer / data / brain science"

# global metadata to all the contents
DEFAULT_METADATA = (('email', 'gael.varoquaux@normalesup.org'),
                    ('profile_image', PROFILE_IMAGE_URL))


