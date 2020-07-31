#       ============
#       Assignment 200
#       ============
#
#       Python:   3.8.5
#
#       Author:   Michael B. Darlow
#
#       Purpose:   The Tech Academy -- Python Course. Encapsulation Assignment.
#                       Create a class that uses encapsulation.
#
#       Requirements:   -Class makes use of a private attribute or function.
#                               -Class makes use of a protected attribute or function.
#                               -Create an object that makes use of protected and private.
#                       
#
#
#


class Protected:
    _protectedNum = 2
    def __init__(self):
        self.__privateNum = 3
    def getPrivate(self):
        print(self.__privateNum)
    def setPrivate(self, private):
        self.__privateNum = private

num1 = Protected()
num1._protectedNum = 52
print(num1._protectedNum)

num2 = Protected()
num2.getPrivate()
num2.setPrivate(53)
num2.getPrivate()

