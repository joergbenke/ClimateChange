"""
This is a small project to get familiar with the very basic ideas
of climate change modelling and Github Actions
"""


def energy_balance(albedo=1, emissivity=1, swr=2):
    """
    Implementation of the stationary balance of incoming
    and outgoing radiation
    """
    return albedo * emissivity * swr

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


if __name__ == "__main__":
    test_energy_balance()
    test_energy_balance_zeroes()
    print(energy_balance(1, 1, 1))
