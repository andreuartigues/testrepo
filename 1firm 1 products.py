import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['lines.linewidth'] = 0.75
plt.rcParams['axes.formatter.limits'] = [-4, 4]
plt.rcParams.update({'font.family': 'Times New Roman', 'mathtext.fontset': 'cm'})
plt.rcParams['figure.dpi'] = 120
import matplotlib.pyplot as plt
import numpy as np

#Demand function price = A-B(output) constants
A = 250 ; B = 0.8; Q = 150; k = 5

suppliers = {
     "thermal": {'p_min':25, 'p_max':130 ,'a': 0.023, 'b': 0, 'c': 100, 'irc':0},
     "wind":  {'p_min':25, 'p_max':100,'a_w': 0.0011,'b_w':1.6 , 'c_w': 10,'irc': 0},
     "solar": {'p_min':0, 'p_max':25 ,'o_pv': 100,'m_pv':0, 'p_annual': 200,'irc':0}}


from scipy.optimize import fsolve


# Define the function that returns the values of the equations
def equations(x):
    t, w, s, λ = x
    eq1 = A-λ-suppliers['thermal']['b']-2*B*(t+w+s)-(2*suppliers['thermal']['a'])*t 
    eq2 = A-λ-suppliers['wind']['b_w']-2*B*(t+w+s)-(2*suppliers['wind']['a_w'])*w
    eq3 = A-λ-((suppliers['solar']['o_pv']+suppliers['solar']['m_pv'])/(suppliers['solar']['p_annual']))-2*B*(t+w+s)-np.exp(k*(s-suppliers['solar']['p_max']))
    eq4 = t+w+s-Q
    return [eq1, eq2, eq3, eq4]



# Set the initial guess
x0 = [50, 60, 50, -30]
solution = fsolve(equations, x0)

print('Power',solution[:-1])
