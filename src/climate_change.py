"""
This is a small project to get familiar with the very basic ideas
of climate change modelling and Github Actions

We implement a small 0 dimensional energy balance model
"""

import numpy as np
import energybalance_model as ebm


if __name__ == "__main__":
    # Short wave radiation implementation
    print("Absorbed shortwave energy")
    print(ebm.absorbed_shortwave_radiation(0.32, 341.3))
    print("Outgoing longwave radiation")
    print(ebm.outgoing_longwave_radiation(0.57, 291))

    print()
    print(ebm.black_body_radiation(288))
    print(ebm.black_body_radiation(292))
    # Output of the temperature of the black body radiator earth with
    # given outgoing longwave radiation
    print(ebm.temperature_black_body_radiator(238.5))

    #
    # Some tests with the equilibrium tmeperature
    print("Temperature (surface) at equilibrium")
    print("Arguments: tau=0.61, albedo=0.299, iswr=341.3")
    print(ebm.temperature_equilibrium_earth(0.61, 0.299, 341.3))
    print()
    print("Arguments: tau=0.57, albedo=0.299, iswr=341.3")
    print(ebm.temperature_equilibrium_earth(0.57, 0.299, 341.3))
    print()
    print("Arguments: tau=0.61, albedo=0.32, iswr=341.3")
    print(ebm.temperature_equilibrium_earth(0.61, 0.32, 341.3))
    print()
    print("Arguments: tau=0.57, albedo=0.32, iswr=341.3")
    print(ebm.temperature_equilibrium_earth(0.57, 0.32, 341.3))
    print()
    print("Arguments: tau=1.0, albedo=0.299, iswr=341.3")
    print(ebm.temperature_equilibrium_earth(1.0, 0.299, 341.3))
    print()
    print("temporal variable solution of the energy balance model")
    c_w = 4E3  # Specific heat of water in J/kg/K
    rho_w = 1E3  # Density of water in kg/m3
    height = 100.  # Depth of water in m
    hc = c_w * rho_w * height   # Heat capacity of the model
    print('The effective heat capacity is {:.1e} J/m2/K'.format(hc))

    albedo = 0.299
    iswr = 341.3
    tau = 0.57
    theta = 5.67 * 10 ** (-8)
    initial_temperature = 288.0

    t_0 = 0.0
    t_end = 60. * 60. * 24. * 365. * 30  # one year expressed in seconds
    delta_t = 60. * 60. * 24. * 365.
    n_time_steps = int((t_end - t_0) / delta_t)
    time_steps = np.arange(n_time_steps + 1, dtype='float')

    print(ebm.temporal_evolution_temperature(initial_temperature, delta_t, n_time_steps, \
                                             hc, albedo, iswr, tau, theta))
