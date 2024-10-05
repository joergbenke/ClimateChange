"""
This is a small project to get familiar with the very basic ideas
of climate change modelling and Github Actions

We implement a small 0 dimensional energy balance model
"""

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
