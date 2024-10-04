"""
This is a small project to get familiar with the very basic ideas
of climate change modelling and Github Actions

We implement a small 0 dimensional energy balance model
"""


def absorbed_shortwave_radiation(albedo=0.299, iswr=341.3):
    """
    Implementation of the stationary balance of incoming
    and outgoing radiation

    iswr = global mean insulation
    """

    return (1 - albedo) * iswr


def outgoing_longwave_radiation(tau, temperature):
    """
    Calculation of the outgoing radiation of the earth
    (earth is assumed to be an approximated black body radiator
    and the transmissivitiy of the atmosphere is also taken into
    account)
    """
    theta = 5.67 * 10 ** (-8)  # Stefan-Boltzmann-Konstante

    return theta * tau * temperature ** 4


def black_body_radiation(temperature):
    """
    Calculation of the black body radiation of the earth
    (earth is assumed to be an approximated black body radiator)
    """
    theta = 5.67 * 10 ** (-8)  # Stefan-Boltzmann-Konstante

    return theta * temperature ** 4


def temperature_black_body_radiator(olr):
    """
    Calculate the temprature of a black body radiator with the help of
    the outgoing longwave radiation (olr)
    """
    theta = 5.67 * 10 ** (-8)

    return (olr / theta) ** (1/4)


def temperature_equilibrium_earth(tau, albedo, iswr):
    """
    Calculate the equilibrium temprature of the earth with the help
    of the arguments albedo, transmissivity of the atmosphere and
    the incoming short wave radiation
    """
    theta = 5.67 * 10 ** (-8)

    return ((1 - albedo) * iswr / (tau * theta)) ** (1/4)


if __name__ == "__main__":
    # Short wave radiation implementation
    print("Absorbed shortwave energy")
    print(absorbed_shortwave_radiation(0.32, 341.3))
    print("Outgoing longwave radiation")
    print(outgoing_longwave_radiation(0.57, 291))

    print()
    print(black_body_radiation(288))
    print(black_body_radiation(292))
    # Output of the temperature of the black body radiator earth with
    # given outgoing longwave radiation
    print(temperature_black_body_radiator(238.5))

    #
    # Some tests with the equilibrium tmeperature
    print("Temperature (surface) at equilibrium")
    print("Arguments: tau=0.61, albedo=0.299, iswr=341.3")
    print(temperature_equilibrium_earth(0.61, 0.299, 341.3))
    print()
    print("Arguments: tau=0.57, albedo=0.299, iswr=341.3")
    print(temperature_equilibrium_earth(0.57, 0.299, 341.3))
    print()
    print("Arguments: tau=0.61, albedo=0.32, iswr=341.3")
    print(temperature_equilibrium_earth(0.61, 0.32, 341.3))
    print()
    print("Arguments: tau=0.57, albedo=0.32, iswr=341.3")
    print(temperature_equilibrium_earth(0.57, 0.32, 341.3))
    print()
    print("Arguments: tau=1.0, albedo=0.299, iswr=341.3")
    print(temperature_equilibrium_earth(1.0, 0.299, 341.3))
