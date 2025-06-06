from request import Request
from handlers import HTTPRequest
from url import URL

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
    headers = {
        'User-Agent': 'LuckyFox/1.0'
    }

    Request.register_handler('http', HTTPRequest(headers=headers))
    Request.register_handler('https', HTTPRequest(headers=headers))

    http = HTTPRequest(headers=headers)
    url = URL('https://example.com')
    load(url)