# Scrapman

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/anned20/scrapman.svg)
![GitHub issues](https://img.shields.io/github/issues/anned20/scrapman.svg)
![GitHub pull requests](https://img.shields.io/github/issues-pr/anned20/scrapman.svg)
![GitHub](https://img.shields.io/github/license/anned20/scrapman.svg)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)


Scrapman is a Python script to crawl a list of elements from a specified URL with a specified selector.

## Getting started

Clone this repository:

```shell
git clone https://github.com/anned20/scrapman.git
```

Install the dependencies:

```shell
pip install -r requirements.txt
```

You are now ready to use Scrapman:

```shell
python scrapman.py --help
```

You should see something like:

```
Usage: scrapman.py [OPTIONS]

Options:
--debug / --no-debug           Debug mode
--url TEXT                     URL to crawl
--selector TEXT                Selector for the elements
--output-type [dict|json|csv]
--output-file TEXT             File to output the result into. Use "-" for
stdout
--help                         Show this message and exit.

```

## Testing

To run the tests you use [pytest](https://pytest.org)

Execute them with `pytest` in the project directory

## Built with

- [requests](http://docs.python-requests.org/en/master/) - Getting the webpage
- [click](https://github.com/mitsuhiko/click) - Parsing command line options
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - Parsing the HTML of the webpage

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


