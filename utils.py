import requests
from bs4 import BeautifulSoup
import re
import time
import random
import json
import argparse

# MAIN PROGRAM

# GIVEN_URL = str(input("Please provide the URL of Table Of Content subpage of webnovel you wish to back up."))
GIVEN_URL_A = "https://readnovelfull.com/omniscient-readers-viewpoint-v1.html#tab-chapters-title"
GIVEN_URL_B = "https://bestlightnovel.com/novel_888102980"
GIVEN_URL_C = "https://www.readwn.com/novel/omniscient-reader.html"


# REQUEST A PAGE

def get_page_as_soup(page_url):
    randomly_delay_requests()
    page = requests.get(page_url)
    page_soup = BeautifulSoup(page.content, "html.parser")
    return page_soup


def randomly_delay_requests():
    delay = random.randrange(500, 1000) * 0.001
    pass


# FIND A WEBNOVEL TABLE OF CONTENT // UNNECESSARY

def find_main_page_of_webnovel(webnovel_url):
    webnovel_mainpage = ""
    if webnovel_url.rfind(".html") > -1 :
        n = webnovel_url.rfind(".html") + 5
        webnovel_mainpage = webnovel_url[:n]
    elif webnovel_url.rfind(".htm") > -1 : 
        n = webnovel_url.rfind(".htm") + 4
        webnovel_mainpage = webnovel_url[:n]
    else: webnovel_mainpage = find_main_page_of_webnovel_when_not_htm(webnovel_url)
    return webnovel_mainpage


def find_main_page_of_webnovel_when_not_htm(webnovel_url):
    webnovel_mainpage = ""
    n = webnovel_url.rfind("chap")
    cropped = webnovel_url[:n]
    webnovel_mainpage = webnovel_url.rsplit("/", 1)[0]
    return webnovel_mainpage


def use_archivepage_instead_of_mainpage(webnovel_mainpage):
    if webnovel_mainpage.rfind("readnovelfull") > -1 :
        archivepage_readnovelfull = webnovel_mainpage + "#tab-chapters-title"
        webnovel_mainpage = archivepage_readnovelfull
    return webnovel_mainpage


# CREATE TABLE OF CONTENT DICTIONARY FILE

# given_url -> request Table Of Content page -> soupify ->
# -> from soup extract chapterlist part of soup -> extract all the links ->
# -> create dictionary of chapter names and chapter links -> save dict as json file

def create_table_of_content_file(GIVEN_URL):
    given_url_soup = get_page_as_soup(GIVEN_URL)
    chapterlist_sub_soup = find_chapterlist_in_soup(given_url_soup)
    chapterlinks_list = []

    return filename
    

def find_chapterlist_in_soup(some_soup):
    chapterlist_wordings = [
            "list_chapter",
            "list-chapter",
            "chapter-list",
            "chapter_list",
            "tab-content"
            ]
    chapterlist_tag = some_soup.find_all(class_ = chapterlist_wordings)
    return chapterlist_tag


def find_all_links_in_soup(some_soup):
    list_of_links = some_soup.find_all('a')
    return list_of_links


# GET ONE CHAPTER CONTENT



# ADD ONE CHAPTER TO TXT FILE


# FINAL ACTIONS
