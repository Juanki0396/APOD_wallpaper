from io import BytesIO
from functools import cached_property
from time import localtime
from typing import Protocol, Union


import requests
from bs4 import BeautifulSoup
from PIL import Image

from .exceptions import ApodDateError, ApodRetrieveError


class ApodWebProtocol(Protocol):
    """Defines the dynamics to interact with the web server"""

    def make_http_request(year: int, month: int, day: int) -> int:
        ...

    def check_for_images() -> Union[None, str]:
        ...

    def check_for_video() -> Union[None, str]:
        ...

    def get_description() -> str:
        ...


class ApodExplorer:
    """Asks apod web server for apod of a certain date"""

    APOD_URL = "https://apod.nasa.gov/apod/"

    def __init__(self) -> None:

        self.response: requests.Response = None

    @cached_property
    def html(self) -> BeautifulSoup:
        return BeautifulSoup(self.response.text, "html.parser")

    def generate_date_url(self, year: int, month: int, day: int) -> str:
        """Generate the apod url for the requested date"""
        f"{self.APOD_URL}{str(year)[-2:]}{month:02d}{day:02d}"

    def make_http_request(
        self,
        year: int = localtime().tm_year,
        month: int = localtime().tm_mon,
        day: int = localtime().tm_mday,
    ) -> int:
        """Make an http request to apod for the html of the selected date"""
        if year <= 1995 and month < 6 and day < 21:
            raise ApodDateError(year, month, day)

        # TODO raise error for a future date

        url = self.generate_date_url(year, month, day)
        self.response = requests.get(url)

        if self.response.status_code != requests.codes.ok:
            raise ApodRetrieveError(self.response, "The site {url} is not reacheble")

        return self.response.status_code

    def check_for_images(self) -> Union[str, None]:
        img_tag = self.html.find("img")
        img_href = img_tag["src"]

        if len(img_href) == 0:
            return None

        img_url = f"{self.APOD_URL}{img_href}"
        return img_url


def main():
    pass


if __name__ == "__main__":
    main()
