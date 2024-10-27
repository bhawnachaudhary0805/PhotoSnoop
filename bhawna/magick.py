# -*- coding: utf-8 -*-
# pylint: disable=bare-except

"""
module to run ImageMagick:
- magick - picture conversion
"""

import logging
import os

import common

module_logger = logging.getLogger(__name__)


def magick(cmd, file_in, file_out, command, operating_system):
    """
    run imagemagick command.
    cmd - command for imagemagick
    file_in - fullname picture for processing
    file_out - fullname output picture
    command:
      convert, mogrify, composite, import - ImageMagick
    """
    result = None
    if cmd != "":
        if file_in is not None:
            file_in = common.spacja(file_in, operating_system)
            file_out = common.spacja(file_out, operating_system)
            if operating_system == 'Windows':
                prefix_cmd = "magick.exe "
            else:
                prefix_cmd = ""
            command_exec = (
                prefix_cmd + command + " " + file_in + " " + cmd + " " + file_out
            )
            module_logger.info("Execute: %s", command_exec)
            try:
                os.system(command_exec)
            except:
                module_logger.error("Errot in imagick: %s", command_exec)
                result = None
            else:
                result = "OK"
        else:
            module_logger.warning("imagick: No file for imagick")
            result = None
    else:
        result = None
    return result


# EOF
