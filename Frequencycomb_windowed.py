import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt


# Load the dataset containing R, PHI, and T
# Assuming you have three arrays: R, PHI, and T
# Replace these arrays with your actual dataset
from scipy.signal import find_peaks
import pandas as pd
df = pd.read_excel("C:\\Users\\rober\\OneDrive\\Desktop\\FYP\\Electric field\\Excel files\\K=0.1Delta=-0.27Efield.xlsx")

T = (df['T'].values)/1e11
R = df['R'].values
PHI = df['PHI'].values


# Compute the complex electric field E(t)
E_t = R * np.cos(PHI) + 1j * R * np.sin(PHI)
#E_field_detrended = E_t - np.mean(E_t)

window = np.hanning(len(E_t))
E_fwindowed = E_t * window

# Perform FFT
E_f = fft((E_fwindowed))


# Assuming T represents the time values, calculate the corresponding frequency values
dt = T[1] - T[0]  # Assuming uniform time sampling
frequencies = np.fft.fftfreq(len(T), dt)
frequencies_GHz = frequencies/1e11 + 1

peaks, _ = find_peaks(np.abs(E_f), height=0)

# Get the frequencies corresponding to the peaks
peak_freqs = frequencies[peaks]

# Sort the peaks by magnitude
sorted_peak_indices = np.argsort(np.abs(E_f[peaks]))[::-1]
sorted_peak_freqs = peak_freqs[sorted_peak_indices]

# Calculate the frequency difference between the first and second tallest peaks
distance_between_peaks = np.abs(sorted_peak_freqs[7] - sorted_peak_freqs[8])
print("Distance between the first and second tallest peaks:", distance_between_peaks)

# Plotting the FFT magnitude spectrum (optional)
plt.figure(figsize=(10, 6))
plt.plot(frequencies_GHz, (np.abs(E_f)), linewidth  = 0.75,color = 'navy')
plt.yscale('log')
plt.xlabel('Frequency (THz)', fontsize = 14 )
plt.ylabel('Magnitude', fontsize = 14)
plt.title('Frequency comb for optically injected class A laser K = 0.1 ∆ = -0.27', fontsize = 14)
plt.grid(False)

# Limiting the x-axis range
plt.xlim(0.7,1.5)
plt.ylim(1e0)


plt.show()
