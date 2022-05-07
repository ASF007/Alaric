from collections import namedtuple

from .advanced_query import AQ
from .document import Document

__all__ = ("AQ", "Document")
__version__ = "0.0.1"
VersionInfo = namedtuple("VersionInfo", "major minor micro releaselevel serial")
version_info = VersionInfo(major=0, minor=0, micro=1, releaselevel="final", serial=0)
