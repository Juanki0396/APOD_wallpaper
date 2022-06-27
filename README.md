# APOD with python

![](.readme/apod_2022627.jpeg)

*Image by [Wang Jin](royalk86@gmail.com)*

![Tests](https://github.com/Juanki0396/APOD_wallpaper/actions/workflows/tests.yml/badge.svg)
![LICENSE](https://img.shields.io/github/license/juanki0396/APOD_wallpaper?)
![commit](https://img.shields.io/github/last-commit/juanki0396/APOD_wallpaper)

Do you love APOD images? This repo give you an easy interface to obtain this images from the source with python. Also, if you run an Ubuntu OS with Gnome 3, a python script can be used to automatically change your wallpaper to your favourite apod.

----

## Instalation

The package is already public in PyPi. You can easily install with pip:

    python3 -m pip install apod

---

## APOD package

The apod package is based in two objects: ApodExplorer and ApodImageDownloader. The ApodExplorer make requests for apod server and obtain the image url.

    import apod

    explorer = apod.ApodExplorer()
    http_status = explorer.make_http_request(year=2022, month=6, day=27)
    image_url = explorer.check_for_images()

The other object is responsible to download the image and save it:

    downloader = apod.ApodImageDownloader(image_url)
    # Obtain PIL image
    image = downloader.get_image()
    # Download and save
    downloader.save_image(path=<DIRPATH>, name=<FILENAME>)

---

## Wallpaper script

If you want to use the automatic apod wallpaper script you must [install the apod package](#apod-package) and clone the repo:

    git clone https://github.com/Juanki0396/APOD_wallpaper.git

The script is very easy to use. The ussual operation will be:

    python3 apod_wallpaper.py --date <YEAR> <MONTH> <DAY> --dirpath <DOWNLOAD DIR>