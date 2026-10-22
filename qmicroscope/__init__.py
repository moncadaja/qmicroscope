try:
    from ._version import __version__
except ImportError:  # source checkout that was never built/installed
    __version__ = "0.0.0+unknown"

from .microscope import Microscope
from .plugins import *
