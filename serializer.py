import json
import csv
import io


def serialize_dict(elements):
    """Serialize a list of BS4 tags to Python dict
    Keyword Arguments:
    elements : list
    """
    return [
        {
            'name': el.name,
            'attributes': el.attrs,
            'content': el.string,
            'source': str(el),
        } for el in elements
    ]


def serialize_json(elements):
    """Serialize a list of BS4 tags to JSON
    Keyword Arguments:
    elements : list
    """
    elements = serialize_dict(elements)

    return json.dumps(elements)


def serialize_csv(elements):
    """Serialize a list of BS 4 tags to CSV
    Keyword Arguments:
    elements : list
    """
    elements = serialize_dict(elements)

    output = io.StringIO()

    keys = elements[0].keys()

    dict_writer = csv.DictWriter(output, keys, quoting=csv.QUOTE_ALL)
    dict_writer.writeheader()
    dict_writer.writerows(elements)

    return output.getvalue()


serializers = {
    'dict': serialize_dict,
    'json': serialize_json,
    'csv':  serialize_csv,
}
