from numpy import *
from math import *

o = array([0, 0, 0, 0])
s = 120 / 180.0 * pi
ry = array([
    [ cos(s), 0, sin(s), 0],
    [      0, 1,      0, 0],
    [-sin(s), 0, cos(s), 0],
    [      0, 0,      0, 0]
]) 
rz = array([
    [cos(s), -sin(s), 0, 0],
    [sin(s),  cos(s), 0, 0],
    [     0,       0, 1, 0],
    [     0,       0, 0, 1]
]) 
v1 = array([0, 0, 4000, 0])
v2 = dot(v1, ry)
v3 = dot(v2, rz)
v4 = dot(v3, rz)
print(v1)
print(v2)
print(v3)
print(v4)
