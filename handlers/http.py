from request import RequestHandler
from dataclasses import dataclass, field
from typing import Optional
from url import URL
import socket
import ssl

@dataclass
class HTTPRequest(RequestHandler):
    headers: dict[str, str] = field(default_factory=dict)

    def fetch(self, url: 'URL', headers: Optional[dict[str, str]] = None) -> str:
        s = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_STREAM,
            proto=socket.IPPROTO_TCP
        )

        s.connect((url.host, url.port))

        if url.scheme == 'https':
            ctx = ssl.create_default_context()
            s = ctx.wrap_socket(s, server_hostname=url.host)

        request = 'GET {} HTTP/1.1\r\n'.format(url.path)
        request += 'Host: {}\r\n'.format(url.host)

        for key, value in self.headers.items():
            request += '{}: {}\r\n'.format(key, value)

        request += 'Connection: close\r\n'
        request += '\r\n'

        s.send(request.encode('utf-8'))

        response = s.makefile('r', encoding='utf-8', newline='\r\n')
        
        status_line = response.readline()

        version, status, explanation = status_line.split(' ', 2)

        response_headers = {}

        while True:
            line = response.readline()
            if line == '\r\n':
                break
            header, value = line.split(':', 1)
            response_headers[header.casefold()] = value.strip()

        assert 'transfer-encoding' not in response_headers
        assert 'content-encoding' not in response_headers

        content = response.read()
        s.close()

        return content
