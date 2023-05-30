# This Python code uses sympy to find the center of circumscribing circle using vector algebra.
# It uses right bisectors planes of two legs of triangle and the plane containing the three points (obtained by cross product of triangle legs)
# Then it solves those three equations linearly by using SYMPY to obtain the center of circle.
# 
from sympy import symbols, Eq, solve
import numpy as np


def find_circle_center(p1,p2,p3):
    p1=np.array(p1)
    p2=np.array(p2)
    p3=np.array(p3)
    p1_p2_mean=(p1+p2)/2
    p1_p2_vec=(p1-p2)

    p2_p3_mean=(p2+p3)/2
    p2_p3_vec=(p2-p3)


    circle_plane_normal=np.cross(p1_p2_vec,p2_p3_vec)
    # defining symbols used in equations
    # or unknown variables
    x, y, z = symbols('x,y,z')

    # defining equations
    eq1 = Eq(((x-p1_p2_mean[0])*p1_p2_vec[0]+(y-p1_p2_mean[1])*p1_p2_vec[1]+(z-p1_p2_mean[2])*p1_p2_vec[2]), 0)
    #print("Equation 1:")
    #print(eq1)

    eq2 = Eq(((x-p2_p3_mean[0])*p2_p3_vec[0]+(y-p2_p3_mean[1])*p2_p3_vec[1]+(z-p2_p3_mean[2])*p2_p3_vec[2]), 0)
    #print("Equation 2:")
    #print(eq2)

    eq3 = Eq(((x-p2_p3_mean[0])*circle_plane_normal[0]+(y-p2_p3_mean[1])*circle_plane_normal[1]+(z-p2_p3_mean[2])*circle_plane_normal[2]), 0)
    #print("Equation 3:\n", eq3 )

    # solving the equation and printing the 
    # value of unknown variables
    print("Values of 3 unknown variable  aka \nCircle Center (x,y,z) are as follows:")
    print(solve((eq1, eq2, eq3), (x, y, z)))
    center_of_circle=solve((eq1, eq2, eq3), (x, y, z))
    center_of_circle=np.asarray(list(center_of_circle.values()))
    return center_of_circle.astype(float)
