import numpy as np
import matplotlib.pyplot as plt
import ODESolver as ODES

L = 1 #conditions given by problem
omega = np.sqrt(3.5)
C = 0.25
R = 0.2


class Electric_circuit:
    """
    A class for electric circuit
    """
    def __init__(self, L, omega, R, C):
        """
        constructor
        """
        self.L = L; self.omega = omega
        self.C = C; self.R = R

    def __call__(self, u, t):
        L = self.L; R = self.R
        C = self.C; omega = self.omega
        I = u[0]; Q = u[1]
        def E(t):
            #given by problem
            return 2*np.sin(omega*t)
        #du_Q = I
        #du_I = (E(t)-R*I-(Q/C))/L #tried something, didn't work, didn't have time to do it
        return (E(t)-R*I-(Q/C))/L, I


time_frame = 2*np.pi/omega #time frame given
dt = ((2*np.pi)/(60*omega)) #the dt
n = time_frame/dt #number of steps

time_points = (0, 10*time_frame, n) #time_points, goes from 0 to time_frame with n steps

problem = Electric_circuit(L, omega, R, C) #makes an instance of the Electric_circuit class
solver = ODES.RungeKutta4(problem) #takes that over to be solved by ForwardEuler method
solver.set_initial_condition((1, 1)) #sets the initial condition
u, t = solver.solve(time_points) #returns the arrays

plt.plot(t, u) #plots it
plt.show()


"""
Test run in terminal:
chris@nih:~/Documents/in1900/oblig/46$ python electric_circuit.py
Output is a plot
"""
