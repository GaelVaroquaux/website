#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ga\xebl Varoquaux'
SITENAME = u'Ga\xebl Varoquaux'
SITEURL = 'https://gael-varoquaux.info'
# The below gets overiden in the publishconf.py
SITEURL = 'http://localhost:8000/'
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
          #('Selected posts', 'tag/selected.html'),
          ('Latest posts', 'index.html#posts'),
          ('About me', 'about.html'),
          )

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'


PAGE_URL = '{slug}.html'
URL = '{category}/{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

DEFAULT_PAGINATION = 20
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
# The readtime plugin
import readtime
PLUGINS=[readtime, ]

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
    ('Google scholar', 'fa-solid fa-graduation-cap',
     'http://scholar.google.fr/citations?user=OGGu384AAAAJ', ''),
    #('twitter', 'fa-brands fa-twitter-square', 'https://twitter.com/GaelVaroquaux', ''),
    ('bluesky', 'fa-brands fa-bluesky', 'https://bsky.app/profile/gaelvaroquaux.bsky.social', ''),
    ('GitHub', 'fa-brands fa-github', GITHUB_URL, ''),
    ("Artwork", 'fa-solid fa-camera-retro',
     'http://www.flickriver.com/photos/gaelvaroquaux/popular-interesting/',
"""<div class="extra"><div id="flickrstream"></div></div>"""),
)
# Linkedin, slideshare

# My gravatar
PROFILE_IMAGE_URL = 'https://gael-varoquaux.info/images/gael.png'

# The pretty picture for the sidebar
# Now done in the CSS, "pure.css", to enable overide in given pages.
#COVER_IMG_URL = 'http://gael-varoquaux.info/images/cover_img.jpg'

TAGLINE = "computer / data / health science"

# global metadata to all the contents
DEFAULT_METADATA = (('email', 'gael.varoquaux@normalesup.org'),
                    ('profile_image', PROFILE_IMAGE_URL))


# A function used as jinja filter to find a default image
# Used for opengraph summary
import bs4

def findimage(string):
    soup = bs4.BeautifulSoup(string, 'html.parser')
    img = soup.find('img')
    if img is None:
        return ""
    return img['src']

JINJA_FILTERS = {'findimage': findimage}

