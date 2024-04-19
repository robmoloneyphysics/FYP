import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_excel("C:\\Users\\rober\\OneDrive\\Desktop\\FYP\\Period log combined.xlsx")

Delta075 = (df['Delta0.075'].values)
Period075 = (df['Period0.075'].values)

Delta1 = (df['Delta0.1'].values)
Period1 = (df['Period0.1'].values)

Delta05 = (df['Delta0.05'].values)
Period05 = (df['Period0.05'].values)

Delta025 = (df['Delta0.025'].values)
Period025 = (df['Period0.025'].values)


plt.figure(figsize=(12, 6))

plt.subplot(1, 4, 2)  # (rows, columns, plot_number)
plt.plot(Delta075, Period075, color='k')
plt.title('K = 0.075')
plt.yscale('log')
plt.xlabel('∆')
plt.ylabel('Period(s)')


plt.subplot(1, 4, 1)  # (rows, columns, plot_number)
plt.plot(Delta1, Period1, color='c')
plt.title('K =0.1')
plt.xlabel('∆')
plt.ylabel('Period(s)')

plt.subplot(1, 4, 3)  # (rows, columns, plot_number)
plt.plot(Delta05, Period05, color='blue')
plt.title('K = 0.05')
plt.xlabel('∆')
plt.ylabel('Period(s)')

plt.subplot(1, 4, 4)  # (rows, columns, plot_number)
plt.plot(Delta025, Period025, color='red')
plt.title('K = 0.025')
plt.xlabel('∆')
plt.ylabel('Period(s)')


plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()
