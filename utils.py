import requests
from bs4 import BeautifulSoup
import re
import time
import random



def get_chapterlist(WEBNOVEL_URL):
    CHAPTER_URLS_LIST = ""
    WEBNOVEL_MAINPAGE = find_main_page_of_webnovel(WEBNOVEL_URL)
    SUBPAGE_SOUP = get_subpage_as_soup(WEBNOVEL_MAINPAGE)
    return CHAPTER_URLS_LIST


def find_main_page_of_webnovel(WEBNOVEL_URL):
    WEBNOVEL_MAINPAGE = ""
    if WEBNOVEL_URL.rfind(".html") > -1 :
        n = WEBNOVEL_URL.rfind(".html") + 5
        WEBNOVEL_MAINPAGE = WEBNOVEL_URL[:n]
    elif WEBNOVEL_URL.rfind(".htm") > -1 : 
        n = WEBNOVEL_URL.rfind(".htm") + 4
        WEBNOVEL_MAINPAGE = WEBNOVEL_URL[:n]
    else: WEBNOVEL_MAINPAGE = find_main_page_of_webnovel_when_not_htm(WEBNOVEL_URL)
    return WEBNOVEL_MAINPAGE


def find_main_page_of_webnovel_when_not_htm(WEBNOVEL_URL):
    WEBNOVEL_MAINPAGE = ""
    n = WEBNOVEL_URL.rfind("chap")
    cropped = WEBNOVEL_URL[:n]
    WEBNOVEL_MAINPAGE = WEBNOVEL_URL.rsplit("/", 1)[0]
    return WEBNOVEL_MAINPAGE


def use_archivepage_instead_of_mainpage(WEBNOVEL_MAINPAGE):
    if WEBNOVEL_MAINPAGE.rfind("readnovelfull") > -1 :
        archivepage_readnovelfull = WEBNOVEL_MAINPAGE + "#tab-chapters-title"
        WEBNOVEL_MAINPAGE = archivepage_readnovelfull
    return WEBNOVEL_MAINPAGE


def get_subpage_as_soup(SUBPAGE_URL):
    subpage = requests.get(SUBPAGE_URL)
    SUBPAGE_SOUP = BeautifulSoup(subpage.content, "html.parser")
    return SUBPAGE_SOUP


def find_chapters_in_soup_A(SUBPAGE_SOUP):
    SUBPAGE_SOUP.find_all(re.compile("chapter.*list"))
    return CHAPTER_URLS_LIST


def randomly_delay_requests(self):
    delay = random.randrange(500, 2000) * 0,001
    time.sleep(delay)


def is_chapterlist_valid():
    validness_of_chapterlist = False
    return validness_of_chapterlist


def markdown_chapter():
    pass


def create_one_file():
    pass


def add_chapter_to_one_file():
    pass



