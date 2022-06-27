import unittest

from apod.apod_web import ApodExplorer
from apod.exceptions import ApodDateError


class TestApodExplorer(unittest.TestCase):
    def test_get_url(self):
        explorer = ApodExplorer()
        url = explorer.generate_date_url(year=2022, month=1, day=9)
        real_url = "https://apod.nasa.gov/apod/ap220109.html"
        self.assertEqual(url, real_url)

    def test_make_http_request(self):
        explorer = ApodExplorer()
        code = explorer.make_http_request(year=2022, month=1, day=9)
        self.assertEqual(code, 200)

    def test_request_wrong_date(self):
        explorer = ApodExplorer()
        with self.assertRaises(ApodDateError):
            code = explorer.make_http_request(year=1900, month=1, day=9)

    def test_check_for_images(self):
        explorer = ApodExplorer()
        code = explorer.make_http_request(year=2022, month=1, day=9)
        img_url = (
            "https://apod.nasa.gov/apod/image/2201/JupiterOpal_HubbleMasztalerz_960.jpg"
        )
        self.assertEqual(img_url, explorer.check_for_images())
        code = explorer.make_http_request(year=2022, month=1, day=10)
        self.assertIsNone(explorer.check_for_images())
