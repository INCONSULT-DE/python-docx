
"""
Custom element classes related to hyperlinks (CT_Hyperlink).
"""

from ..ns import qn
from ..simpletypes import XsdString
from ..xmlchemy import BaseOxmlElement, ZeroOrMore, ZeroOrOne


class CT_Hyperlink(BaseOxmlElement):
    """
    ``<w:hyperlink>`` element, containing the properties and text for a hyperlink.
    """
    r = ZeroOrMore('w:r')
    rId = ZeroOrOne('r:id')

    def clear_content(self):
        """
        Remove all child elements
        """
        for child in self[:]:
            self.remove(child)





