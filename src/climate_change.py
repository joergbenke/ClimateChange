"""
This is a small project to get familiar with the very basic ideas
of climate change modelling and Github Actions

We implement a small 0 dimensional energy balance model
"""


def absorbed_shortwave_radiation(albedo=0.299):
    """
    Implementation of the stationary balance of incoming
    and outgoing radiation
    """
    Q = 341.3  # global mean insulation

    return (1 - albedo) * Q


def outgoing_longwave_radiation(temperature):
    """
    Calculation of the outgoing radiation of the earth
    (earth is assumed to be an approximated black body radiator
    and the transmissivitiy of the atmosphere is also taken into
    account)
    """
    STEFAN_BOLTZMANN_CONSTANT = 5.67 * 10 ** (-8)
    TAU = 0.61  # transmissivity of the atmosphere

    return STEFAN_BOLTZMANN_CONSTANT * TAU * temperature ** 4


def black_body_radiation(temperature):
    """
    Calculation of the black body radiation of the earth
    (earth is assumed to be an approximated black body radiator)
    """
    STEFAN_BOLTZMANN_CONSTANT = 5.67 * 10 ** (-8)

    return STEFAN_BOLTZMANN_CONSTANT * temperature ** 4


def temperature_black_body_radiator(olr):
    """
    Calculate the temprature of a black body radiator with the help of
    the outgoing longwave radiation (olr)
    """
    STEFAN_BOLTZMANN_CONSTANT = 5.67 * 10 ** (-8)

    return (olr / STEFAN_BOLTZMANN_CONSTANT) ** (1/4)


def temperature_equilibrium_earth(tau, albedo, Q):
    """
    Calculate the equilibrium temprature of the earth with the help
    of the arguments albedo, transmissivity of the atmosphere and
    the incoming short wave radiation
    """
    STEFAN_BOLTZMANN_CONSTANT = 5.67 * 10 ** (-8)

    return ((1 - albedo) * Q / (tau * STEFAN_BOLTZMANN_CONSTANT)) ** (1/4)


if __name__ == "__main__":
    # Short wave radiation implementation
    print(absorbed_shortwave_radiation(0.299))

    print(black_body_radiation(288))
    print(black_body_radiation(292))
    # Output of the temperature of the black body radiator earth with
    # given outgoing longwave radiation
    print(temperature_black_body_radiator(238.5))

    #
    # Some tests with the equilibrium tmeperature
