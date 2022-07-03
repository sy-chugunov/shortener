import string

from aiohttp import web
import validators


def get_url(data):
    try:
        url = data["url"]
        is_valid = validators.url(url)
    except KeyError:
        raise web.HTTPBadRequest(text="`url` field is not set in request data")

    if not is_valid:
        raise web.HTTPBadRequest(text="`url` is invalid")

    return url


CHARS = string.ascii_letters + string.digits


def generate_short_id(next_id, alphabet=CHARS):
    # offset between next_id and alphabet indexes
    index = next_id - 1

    if index == 0:
        return alphabet[0]

    base = len(alphabet)
    result = []

    while index:
        result.append(alphabet[index % base])
        index = index // base

    result.reverse()

    return "".join(result)
