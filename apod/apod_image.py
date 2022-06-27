import os
from io import BytesIO
from typing import Protocol

import requests
from PIL import Image

from .exceptions import ApodRetrieveError


class ApodImageDownloaderProtocol(Protocol):
    """Defines the way apod images must be dowloaded and treated"""

    image_url: str

    def get_image(self) -> Image:
        ...

    def save_image(self, path: str, name: str) -> None:
        ...


class ApodImageDownloader:
    def __init__(self, image_url: str) -> None:
        self.url = image_url

    def get_image(self) -> Image.Image:
        response = requests.get(self.url)
        if response.status_code != requests.codes.ok:
            raise ApodRetrieveError(
                response, "APOD image was imposible to be downloaded."
            )
        image = Image.open(BytesIO(response.content))
        return image

    def save_image(self, dir_path: str, name: str) -> None:

        full_path = os.path.join(dir_path, name)
        image = self.get_image()
        image.save(full_path, format="jpeg")
