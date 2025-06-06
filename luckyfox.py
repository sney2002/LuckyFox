from request import Request
from handlers import HTTPRequest, FileRequest
from url import URL
import sys

def show(body: str):
    in_tag = False
    for c in body:
        if c == '<':
            in_tag = True
        elif c == '>':
            in_tag = False
        elif not in_tag:
            print(c, end='')

def load(url: URL):
    request = Request()
    body = request.fetch(url)
    show(body)

if __name__ == '__main__':
    url_string = sys.argv[1] if len(sys.argv) > 1 else 'file:///C:/'
    headers = {
        'User-Agent': 'LuckyFox/1.0'
    }

    Request.register_handler('http', HTTPRequest(headers=headers))
    Request.register_handler('https', HTTPRequest(headers=headers))
    Request.register_handler('file', FileRequest())

    http = HTTPRequest(headers=headers)
    url = URL(url_string)

    print(repr(url))

    load(url)