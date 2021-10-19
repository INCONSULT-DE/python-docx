
"""
Smart tag-related proxy types.
"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from .run import Run
from ..shared import Parented
from ..runcntnr import RunItemContainer

class SmartTag(RunItemContainer):
    """
    Proxy object wrapping ``<w:smartTag>`` element.
    """
    def __init__(self, s, parent):
        super(SmartTag, self).__init__(s, parent)
        self._s = self._element = s

    def clear(self):
        """
        Return this same paragraph after removing all its content.
        Paragraph-level formatting, such as style, is preserved.
        """
        self._h.clear_content()
        return self

    @property
    def runs(self):
        return super(SmartTag, self).runs

    @property
    def element(self):
        return self._s.element