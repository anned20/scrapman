import click
import logging
from os import path
from page import get_page
from parser import parse_page
from logger import logger
from serializer import serializers


@click.command()
@click.option('--debug/--no-debug', help='Debug mode', default=False)
@click.option('--url', prompt='URL to crawl', help='URL to crawl')
@click.option('--selector', prompt='Selector for the elements',
              help='Selector for the elements')
@click.option('--output-type', type=click.Choice(serializers.keys()),
              default='json')
@click.option('--output-file', default='-',
              help='File to output the result into. Use "-" for stdout')
def main(debug, url, selector, output_type, output_file):
    logging.basicConfig(level=logging.DEBUG if debug else logging.WARNING)

    logger.debug('Debug mode is on')

    logger.debug(f'Using {url} as URL')
    logger.debug(f'Using {selector} as selector')

    page = get_page(url)
    soup = parse_page(page)

    elements = soup.select(selector)

    logger.debug(f'Using {output_type} as serializer')

    serializer = serializers.get(output_type, 'No such serializer')

    logger.debug(f'Serializing {len(elements)} elements')

    output = serializer(elements)

    if output_file == '-':
        logger.debug('Printing output')
        print(output)

        return

    with open(path.abspath(output_file), 'w') as _file:
        logger.debug(f'Writing output to {output_file}')
        _file.write(output)


if __name__ == '__main__':
    main()
