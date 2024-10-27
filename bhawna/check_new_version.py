# -*- coding: utf-8 -*-

"""
From https://stackoverflow.com/questions/28774852/pypi-api-how-to-get-stable-package-version
"""

import json
import logging
import requests
import time

try:
    from packaging.version import parse
except ImportError:
    from pip._vendor.packaging.version import parse

module_logger = logging.getLogger(__name__)

URL_PATTERN = "https://pypi.org/pypi/{package}/json"


def get_version(url_pattern=URL_PATTERN):
    """Return version of package on pypi.python.org using json."""

    package = "bhawna"
    version = parse("0")
    try:
        req = requests.get(url_pattern.format(package=package), timeout=2.50)
        request_success = 1
    except:
        request_success = 0

    if request_success and req.status_code == requests.codes.ok:
        j = json.loads(req.text.encode(req.encoding))
        releases = j.get("releases", [])
        for release in releases:
            ver = parse(release)
            if not ver.is_prerelease:
                version = max(version, ver)
    return (request_success, str(version))


def check_version(current_version):
    """
    Check version of bhawna in PyPi
    return 1 - get new
    return 0 - there are no new
    """
    start_time = time.time()
    result = 0
    result_success, result_version = get_version()
    if result_success and result_version > current_version:
        result = 1
    module_logger.info("check_version: %ss", str(time.time() - start_time))
    return (result, result_version)
