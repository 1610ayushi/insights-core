"""
BlacklistedSpecs - File ``blacklisted_specs.txt``
=================================================
"""
from insights.core import JSONParser
from insights.core.plugins import parser
from insights.specs import Specs


@parser(Specs.blacklisted_specs)
class BlacklistedSpecs(JSONParser):
    """
    Parses the blacklisted_specs.txt file generated on archive creation.

    Typical output::
        "{"specs": ["insights.specs.default.DefaultSpecs.dmesg", "insights.specs.default.DefaultSpecs.fstab"]}"

    Attributes:
        specs (list): List of blacklisted specs.

    Examples:
        >>> type(specs)
        <class 'insights.parsers.blacklisted.BlacklistedSpecs'>
        >>> result = ['insights.specs.default.DefaultSpecs.dmesg', 'insights.specs.default.DefaultSpecs.fstab']
        >>> specs.specs == result
        True
    """
    @property
    def specs(self):
        return self.data['specs']