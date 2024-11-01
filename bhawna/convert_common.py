# -*- coding: utf-8 -*-
# pylint: disable=bare-except

"""
Info
- fonts_list - fonts list
- display_image - display image
- get_image_size - identify picture: width and height
- preview - preview image
- make_clone
- save_close_clone
- rotate
- mirror
- resize
- border
- nornalize
- bw
- contrast
- crop
- text
- compose
"""

import logging
import time
import PIL

try:
    from wand.image import Image
    from wand.display import display

    WAND_TEXT = "Wand found"
except:
    WAND_TEXT = "ImageMagick or Wand-py not found"

import convert_pillow
import convert_wand


module_logger = logging.getLogger(__name__)
module_logger.info(WAND_TEXT)


def fonts_list(set_pillow):
    """list of available fonts"""
    start_time = time.time()
    if set_pillow:
        result = convert_pillow.fonts_list()
    else:
        result = convert_wand.fonts_list()
    module_logger.info("Get fonts list: %ss", str(time.time() - start_time))
    return result


def display_image(file_to_display, set_pillow):
    """display image"""
    # file_in = common.spacja(file_to_display)
    module_logger.info(" Display file: %s", file_to_display)
    try:
        start_time = time.time()
        if set_pillow:
            with PIL.Image.open(file_to_display) as image:
                image.show()
        else:
            with Image(filename=file_to_display) as image:
                display(image)
            module_logger.info("Display_image: %ss", str(time.time() - start_time))
    except:
        module_logger.error(" Error display file: %s", file_to_display)
        result = None

    result = "OK"

    return result


def get_image_size(file_in, set_pillow):
    """
    identify width and height of picture
    input: file name
    output: size (width, height)
    """
    start_time = time.time()
    if set_pillow:
        size = convert_pillow.get_image_size(file_in)
    else:
        size = convert_wand.get_image_size(file_in)
    module_logger.info("get_image_size: %ss", str(time.time() - start_time))
    return size


def preview(file_logo, size, set_pillow, operating_system, coord=""):
    """preview"""
    start_time = time.time()
    if set_pillow:
        result = convert_pillow.preview(file_logo, size, operating_system, coord)
    else:
        result = convert_wand.preview(file_logo, size, operating_system, coord)
    module_logger.info("preview: %s s", str(time.time() - start_time))
    return result


def make_clone(file_to_clone, set_pillow, color=None):
    """open picture and make clone for processing"""
    start_time = time.time()
    if set_pillow:
        result = convert_pillow.make_clone(file_to_clone, color)
    else:
        result = convert_wand.make_clone(file_to_clone, color)
    module_logger.info("Make clone: %ss", str(time.time() - start_time))
    return result


def save_close_clone(clone, file_out, exif_on, set_pillow):
    """save_close_clone"""
    start_time = time.time()
    if set_pillow:
        convert_pillow.save_close_clone(clone, file_out, exif_on)
    else:
        convert_wand.save_close_clone(clone, file_out, exif_on)
    module_logger.info("Save clone: %ss", str(time.time() - start_time))


def rotate(clone, angle, color, angle_own, set_pillow):
    """rotate"""
    start_time = time.time()
    if set_pillow:
        result = convert_pillow.rotate(clone, angle, color, angle_own)
    else:
        convert_wand.rotate(clone, angle, color, angle_own)
        result = clone
    module_logger.info("Rotate: %ss", str(time.time() - start_time))
    return result


def mirror(clone, flip, flop, set_pillow):
    """mirror: flip and flop"""
    start_time = time.time()
    if set_pillow:
        result = convert_pillow.mirror(clone, flip, flop)
    else:
        convert_wand.mirror(clone, flip, flop)
        result = clone
    module_logger.info("Mirror: %ss", str(time.time() - start_time))
    return result


def resize(clone, command, set_pillow):
    """resize picture"""
    start_time = time.time()
    if set_pillow:
        result = convert_pillow.resize(clone, command)
    else:
        convert_wand.resize(clone, command)
        result = clone
    module_logger.info("Resize: %ss", str(time.time() - start_time))
    return result


def border(clone, color, x, y, set_pillow):
    """mirror: flip and flop"""
    start_time = time.time()
    if set_pillow:
        result = convert_pillow.border(clone, color, x, y)
    else:
        convert_wand.border(clone, color, x, y)
        result = clone
    module_logger.info("Resize: %ss", str(time.time() - start_time))
    return result


def normalize(clone, normalize_variant, channel, set_pillow):
    """normalize levels of colors"""
    start_time = time.time()
    if set_pillow:
        result = convert_pillow.normalize(clone, normalize_variant, channel)
    else:
        convert_wand.normalize(clone, normalize_variant, channel)
        result = clone
    module_logger.info("Normalize %ss", str(time.time() - start_time))
    return result


def bw(clone, bw_variant, sepia, set_pillow):
    """black and white or sepia"""
    start_time = time.time()
    if set_pillow:
        result = convert_pillow.bw(clone, bw_variant, sepia)
    else:
        convert_wand.bw(clone, bw_variant, sepia)
        result = clone
    module_logger.info("Black-white/sepia %ss", str(time.time() - start_time))
    return result


def contrast(clone, contrast_variant, selection, black, white, set_pillow):
    """black and white or sepia"""
    start_time = time.time()
    if black == "" or black is None:
        black = 0
    if white == "" or white is None:
        white = 0
    if set_pillow:
        result = convert_pillow.contrast(
            clone, contrast_variant, selection, black, white
        )
    else:
        convert_wand.contrast(clone, contrast_variant, selection, black, white)
        result = clone
    module_logger.info("Contrast %ss", str(time.time() - start_time))
    return result


def crop(file_in, clone, crop_variant, gravity, entries, set_pillow):
    """black and white or sepia"""
    start_time = time.time()
    if set_pillow:
        result = convert_pillow.crop(file_in, clone, crop_variant, gravity, entries)
    else:
        convert_wand.crop(file_in, clone, crop_variant, gravity, entries)
        result = clone
    module_logger.info("Crop %ss", str(time.time() - start_time))
    return result


def text(convert_data, set_pillow):
    """black and white or sepia"""
    start_time = time.time()
    if set_pillow:
        result = convert_pillow.text(convert_data)
    else:
        result = convert_wand.text(convert_data)
    module_logger.info("Text %ss", str(time.time() - start_time))
    return result


def compose(clone, compose_file, right, autoresize, color, gravity, set_pillow):
    """join two pictures"""
    start_time = time.time()
    if set_pillow:
        result = convert_pillow.compose(
            clone, compose_file, right, autoresize, color, gravity
        )
    else:
        result = convert_wand.compose(
            clone, compose_file, right, autoresize, color, gravity
        )
    module_logger.info("Compose %ss", str(time.time() - start_time))
    return result
