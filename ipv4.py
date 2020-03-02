"""
DEFANGING AN IP ADDRESS
https://leetcode.com/problems/defanging-an-ip-address/

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

ADDRESS IS IPv4
"""

def defangIPaddr(address): #input = String
    """
    :type address: str
    :rtype: str
    """
    #runtime 4ms
    string = "" 
    for x in address: 
        if x == ".": 
            string += "[.]" 
        else: 
            string += x 
    return string
    
    #return address.replace(".", "[.]") #runtime 16ms

print(defangIPaddr("1.1.1.1"))
print(defangIPaddr("255.100.50.0"))
