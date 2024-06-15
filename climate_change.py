"""
This is a small project to get familiar with the very basic ideas
of climate change modelling and Github Actions
"""


def energy_balance(albedo=1, emissivity=1, swr=1):
    """
    Implementation of the stationary balance of incoming
    and outgoing radiation
    """
    return albedo * emissivity * swr


if __name__ == "__main__":
    print(energy_balance(1, 1, 1))
