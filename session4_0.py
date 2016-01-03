from numpy import *
from math import *
import itertools

g = (1.0 + sqrt(5)) / 2.0
v = []
v.append(array([+1.0, +g  ,  0.0, 0.0]))
v.append(array([-1.0, +g  ,  0.0, 0.0]))
v.append(array([+1.0, -g  ,  0.0, 0.0]))
v.append(array([-1.0, -g  ,  0.0, 0.0]))
v.append(array([ 0.0, +1.0,   +g, 0.0]))
v.append(array([ 0.0, -1.0,   +g, 0.0]))
v.append(array([ 0.0, +1.0,   -g, 0.0]))
v.append(array([ 0.0, -1.0,   -g, 0.0]))
v.append(array([  +g,  0.0, +1.0, 0.0]))
v.append(array([  -g,  0.0, +1.0, 0.0]))
v.append(array([  +g,  0.0, -1.0, 0.0]))
v.append(array([  -g,  0.0, -1.0, 0.0]))
o = array([0, 0, 0, 0])
s = 120 / 180.0 * pi
rs = array([
    [ 1000,    0,    0, 0],
    [    0, 1000,    0, 0],
    [    0,    0, 1000, 0],
    [    0,    0,    0, 1],
]) 
for vv in v:
    vv = dot(vv, rs)
    print(vv)

for element in itertools.combinations(xrange(len(v)), 3):
    v0 = v[element[0]]
    v1 = v[element[1]]
    v2 = v[element[2]]
    n0 = linalg.norm(v0 - v1)
    n1 = linalg.norm(v1 - v2)
    n2 = linalg.norm(v2 - v0)
    if n0 == 2.0 and n1 == 2.0 and n2 == 2.0:
        print(element, n0, n1, n2)
