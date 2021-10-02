"""
PandO.py

Author: Matthew Yu, Array Lead (2020).
Contact: matthewjkyu@gmail.com
Created: 11/18/20
Last Modified: 02/27/21

Description: Implementation of the PandO hill climbing algorithm.
"""
# Library Imports.


# Custom Imports.
from ArraySimulation.MPPT.LocalMPPTAlgorithms.LocalMPPTAlgorithm import (
    LocalMPPTAlgorithm,
)


class BisectionPandO(LocalMPPTAlgorithm):
    """
    The PandO (Perturb and Observe) class is a derived class of
    LocalMPPTAlgorithm, utilizing the change of power and change of voltage over
    time to determine the direction of movement and stride of the next reference
    voltage. It belongs to the classification of hill climbing algorithms.
    """

    def __init__(self, numCells=1, strideType="Fixed"):
        super(BisectionPandO, self).__init__(numCells, "BisectionPandO", strideType)
        self.vOld = 0
        self.pOld = 0 
        self.stride = .01
        # self._minVoltage = .05
        # self.kick = True

    def getReferenceVoltage(self, arrVoltage, arrCurrent, irradiance, temperature):
        power = arrVoltage * arrCurrent     
        Pdiff = power - (self.pOld)
        Vdiff = arrVoltage - self.vOld
        vRef = arrVoltage
        adaptstride = self.stride
        # Decide the value of the stride
        if (Vdiff != 0):
            if (Pdiff/Vdiff > 0):
                adaptstride = Pdiff/Vdiff *.0055
                print(adaptstride)
            if (Pdiff/Vdiff < 0):
                adaptstride = (((arrVoltage + self.vOld)/2) - self.vOld)
                # print(adaptstride)
            self.stride = max(adaptstride, self.stride)
        # Decide which direction to step
        if (arrVoltage == 0):
            vRef = vRef + self.stride
        elif Vdiff > 0:
            if Pdiff > 0:
                vRef = vRef + self.stride
            elif Pdiff < 0:
                vRef = vRef - self.stride
        elif Vdiff < 0:
            if Pdiff < 0:
                vRef = vRef + self.stride
            elif Pdiff > 0:
                vRef = vRef - self.stride
        self.vOld = arrVoltage
        self.pOld = arrVoltage * arrCurrent
        return vRef
  

