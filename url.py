from dataclasses import dataclass
import re

port_regex = re.compile(r':(\d+)$')
driver_letter_regex = re.compile(r'^[a-zA-Z]:')
scheme_default_ports = {
    'http': 80,
    'https': 443,
}

@dataclass
class URL:
    port: int = 0
    scheme: str = ''
    host: str = ''
    path: str = ''

    def __init__(self, url: str):
        if url.startswith('data:'):
            self.scheme = 'data'
            self.path = url[5:]
            return

        self.scheme, url = url.split('://', 1)
        self.port = scheme_default_ports.get(self.scheme, 0)

        if not '/' in url:
            url = url + '/'

        self.host, url = url.split('/', 1)

        if self.has_custom_port():
            self.host, port = self.host.split(':', 1)
            self.port = int(port)

        if self.scheme == 'file':
            self.__set_file_path(url)
        else:
            self.path = '/' + url

    def has_custom_port(self) -> bool:
        return port_regex.search(self.host) is not None

    def __set_file_path(self, url: str):
        if url[0] == '/' and driver_letter_regex.match(url[1:]):
            self.path = url[1:]
        elif driver_letter_regex.match(self.host):
            self.path = self.host + '/' + url
        else:
            self.path = url
        self.host = ''

    def __str__(self):
        return f"{self.scheme}://{self.host}{self.path}"

    def __repr__(self):
        return f"URL(scheme='{self.scheme}', host='{self.host}', port={self.port}, path='{self.path}')"