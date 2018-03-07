"""rio_tiler.profiles"""

from rio_tiler.errors import InvalidFormat


class TileProfiles():
    """https://github.com/mapnik/mapnik/wiki/Image-IO#default-output-details
    """
    def __init__(self):
        pass

    def get(name):
        if name == 'jpeg':
            """https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#jpeg"""
            return {'quality': 95}

        elif name == 'png':
            """https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#png"""
            return {'compress_level': 0}

        elif name == 'webp':
            """https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#webp"""
            return {'quality': 80}
        else:
            raise InvalidFormat('{} format is not supported'.format(name))
