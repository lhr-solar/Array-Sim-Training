"""
AdaptiveStride.py

Author: Matthew Yu, Array Lead (2020).
Contact: matthewjkyu@gmail.com
Created: 11/19/20
Last Modified: 02/27/21
Description: Implementation of the Adaptive Stride perturbation function.

The AdaptiveStride class implements the perturbation function discussed in the
following paper:

    Adaptive Perturb and Observe Algorithm for Photovoltaic Maximum
    Power Point Tracking (Piegari et Rizzo.)

    Section 5, Algorithm Validation

    Building off of the stride function defined in OptimalStride,
    We can define any stride function as follow:
        stride = f(V_best - V) + dV_min
    
    Piegari et Rizzo proposes a piecewise function for f(V_best - V).

    f(V_best - V) = exp( (V_best - V) / 3 ) - 1     , V < V_best
                    0                               , V > V_best
    
    We see that in the event of the solar cell voltage being to the right of the 
    maximum power point, Piegari et Rizzo use dV_min to shift back towards the 
    maximum power point.

    dV_min is defined as a function of the estimation error, K, which is a user
    constant. Piegari et Rizzo also proposes that dV_min should be at least

    K^2 / (2 * (1 - K)) * V_best.

    The error estimation allows for correcting the parent local MPPT algorithm
    to converge at the maximum. However, if the predicted V_best is off mark, so
    will be the initial convergence.
"""
# Library Imports.
from math import exp

# Custom Imports.
from ArraySimulation.MPPT.MPPTComponents.Stride import Stride


class AdaptiveStride(Stride):
    """
    Derived class of Stride seeking to adaptively jump towards the VMPP at all
    times.
    """

    def __init__(self, minStride=0.01, VMPP=0.621, error=0.05):
        super(AdaptiveStride, self).__init__("Adaptive", minStride, VMPP, error)

    def getStride(self, arrVoltage, arrCurrent, irradiance, temperature):
        minStride = self.error * self.error * self.VMPP / (2 * (1 - self.error))
        stride = 0
        if arrVoltage < self.VMPP:
            stride = exp((self.VMPP - arrVoltage) / 3) - 1
        return stride + minStride
