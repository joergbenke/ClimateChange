import math as m

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


def absorbed_shortwave_radiation(albedo=0.299):
    """
    Implementation of the stationary balance of incoming
    and outgoing radiation
    """
    Q = 341.3  # global mean insulation
    
    return (1 - albedo) * Q


def black_body_radiation(temperature):
    """
    Calculation of the black body radiation of the earth
    (earth is assumed to be an approximated black body radiator)
    """
    STEFAN_BOLTZMANN_CONSTANT = 5.67 * 10 ** (-8)
    TAU = 0.61  # transmissivity of the atmosphere 
    
    return STEFAN_BOLTZMANN_CONSTANT * TAU * temperature ** 4


def temperature_black_body_radiator(olr):
    """
    Calculate the temprature of a black body radiator with the help of 
    the outgoing longwave radiation (olr) 
    """
    STEFAN_BOLTZMANN_CONSTANT = 5.67 * 10 ** (-8)
    
    return (olr / STEFAN_BOLTZMANN_CONSTANT) ** (1/4)


if __name__ == "__main__":
    print(energy_balance(1, 1, 1))

    # Short wave radiation implementation
    print(absorbed_shortwave_radiation(0.299))
    
    print(black_body_radiation(288))
    print(black_body_radiation(292))
    # Output of the temperature of the black body radiator earth with
    # given outgoing longwave radiation
    print(temperature_black_body_radiator(238.5))
