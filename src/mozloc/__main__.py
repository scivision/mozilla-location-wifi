#!/usr/bin/env python
"""
https://mozilla.github.io/ichnaea/api/geolocate.html
https://ichnaea.readthedocs.io/en/latest/api/geolocate.html

you should get your own Mozilla Location Services API key

Don't abuse the API or you'll get banned (excessive polling rate)
"""
from .base import log_wifi_loc
from argparse import ArgumentParser


def mozilla_location():
    """
    output: lat lon [deg] accuracy [m]
    """
    p = ArgumentParser()
    p.add_argument("logfile", help="logfile to append location to", nargs="?")
    p.add_argument(
        "-T", "--cadence", help="how often to ping [sec]. Some laptops cannot go faster than 30 sec.", default=60, type=float
    )
    p.add_argument(
        "-url",
        help="Mozilla location services URL--don't use this default test key",
        default="https://location.services.mozilla.com/v1/geolocate?key=test",
    )
    p = p.parse_args()

    log_wifi_loc(p.cadence, p.url, p.logfile)


def csv2kml():
    """convert logged positions to KML"""
    from .utils import csv2kml

    p = ArgumentParser()
    p.add_argument("logfn", help="csv logfile to read")
    p.add_argument("kmlfn", help="kml filename to write")
    p = p.parse_args()

    csv2kml(p.logfn, p.kmlfn)