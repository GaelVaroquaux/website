#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ga\xebl Varoquaux'
SITENAME = u'Ga\xebl Varoquaux'
SITEURL = 'http://gael-varoquaux.info'
AUTHOR_EMAIL = 'gael.varoquaux@normalesup.org'
GITHUB_URL = 'https://github.com/GaelVaroquaux/'
TWITTER_USERNAME = 'GaelVaroquaux'
DISQUS_SITENAME = "gaelvaroquaux"

# global metadata to all the contents
DEFAULT_METADATA = (('email', 'gael.varoquaux@normalesup.org'),)

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

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
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'science/attachments', 'programming/attachments',
                'personnal/attachments']

# apply the typogrify post-processing
TYPOGRIFY = False

USE_FOLDER_AS_CATEGORY = True

import logging
LOG_FILTER = [(logging.WARN, 'Empty alt attribute for image.*')]

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
    ('GitHub', 'github', GITHUB_URL),
    ('flickr', 'flickr', 'https://www.flickr.com/photos/GaelVaroquaux'),
)
# Linkedin, slideshare

# My gravatar
PROFILE_IMAGE_URL = 'http://gael-varoquaux.info/images/gael.png'

# The pretty picture for the sidebar
COVER_IMG_URL = 'http://gael-varoquaux.info/images/cover_img.jpg'

TAGLINE = "computer / data / brain science"
