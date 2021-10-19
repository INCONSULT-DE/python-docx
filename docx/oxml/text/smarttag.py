
"""
Custom element classes related to smarttags (CT_SmartTagRun).
"""

from ..simpletypes import ST_String
from ..xmlchemy import BaseOxmlElement, ZeroOrMore, OptionalAttribute, RequiredAttribute


class CT_SmartTagRun(BaseOxmlElement):
    """
    ``<w:smartTag>`` element, containing the properties and text for a smart tag.
    """
    r = ZeroOrMore('w:r')
    element = RequiredAttribute('w:element', ST_String)

    def clear_content(self):
        """
        Remove all child elements
        """
        for child in self[:]:
            self.remove(child)





