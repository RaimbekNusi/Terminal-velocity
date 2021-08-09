# Terminal velocity

## Description
Terminal velocity is the maximum velocity (speed) attainable by an object as it falls through a fluid (air is the most common example). It occurs when the sum of the drag force (Fd) and the buoyancy is equal to the downward force of gravity (FG) acting on the object. Since the net force on the object is zero, the object has zero acceleration. That can be approximated by:

![image](https://user-images.githubusercontent.com/86201781/128756090-d1784a47-87bd-4975-b721-ce000c702906.png)



where m is the mass of the object, g is the acceleration due to gravity (9.8m/s2), ρ is the viscosity (air is approximately 1.81e − 5kg/m/s), A is the surface area and Cd is the drag coefficient (around 1.1). The result is Vt, the maximum velocity the object will reach.

## Problem description

Write a Python function named terminal_velocity which has five parameters (i.e. the five quantities above) and returns the final velocity the object will reach. 

Also write a main program that reads the four necessary values from the user, passes the entered values
to the terminal_velocity function to perform the computation, obtains the function’s return value, then
prints a message to the console that reports the user’s future value. Function terminal_velocity
should do no console input and no console output. It must receive its input through its parameters and
send its output using a return value.

Here is an example of how your program’s console output might look. Green text was entered by the user; blue text came from data returned by the terminal_velocity function. 

![image](https://user-images.githubusercontent.com/86201781/128755977-63562e64-3f42-4a19-a5a0-721bbb0ff211.png)

## How to use

Here are the steps for how to open, use and utilize the program:

- First, download all of the files listed above;
- Put all the files in one folder;
- Open the file Projec_rock_paper.py;
- The program will open a command console which will ask you to input the mass of the object, the acceleration due to gravity, viscosity, area, and drag coefficient.
