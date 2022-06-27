import argparse
import os
import time
import datetime

import apod

lt = time.localtime()

parser = argparse.ArgumentParser(
    prog="ApodWallpaper",
    description="Look for an APOD image, download it and set it as wallpaper. Only works for gnome 3",
)
parser.add_argument(
    "--date",
    type=int,
    nargs=3,
    default=[lt.tm_year, lt.tm_mon, lt.tm_mday],
    help="Select the apod date: year | month | day. The default option is the curret day",
)
parser.add_argument(
    "--dirpath",
    type=str,
    default=f"{os.getenv('HOME')}/Pictures",
    help="Select the directory wher apod will be saved",
)
parser.add_argument(
    "--disable-description",
    action="store_false",
    help="The program will not download the apod description",
)
parser.add_argument(
    "--force", action="store_true", help="Ignore if there is a gnome instalation."
)

options = parser.parse_args()

# Checks for a gnome instalation
if "gnome" not in "".join([env.lower() for env in os.environ]) and not options.force:
    raise OSError("Cannot find a gnome instalation.")

date = datetime.datetime(*options.date)
explorer = apod.ApodExplorer()
url_image = None

# Look for an apod image in a loop, day by day in reverse until one is found.
while True:
    print(f"Looking for APOD in date: {date}")
    explorer.make_http_request(date.year, date.month, date.day)
    url_image = explorer.check_for_images()
    if url_image is not None:
        print(f"APOD image has been found.")
        break
    delta = datetime.timedelta(days=1)
    date = date - delta


# Formatting the path
path = str(options.dirpath)
if path.startswith("~"):
    path = f"{os.getenv('HOME')}/{path[2:]}"
elif not path.startswith("/"):
    path = os.path.abspath(path)
name = f"apod_{date.year}{date.month}{date.day}.jpeg"
fullpath = os.path.join(path, name)

print(f"Saving APOD in {fullpath}")

# Downloading and saving
downloader = apod.ApodImageDownloader(url_image)
downloader.save_image(path, name)

print("APOD saved succesfully.")

fullpath = os.path.abspath(os.path.join(path, name))
command = (
    f"gsettings set  org.gnome.desktop.background  picture-uri 'file://{fullpath}'"
)

print("Setting up new wallpaper.")

os.system(command)

print("Enjoy your APOD :)")
