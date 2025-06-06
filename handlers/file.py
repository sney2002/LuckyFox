from url import URL
from request import RequestHandler
from typing import Optional
import os

class FileRequest(RequestHandler):
    def fetch(self, url: 'URL', headers: Optional[dict[str, str]] = None) -> str:

        if os.path.isdir(url.path):
            return '\n'.join(os.listdir(url.path))

        try:
            with open(url.path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {url.path}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while reading the file: {e}")