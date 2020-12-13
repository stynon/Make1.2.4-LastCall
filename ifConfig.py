#!/usr/bin/env python
"""
IP weergave (LAN en/of WAN, eth0 en of wlan0)
"""

# Import
import os

__author__ = "Stijn Janssen"
__email__ = "stijn.janssen@student.kdg.be"
__status__ = "Development"


def ip():
    os.system("ifconfig")

