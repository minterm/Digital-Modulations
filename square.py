# Square Wave with 50% duty cycle
import matplotlib.pyplot as plt
import numpy as np
f = 10;                # MHz
overSampRate = 30;     # oversampling rate
fs = f*overSampRate;
nCycl = 5;             # number of cycles
t = np.arange(0, nCycl/float(f) - 1./fs, 1./fs);
g = np.sign(np.sin(2*np.pi*f*t));
plt.figure();
plt.plot(t, g);
plt.title("Square Wave (f = " + str(f) + " MHz)");
plt.xlabel("Time (s)");
plt.ylabel("Amplitude");
plt.show();