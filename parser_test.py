import parser


def test_parse_page():
    parsed = parser.parse_page('<html><head><title>wow</title></head></html>')

    assert str(parsed.__class__) == "<class 'bs4.BeautifulSoup'>"
    assert parsed.title.string == 'wow'
