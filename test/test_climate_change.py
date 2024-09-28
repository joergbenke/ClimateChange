from climate_change import energy_balance
import pytest

#
# Testregion

def test_energy_balance():
    """
    Test with some normal parameters
    """
    assert energy_balance(1, 1, 2) == 2


def test_energy_balance_zeroes():
    """
    Test with all 0 parameters
    """
    assert energy_balance(0, 0, 0) == 0

