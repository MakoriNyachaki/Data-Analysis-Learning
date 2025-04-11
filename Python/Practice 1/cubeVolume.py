# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 06:21:48 2023

@author: Lenovo
"""

## Computes the volume of a cube
# @param sideLength length of a side of the cube
# @return the volume of the cube
#
from typing import Union

def cubeVolume(sideLength : Union[int, float]) -> Union[int, float]:
    volume = sideLength ** 3
    return(volume)

print(f'Volume int: {cubeVolume(4)}')
print(f'Volume float: {cubeVolume(2.5)}')