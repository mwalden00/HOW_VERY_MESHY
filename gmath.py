import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    len = math.sqrt(vector[0]*vector[0] + vector[1]*vector[1] + vector[2]*vector[2])
    return [vector[0]/len, vector[1]/len, vector[2]/len]

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    p1 = polygons[i]
    p2 = polygons[i + 1]
    p3 = polygons[i + 2]
    a = [p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2]]
    b = [p1[0] - p3[0], p1[1] - p3[1], p1[2] - p3[2]]
    n = [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - b[2]*a[0], a[0]*b[1] - a[1]*b[0]]
    return n
