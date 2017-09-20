# Sin Wave
import matplotlib.pyplot as plt
import numpy as np
f = 10;                # MHz
overSampRate = 30;     # oversampling rate
fs = f*overSampRate
phase = 1.0/3 * np.pi; # desired phase shift in radians
nCycl = 5;             # number of cycles
t = np.arange(0, nCycl/float(f) - 1./fs, 1./fs);
g = np.sin(2*np.pi*f*t + phase);
plt.figure();
plt.plot(t, g);
plt.title("Sine Wave (f = " + str(f) + " MHz)");
plt.xlabel("Time (s)");
plt.ylabel("Amplitude");
plt.show();