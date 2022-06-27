import os
import unittest

from PIL.Image import Image

from apod.apod_image import ApodImageDownloader
from apod.exceptions import ApodRetrieveError


class TestApodImageDownloader(unittest.TestCase):
    def test_download_image(self):
        """Check if ApodImageDownloader can obtain a known apod."""
        url = "https://apod.nasa.gov/apod/image/2201/JupiterOpal_HubbleMasztalerz_1880.jpg"
        downloader = ApodImageDownloader(url)
        image = downloader.get_image()
        self.assertIsInstance(image, Image)

    def test_download_from_wrong_url(self):
        """Check if ApodImageDownloader raise an error when an incorrect url is given."""
        url = "https://apod.nasa.gov/apod/image/2201/SDSADASDas.jpg"
        downloader = ApodImageDownloader(url)
        with self.assertRaises(ApodRetrieveError):
            image = downloader.get_image()

    def test_save_image(self):
        """Checks if an apod can be saved on a existing directory"""
        url = "https://apod.nasa.gov/apod/image/2201/JupiterOpal_HubbleMasztalerz_1880.jpg"
        path = "saved_images"
        name = "apod.jpeg"
        fullpath = os.path.join(path, name)
        if os.path.exists(fullpath):
            os.remove(fullpath)
        downloader = ApodImageDownloader(url)
        downloader.save_image(path, name)
        self.assertTrue(os.path.exists(fullpath))

    def test_save_directory_not_exists(self):
        """Checks if ApodImageDownloader raise an error while saving an apod on a non existing directory"""
        url = "https://apod.nasa.gov/apod/image/2201/JupiterOpal_HubbleMasztalerz_1880.jpg"
        path = "asdsafds"
        name = "apod.jpeg"
        downloader = ApodImageDownloader(url)
        with self.assertRaises(FileNotFoundError):
            downloader.save_image(path, name)
