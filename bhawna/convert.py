# -*- coding: utf-8 -*-
"""
- out_full_filename - prepare output file for conversion
"""

import os

import logging

module_logger = logging.getLogger(__name__)


def out_full_filename(file_in, destination, extension):
    """
    Input:
        file_in - original file for processing
        destination - output directory
        extension - extension of result file, for change format (jpg->png)
    Output:
        file_out - fullname file for processing in destination
    """
    result = "OK"  # initial value
    if file_in is not None:
        if os.path.isfile(file_in):
            # making output diretory if not exist
            out_dir = os.path.join(os.path.dirname(file_in), destination)
            if os.path.isdir(out_dir) is False:
                try:
                    os.mkdir(out_dir)
                except FileExistsError:
                    module_logger.error("pre_imagick: FileExistsError %s", out_dir)
                except FileNotFoundError:
                    try:
                        os.mkdir(os.path.dirname(out_dir))
                    except FileNotFoundError:
                        module_logger.error(
                            "pre_imagick: Cannot make directory for output pictures %s",
                            os.path.dirname(out_dir),
                        )
                        result = None
                    except:
                        module_logger.error(
                            "pre_imagick: other problem to create %s",
                            os.path.dirname(out_dir),
                        )
                        result = None
                    if result == "OK":
                        try:
                            os.mkdir(out_dir)
                        except FileExistsError:
                            module_logger.error("pre_imagick: FileExistsError %s", out_dir)
                        except FileNotFoundError:
                            module_logger.error(
                                "pre_imagick: FileExistsError %s",
                                os.path.dirname(out_dir),
                            )
                            result = None
                        except:
                            module_logger.error(
                                "pre_imagick: other problem to create %s", out_dir
                            )
                            result = None
                except:
                    module_logger.error("pre_imagick: other problem to create %s", out_dir)
                    result = None

        else:
            result = None
    else:
        result = None

    if result == "OK":
        # preparing output filename
        file_in_without_ext = os.path.splitext(file_in)
        file_out = os.path.join(
            out_dir, os.path.basename(file_in_without_ext[0] + extension)
        )
    else:
        file_out = None
    return file_out


# EOF
