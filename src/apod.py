from dataclasses import dataclass
from io import BytesIO
from time import localtime

import requests
from bs4 import BeautifulSoup
from PIL import Image

APOD_URL = "https://apod.nasa.gov/apod/"


@dataclass
class DateHandler:
    """Transform date to the specified apod requeriments"""

    year: int = localtime().tm_year
    month: int = localtime().tm_mon
    day: int = localtime().tm_mday

    def __post_init__(self) -> None:
        """Checks for correct year"""
        if self.year < 1995 or self.year > localtime().tm_year:
            raise ValueError(f"APODs  only exist from 1995 to {localtime().tm_year}")

    @property
    def apod_date(self) -> str:
        return f"{str(self.year)[-2:]}{self.month:02d}{self.day:02d}"


class APODRetrieveError(Exception):
    """Exception that handles APOD requests that goes wrong"""

    def __init__(self, response: requests.Response, msg: str) -> None:
        self.reponse = response
        self.msg = msg
        super().__init__(f"HTTPcode: {self.reponse.status_code}. {self.msg}")


class Retriever:
    """Asks apod web server for apod of a certain date"""

    def __init__(self, date: DateHandler) -> None:

        self.date = date
        self.response = Retriever.get_response(href=f"ap{self.date.apod_date}.html")
        self.html = Retriever.parse_html(self.response)

    @staticmethod
    def get_response(href: str) -> requests.Response:

        url = f"{APOD_URL}{href}"
        response = requests.get(url)
        if response.status_code != requests.codes.ok:
            raise APODRetrieveError(response, "The site {url} is not reacheble")
        return response

    @staticmethod
    def parse_html(response: requests.Response) -> BeautifulSoup:
        return BeautifulSoup(response.text, "html.parser")

    def get_image(self) -> Image.Image:
        img_tag = self.html.find("img")
        img_href = img_tag["src"]
        img_response = requests.get(f"{APOD_URL}{img_href}")
        img = Image.open(BytesIO(img_response.content))
        return img


def main():
    date = DateHandler(year=2022, month=6, day=24)
    retriever = Retriever(date)
    print(retriever.get_image())


if __name__ == "__main__":
    main()
