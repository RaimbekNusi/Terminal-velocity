"Raimbek Nussipkhozhin, NFU892, 11313819, Jeffrey Long"
"Question 4"
import math as s
m = float(input("Please enter the mass of the object: "))
g = float(input("Please enter the acceleration of the object: "))
p = float(input("Please enter the viscosity of the object: "))
A = float(input("Please enter the surface area: "))
Cd = float(input("Please enter the drag coefficient: "))
def terminal_velocity(m, g, p, A, Cd):
 """
 This function computes the terminal velocity of the object
 m: a float for the mass of the object
 g: a float for the velocity of the object
 p: a float for the viscosity of the object
 A: a float for a surface area
 Cd: a float for the drag coefficient
 Vt: a float fot the terminal velocity
 returns: a float value of the terminal velocity of the object
 """
 Vt = s.sqrt((2*m*g)/(p*A*Cd))
 return Vt
print("The terminal velocity of the object is: " + str(terminal_velocity(m, g, p, A, Cd)) + "!")
