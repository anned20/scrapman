from bs4 import BeautifulSoup
from logger import logger


def parse_page(text):
    """Parse the page and return a BeautifulSoup object
    Keyword Arguments:
    text : string
    """
    soup = BeautifulSoup(text, 'html.parser')

    logger.debug(f'Title of page is {soup.title.string}')

    return soup
