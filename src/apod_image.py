from typing import Protocol

from PIL import Image


class ApodImageDownloaderProtocol(Protocol):
    """Defines the way apod images must be dowloaded and treated"""

    image_url: str

    def get_image() -> Image:
        ...

    def save_image(path: str, name: str) -> None:
        ...
