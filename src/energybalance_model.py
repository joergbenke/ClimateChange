"""
This functions are the implementations of the zero dimensional
energy model
"""

import numpy as np


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


def temporal_evolution_temperature(initial_temperature, dt, n_time_steps, \
                                   hc, albedo, iswr, tau, theta):
    """
    Solution of the time dependent energy balance model 
    C * dT/dt = (1 - albedo) * Q - tau * theta * T ** 4
    """
    solution = np.arange(n_time_steps + 1, dtype='float')
    solution[0] = float(initial_temperature)
    for ts in range(0, n_time_steps):
        solution[ts+1] = solution[ts] + (dt / float(hc)) \
        * ((1 - albedo) * iswr - theta * tau * solution[ts] ** 4)

    return solution
