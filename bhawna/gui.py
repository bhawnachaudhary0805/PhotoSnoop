# -*- coding: utf-8 -*-
"""

function for GUI:
- copy_to_clipboard - copy result into clipboard (only Windows)
- only_numbers - validate only natural values
- only_integer - validate integer values
"""

from io import BytesIO
import logging
import platform
import re
from PIL import Image

import common

if platform.system() == "Windows":
    import win32clipboard
elif platform.system() == "Darwin":
    import subprocess


module_logger = logging.getLogger(__name__)


def copy_to_clipboard(file_in, operating_system):
    """
    Copy results into clipboard for Windows
    https://stackoverflow.com/questions/34322132/copy-image-to-clipboard
    Copy results into clipboard for Macos
    https://stackoverflow.com/questions/54008175/copy-an-image-to-macos-clipboard-using-python?rq=4
    debug needed!
    """
    if operating_system == "Windows":
        # Create an in-memory file-like object
        image_buffer = BytesIO()
        image = Image.open(common.spacja(file_in, operating_system))
        image.convert("RGB").save(image_buffer, "BMP")
        data = image_buffer.getvalue()[14:]

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
        image_buffer.close()
    elif operating_system == "MACOS":
        try:
            subprocess.run(
                [
                    "osascript",
                    "-e",
                    'set the clipboard to (read (POSIX file "'
                    + file_in
                    + '") as JPEG picture)',
                ]
            )
            module_logger.debug(
                "Successful copied result into clipboard under MacOS: %s", file_in
            )
        except:
            module_logger.debug(
                "Failed copied result into clipboard under MacOS: %s", file_in
            )


def only_numbers(char):
    """Validation entry widgets: only digits"""
    return char.isdigit()


def only_integer(char):
    """Validation entry widgets: only digits"""
    if re.match("^[-]{0,1}[0-9]{,6}$", str(char)):
        result = True
    else:
        result = False
    return result


# EOF
