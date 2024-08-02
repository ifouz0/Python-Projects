"""
Module Name: pylib.utilities.sysutils
Module Description: SO Module Info
"""

import os
import platform
import sys

def python_info() -> tuple[str,str]:
    """Python DocString"""
    return platform.python_implementation(), platform.python_version()


def machine_info() -> tuple[str,str,str,str,str]:
    """Python DocString"""
    return (platform.machine(), platform.system(), platform.platform(), platform.version(), platform.processor())