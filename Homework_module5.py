""" Homework 5 - needs to be presented before exam day"""

# We want to create class for an object that behaves like a triangle, that has flexible sides and angles.
# Because of approximations in python the triangle will get distorted after some of the changes so this is not a
# perfect model
# 30P
#  - class constructor can receives 3 arguments for angles (with default value of 60) and 3 arguments for sides (with
# default value of 1)
# class variables for sides will be called A, B, C
# class variables for angles will be called AB, BC, CA (indicating sides)

# 30P
# - class implements method to modify_angle:
#   - modify_angle method takes two argument:
#       - "angle" and can be one of 3 string values 'AB', 'BC', 'CA'
#       - "degrees" that can be a positive or negative and represents the amount by which the angle will be modified
# If as a result of the change any of the angles will be outside interval (0, 180) then method should raise an exception
# When an angel is modifies you will need to recalculate the opposing side which can be done using the following
# example: angle AB is changed then C = (A**2 + B**2 - 2*A*B*cos(AB))**(1/2)
# Because angles in a triangle must sum up to 180 degrees unmodified angles need to be recalculated after we have
# recalculated the opposite side using the following example:
# angle AB is changed then BC = arccos((B**2+ C**2 - A**2) / 2*B*C), CA = arccos((C**2+ A**2 - B**2) / 2*C*A),

# 30P
# - class implements method to modify_side:
#   - modify_side method takes two argument:
#       - "side" and can be one of 3 string values 'A', 'B', 'C'
#       - "meters" that can be a positive or negative and represents the amount by which the side will be modified
# If as a result of the change sum of the unmodified sides is less then or equal to the changed side then method should
# throw an exception
# If as a result of the change side will be less then or equal to 0 then method should raise a different exception
# When a side is modified by some value all other sides need to be modified by the fraction of the change to maintain
# the same triangle angles. For example if A increase by +1 then B = ((A+1)/A)*B and C = ((A+1)/A)*C
# 10P
# Create an object from your class with default constructor values and modify angle AB by +30 degrees and side A by +1.5

from math import cos, acos, degrees
import Homework_module5_Exceptions as My_exception


class Triangle:
    def __init__(self, a=1, b=1, c=1, ab=60, bc=60, ca=60):
        self.A = a
        self.B = b
        self.C = c
        self.AB = ab
        self.BC = bc
        self.CA = ca
        self.modify_side('A', 0.5)
        self.modify_angle('AB', 30)

    def modify_angle(self, angle, degrees):
        if angle == 'AB':
            self.AB += degrees
            if self.AB > 180:
                raise My_exception.ValueToBig
            elif self.AB < 0:
                raise My_exception.ValueToSmall
            print(self.C)
            self.C = (self.A ** 2 + self.B ** 2 - 2 * self.A * self.B * cos(self.AB)) ** (1 / 2)
            # acos can be calculated within the interval [-1,1] everything that would not be in this interval
            # will cause a ValueError.
            self.BC = acos((self.B ** 2 + self.C ** 2 - self.A ** 2) / (2 * self.B * self.C))
            self.CA = acos((self.C ** 2 + self.A ** 2 - self.B ** 2) / (2 * self.C * self.A))
        elif angle == 'BC':
            self.BC += degrees
            if self.BC > 180:
                raise My_exception.ValueToBig
            elif self.BC < 0:
                raise My_exception.ValueToSmall
            self.A = (self.C ** 2 + self.B ** 2 - 2 * self.C * self.B * cos(self.BC)) ** (1 / 2)
            self.AB = acos((self.B ** 2 + self.B ** 2 - self.C ** 2) / (2 * self.A * self.B))
            self.CA = acos((self.C ** 2 + self.A ** 2 - self.B ** 2) / (2 * self.C * self.A))
        elif angle == 'AC':
            self.CA += degrees
            if self.CA > 180:
                raise My_exception.ValueToBig
            elif self.CA < 0:
                raise My_exception.ValueToSmall
            self.B = (self.C ** 2 + self.A ** 2 - 2 * self.C * self.A * cos(self.CA)) ** (1 / 2)
            self.AB = acos((self.B ** 2 + self.B ** 2 - self.C ** 2) / (2 * self.A * self.B))
            self.BC = acos((self.C ** 2 + self.B ** 2 - self.A ** 2) / (2 * self.C * self.B))
        else:
            raise My_exception.InvalidAngleName
        print("AB angle is:", self.AB)
        print("BC angle is:", self.BC)
        print("CA angle is:", self.CA)

    def modify_side(self, side, meters):
        if side == 'A':
            self.A += meters
            if self.A <= 0:
                raise My_exception.SmallSideValue
            elif self.B + self.C <= self.A:
                raise My_exception.LargeSideValue
            self.B = ((self.A + meters) / self.A) * self.B
            self.C = ((self.A + meters) / self.A) * self.C
        elif side == 'B':
            self.B += meters
            if self.B <= 0:
                raise My_exception.SmallSideValue
            elif self.A + self.C <= self.B:
                raise My_exception.LargeSideValue
            self.A = ((self.B + meters) / self.B) * self.A
            self.C = ((self.B + meters) / self.B) * self.C
        elif side == 'C':
            self.C += meters
            if self.C <= 0:
                raise My_exception.SmallSideValue
            elif self.A + self.B <= self.C:
                raise My_exception.LargeSideValue
            self.B = ((self.C + meters) / self.C) * self.B
            self.A = ((self.C + meters) / self.C) * self.A
        else:
            raise My_exception.InvalidSideName
        print("A side is:", self.A)
        print("B side is:", self.B)
        print("C side is:", self.C)


ObjTriangle = Triangle()
ObjTriangle.modify_angle('AB', 30)
ObjTriangle.modify_side('A', 0.5)
# <your code here>
