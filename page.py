import requests
from logger import logger


def get_page(url):
    """Get source of url
    Keyword Arguments:
    url : string
    """
    logger.debug(f'Getting source for {url}')
    res = requests.get(url)
    logger.debug(f'Status code for {url} is {res.status_code}')

    if res.status_code < 200 or res.status_code >= 300:
        raise Exception(f'''
        Not succesful retrieving {url},
        the status code is {res.status_code}
        ''')

    logger.debug(f'Request succesful, returning text')

    return res.text
