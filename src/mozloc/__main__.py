"""
https://mozilla.github.io/ichnaea/api/geolocate.html
https://ichnaea.readthedocs.io/en/latest/api/geolocate.html

you should get your own Mozilla Location Services API key

Don't abuse the API or you'll get banned (excessive polling rate)
"""

import argparse

from .base import log_wifi_loc, process_file


p = argparse.ArgumentParser()
p.add_argument("logfile", help="logfile to append location to", nargs="?")
p.add_argument(
    "-T", "--cadence", help="how often to update [sec]. Some laptops cannot go faster than 30 sec.", default=60, type=float
)
p.add_argument(
    "-url",
    help="Mozilla location services URL--don't use this default test key",
    default="https://location.services.mozilla.com/v1/geolocate?key=test",
)
p.add_argument("-i", "--infile", help="use raw text saved from command line")
p = p.parse_args()

if p.infile:
    process_file(p.infile, mozilla_url=p.url)
else:
    log_wifi_loc(cadence_sec=p.cadence, mozilla_url=p.url, logfile=p.logfile)
