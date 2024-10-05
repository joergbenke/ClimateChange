"""
This module is the test suite for the ClimateLab project
"""

from src.climate_change import absorbed_shortwave_radiation

# import pytest


#
# Testregion

def test_absorbed_shortwave_radiation():
    """
    Test with all 0 parameters
    """

    assert absorbed_shortwave_radiation(0, 0) == 0
