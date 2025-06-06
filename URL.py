
class URL:
    def __init__(self, url: str):
        self.scheme, url = url.split('://', 1)

        if self.scheme == 'http':
            self.port = 80
        elif self.scheme == 'https':
            self.port = 443

        if not '/' in url:
            url = url + '/'

        self.host, url = url.split('/', 1)

        if ':' in self.host:
            self.host, port = self.host.split(':', 1)
            self.port = int(port)
        
        self.path = '/' + url

    def __str__(self):
        return f"{self.scheme}://{self.host}{self.path}"