"""
The apod package pretend to create a easy interface to interact with the apod web page. It can download the apod image of the day
using the get_apod_image function.
"""

__version__ = "0.0.1"

from .apod_web import ApodExplorer
from .apod_image import ApodImageDownloader, Image


def get_apod_image(year: int, month: int, day: int) -> Image:
    """Return the APOD image for the selected date."""
    explorer = ApodExplorer()
    explorer.make_http_request(year, month, day)
    img_url = explorer.check_for_images()
    downloader = ApodImageDownloader(img_url)

    return downloader.get_image()
