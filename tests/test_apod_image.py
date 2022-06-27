import unittest

from PIL.Image import Image

from apod.apod_image import ApodImageDownloader


class TestApodImageDownloader(unittest.TestCase):
    def test_download_image(self):
        url = "https://apod.nasa.gov/apod/image/2201/JupiterOpal_HubbleMasztalerz_1880.jpg"
        downloader = ApodImageDownloader(url)
        image = downloader.get_image()
        self.assertIsInstance(image, Image)
