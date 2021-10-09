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


class PandO(LocalMPPTAlgorithm):
    """
    The PandO (Perturb and Observe) class is a derived class of
    LocalMPPTAlgorithm, utilizing the change of power and change of voltage over
    time to determine the direction of movement and stride of the next reference
    voltage. It belongs to the classification of hill climbing algorithms.
    """

    def __init__(self, numCells=1, strideType="Fixed"):
        super(PandO, self).__init__(numCells, "PandO", strideType)
        # self._minVoltage = .05
        # self.kick = True
        self.prevVolt = 0
        self.prevCurrent = 0

    def getReferenceVoltage(self, arrVoltage, arrCurrent, irradiance, temperature):
        
        currVolt = arrVoltage
        currCurrent = arrCurrent

        if(currVolt==0):

            currVolt+=.01
            
            return currVolt
        
        voltDiff = currVolt-self.prevVolt
        PDiff = (currVolt*currCurrent)-(self.prevVolt*self.prevCurrent)

        self.prevVolt = currVolt
        self.prevCurrent = currCurrent
        
        if((voltDiff>0 and PDiff>0)or(voltDiff<0 and PDiff<0)):
            currVolt+=.01
        else:
            currVolt-=.01

        return currVolt

