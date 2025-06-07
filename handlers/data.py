from url import URL
from request import RequestHandler
from typing import Optional
import base64

class DataURLRequest(RequestHandler):
    def fetch(self, url: 'URL', headers: Optional[dict[str, str]] = None) -> str:
        mimetype, data = url.path.split(',', 1)

        if mimetype.endswith(';base64'):
            data = base64.b64decode(data).decode('utf-8')

        return data