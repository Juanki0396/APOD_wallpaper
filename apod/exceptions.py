from time import localtime

import requests


class ApodRetrieveError(Exception):
    """Exception that handles APOD requests that goes wrong"""

    def __init__(self, response: requests.Response, msg: str) -> None:
        self.reponse = response
        self.msg = msg
        super().__init__(f"HTTPcode: {self.reponse.status_code}. {self.msg}")


class ApodDateError(Exception):
    """Exception for handling dates before APOD"""

    def __init__(self, year: int, month: int, day: int) -> None:
        self.year = year
        self.month = month
        self.day = day
        first_apod = "First APOD: 21/6/1995"
        last_apod = f"Last APOD: {localtime().tm_mday}/{localtime().tm_mon}/{localtime().tm_year}"
        given_date = "Given Date: {day}/{month}/{year}"
        super().__init__(f"{first_apod} ---- {last_apod} ---- {given_date}")


class ApodImageError(Exception):
    """Exception for dates with none images found."""

    def __init__(self) -> None:
        super().__init__("None images were found fot he selected date.")
