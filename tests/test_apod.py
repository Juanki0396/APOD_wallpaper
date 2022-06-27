import unittest

from PIL.Image import Image

from apod import get_apod_image
from apod.exceptions import ApodDateError, ApodRetrieveError


class TestApod(unittest.TestCase):
    def test_get_apod_image(self):
        image = get_apod_image(year=2022, month=1, day=9)
        self.assertIsInstance(image, Image)

    def test_wrong_date(self):
        with self.assertRaises(ApodDateError):
            image = get_apod_image(year=1900, month=1, day=9)

    def test_try_to_get_video(self):
        with self.assertRaises(ApodRetrieveError):
            image = get_apod_image(year=2022, month=1, day=25)
