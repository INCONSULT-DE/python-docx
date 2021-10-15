
"""
Custom element classes related to hyperlinks (CT_Hyperlink).
"""

from ..simpletypes import ST_RelationshipId
from ..xmlchemy import BaseOxmlElement, ZeroOrMore, OptionalAttribute


class CT_Hyperlink(BaseOxmlElement):
    """
    ``<w:hyperlink>`` element, containing the properties and text for a hyperlink.
    """
    r = ZeroOrMore('w:r')
    rId = OptionalAttribute('r:id', ST_RelationshipId)

    def clear_content(self):
        """
        Remove all child elements
        """
        for child in self[:]:
            self.remove(child)





