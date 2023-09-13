from functools import cache
from math import exp

@cache
def weight(delta_energy:float =0.0, temperature: float=1.0):
    return exp(-delta_energy/temperature)


def boltzmann_weight(delta_energy:float =0.0, temperature: float=1.0):
    return exp(-delta_energy/temperature)



boltzmann_weight()
