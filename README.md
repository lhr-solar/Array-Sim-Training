# MPPT Algorithm Beginner Project
## Overview
For th beginner project, you will implement the Perturb and Observe (PandO) algorithm in the Array Simulator. This will involve implementing the PandO class in PandO.py in the array simulator.

## Algorithm Explanation
This algorithm is in the class of Hill-Climbing algorithms, which means we are trying to climb to the "top" of the curve using past data.
The algorithm is quite novel, but it is popularly used because of its ease of implementation.
The algorithm:
1. Calculate the power at your current point (current * voltage)
2. Calculate $\Delta P$, the difference between your current power and your previous power.
3. Calculate $\Delta V$, the difference between your current voltage value and your previous voltage value
4. Take a fixed stride in voltage either left or right given one of the following conditions:

    - If $\Delta V > 0$ and $\Delta P > 0$, take a stride in positive direction (right)
    -  If $\Delta V > 0$ and $\Delta P <> 0$, take a stride in negative direction (left)
    - If $\Delta V < 0$ and $\Delta P < 0$, take a stride in positive direction (right)
    - If $\Delta V < 0$ and $\Delta P > 0$, take a stride in negative direction (right)

There are a few things to consider:

- First, at the beginning, you will not have a difference between your current voltage and previous voltage because you have not encountered a previous voltage, and your current voltage will start at 0.
- You will also need instance variables in the class that store the old voltage and the old power in order to keep track of them.
