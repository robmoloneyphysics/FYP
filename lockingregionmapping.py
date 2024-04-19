# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 21:53:29 2024

@author: rober
"""

#Class A locking and unlocking
import matplotlib.pyplot as plt

def plot_graph(x1, y1, x2, y2):
    plt.plot(x1, y1, label='Locking ')
    plt.plot(x2, y2, label='Unlocking')
    plt.xlabel('Detuning (∆) Hz')
    plt.ylabel('Injection rate K')
    plt.title('Locking diagram for class A optically injected laser')
    
    plt.legend()
    plt.axvline(0, color='black', linewidth=0.5)  # Adding vertical line at x=0
    plt.ylim(0, 0.12)
    plt.yticks([0, 0.0125, 0.025, 0.0375, 0.05, 0.0625, 0.075, 0.0875, 0.1, 0.1125])
    plt.grid(False)  # Turning off grid
    plt.show()
   


x_values1 = [0, -0.07452, -0.141467,-0.202175 ,-0.258023 ]
y_values1 = [0, 0.025, 0.05, 0.075, 0.1]

x_values2 = [0, 0.084667, 0.138892, 0.304512, 0.412421]
y_values2 = [0, 0.025, 0.05, 0.075, 0.1,]

plot_graph(x_values1, y_values1, x_values2, y_values2)

