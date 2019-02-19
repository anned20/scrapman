from serializer import serializers

class MockTag:
    def __init__(self, name, attrs, string):
        self.name   = name
        self.attrs  = attrs
        self.string = string

    def __str__(self):
        return f'<{self.name}>{self.string}</{self.name}>'


def test_serialize_dict():
    test_list = [
        MockTag('a', {'class': 'some classes'}, 'I am a link')
    ]

    serializer = serializers.get('dict')

    assert serializer(test_list) == [
        {
            'name': 'a',
            'attributes': {
                'class': 'some classes',
            },
            'content': 'I am a link',
            'source': '<a>I am a link</a>',
        }
    ]


def test_serialize_json():
    test_list = [
        MockTag('a', {'class': 'some classes'}, 'I am a link')
    ]

    serializer = serializers.get('json')

    assert serializer(test_list) == '[{"name": "a", "attributes": {"class": "some classes"}, "content": "I am a link", "source": "<a>I am a link</a>"}]'


def test_serialize_csv():
    test_list = [
        MockTag('a', {'class': 'some classes'}, 'I am a link')
    ]

    serializer = serializers.get('csv')

    assert '"name","attributes","content","source"' in serializer(test_list)
