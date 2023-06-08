### Scrap over-few-hundred-chapters webnovelinto one nice and tidy file, ready to generate ebook of any format you can possibly want via pandoc!

import utils
import requests
from bs4 import BeautifulSoup
import re
import random
import time
import json
import argparse


# Provide WEBNOVEL_HTTP

WEBNOVEL_URL = "https://readnovelfull.com/omniscient-readers-viewpoint-v1.html"
WEBNOVEL_URL_B = "https://readnovelfull.com/omniscient-readers-viewpoint-v1.html#tab-description-title"
WEBNOVEL_URL_C = "https://bestlightnovel.com/novel_888151160/chapter_68"
WEBNOVEL_URL_D = "https://www.readwn.com/novel/every-day-i-wake-up-and-see-myself-selling-stupid.html"


# List of http for all available chapters is created
# There's possibility for few modes of scraping to be implemented for chapters' list and mode A will be set automatically

# Invisible captcha doesn't need to be avoided since it's only present on some of the websites

# Content of chapters is scraped via BeautifulSoup and supplemented with Pandoc Markdown

# Save txt or json with Pandoc Markdown ready to be converted

# Optionally: if Pandoc is available, provide parameters and create ebook inside this very script

# Docelowy efekt po uruchomieniu: wpisujesz w konsolę python back-webnovel-up http.//blablabla.html -epub i wsio, dalej się samo robi i do tego jest
# bibilioteka argparse


