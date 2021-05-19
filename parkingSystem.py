"""
LEETCODE - DESIGN A PARKING SYSTEM
https://leetcode.com/problems/design-parking-system/

Design a parking system for a parking lot.
The parking lot has three kinds of parking spaces: big, medium, and small,
with a fixed number of slots for each size.

Implement the ParkingSystem class:

* ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class.
The number of slots for each parking space are given as part of the constructor.
* bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.
"""
#SOLUTION (as of December 16, 2020)
# *** RUNTIME = 128 ms (faster than 77.47% of Python online submissions)
# *** MEMORY = 14.2 MB (less than 11.89% of Python online submissions)
# ---> to improve, use a dictionary in the constructor (improves by 16 ms)

class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        #big, med and small = number of slots for these sized cars
        self.big = big
        self.medium = medium
        self.small = small

        """
        self.carType = {
            1: "big",
            2: "medium",
            3: "small"
        }
        """
        
        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        #if there is space, return true and decrement
        #if zero, return False
        #CAR TYPE:
        #big = 1
        #medium = 2
        #small = 3
        
        if carType == 1:
            if self.big > 0:
                self.big -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.medium > 0:
                self.medium -= 1
                return True
            else:
                return False
        else:
            if self.small > 0:
                self.small -= 1
                return True
            else:
                return False
        """
        if self.carType[carType] == "big":
            if self.big == 0:
                return False
            self.big-=1
        elif self.carType[carType] == "medium":
            if self.medium == 0:
                return False
            self.medium-=1
        elif self.carType[carType] == "small":
            if self.small == 0:
                return False
            self.small-=1            
            
        return True
        """
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
