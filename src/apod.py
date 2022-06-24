from dataclasses import dataclass
from time import localtime

import requests
from bs4 import BeautifulSoup


@dataclass
class DateHandler:
    """Transform date to the specified apod requeriments"""

    year: int = localtime().tm_year
    month: int = localtime().tm_mon
    day: int = localtime().tm_mday

    @property
    def apod_date(self) -> str:
        return f"{self.year - 2000}{self.month:02d}{self.day:02d}"


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
        self.url = f"https://apod.nasa.gov/apod/ap{date.apod_date}.html"

    def get_response(self) -> requests.Response:

        response = requests.get(self.url)

        if response.status_code != requests.codes.ok:
            raise APODRetrieveError(response, "The selected APOD is not reachable.")

        return response


class HTMLParser:
    pass


def main():
    date = DateHandler()
    print(date.apod_date)


if __name__ == "__main__":
    main()
