#       ============
#       Assignment 202
#       ============
#
#       Python:   3.8.5
#
#       Author:   Michael B. Darlow
#
#       Purpose:   The Tech Academy -- Python Course. Abstraction Assignment.
#                       Create a class that utilizes abstraction.
#
#       Requirements:   -Class contains at least one abstract method and one regular method.
#                               -Child class that defines the implementation of its parent's abstract method.
#                               -Create an object that utilizes both parent and child methods.
#                       
#
#
#

from abc import ABC, abstractmethod
class Abs_Class(ABC):
    def print_this(self, num):
        print("print_this\' passed value: ", num)
    @abstractmethod
    def print_this2(self, num):
        pass
 
class Child_Class(Abs_Class):
    def print_this2(self, num):
        print("print_this2's passed value: ", num)

obj = Child_Class()
obj.print_this("1")
obj.print_this2("0")

