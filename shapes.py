# Shapes
import matplotlib.pyplot as plt
import numpy as np

## Waves
def sineWave(f=10, oversamp=30, show=True):
    # Sin Wave
    f = f;                   # MHz
    overSampRate = oversamp; # oversampling rate
    fs = f*overSampRate
    phase = 1.0/3 * np.pi; # desired phase shift in radians
    nCycl = 5;             # number of cycles
    t = np.arange(0, nCycl/float(f) - 1./fs, 1./fs);
    g = np.sin(2*np.pi*f*t + phase);
    if show:
        plt.figure();
        plt.plot(t, g);
        plt.title("Sine Wave (f = " + str(f) + " MHz)");
        plt.xlabel("Time (s)");
        plt.ylabel("Amplitude");
        plt.show();
    return (t, g)

def squareWave(f=10, oversamp=30, show=True):
    f = 10;                  # MHz
    overSampRate = oversamp; # oversampling rate
    fs = f*overSampRate;
    nCycl = 5;             # number of cycles
    t = np.arange(0, nCycl/float(f) - 1./fs, 1./fs);
    g = np.sign(np.sin(2*np.pi*f*t));
    if show:
        plt.figure();
        plt.plot(t, g);
        plt.title("Square Wave (f = " + str(f) + " MHz)");
        plt.xlabel("Time (s)");
        plt.ylabel("Amplitude");
        plt.show();
    return (t, g)

## Pulses
def rectPulse(T=0.2, show=True):
    fs = 500; # sampling frequency
    T  = T; # width of pulse in seconds
    t  = np.arange(-0.5, 0.5, 1./fs);
    g  = (t > -T/2) * (t < T/2) + 0.5*(t == T/2) + 0.5*(t == -T/2);
    if show:
        plt.figure();
        plt.plot(t, g);
        plt.title("Rectangular Pulse (width = " + str(T) + "s)");
        plt.xlabel("Time (s)");
        plt.ylabel("Amplitude");
        plt.show();
    return (t, g)

def gaussianPulse(sigma=0.1, show=True):
    fs    = 80; # sampling frequency
    sigma = sigma; # width of pulse in seconds
    t  = np.arange(-0.5, 0.5, 1./fs);
    g  = np.exp(-t**2 / (2*sigma**2))/(np.sqrt(2*np.pi) * sigma);
    if show:
        plt.figure();
        plt.plot(t, g);
        plt.title("Gaussian Pulse (sigma = " + str(sigma) + "s)");
        plt.xlabel("Time (s)");
        plt.ylabel("Amplitude");
        plt.show();
    return (t, g)

## Chirp
def chirp_signal(t, f0, t1, f1, phase=0):
    t0 = t[0]; T = t1-t0; k = (f1-f0)/T;
    return np.cos(2*np.pi*(k/2*t+f0)*t + phase)

def chirpTest(f0=1, show=True):
    fs = 500; t0 = 0; t1 = 1;
    t  = np.arange(t0, t1, 1./fs);
    f1 = fs/20.;
    g  = chirp_signal(t, f0, t1, f1);
    if show:
        plt.figure();
        plt.plot(t, g);
        plt.title("Chirp Signal");
        plt.xlabel("Time (s)");
        plt.ylabel("Amplitude");
        plt.show();
    return (t, g)

################################################################################
if __name__ == "__main__":
    sineWave()
    squareWave()
    rectPulse()
    gaussianPulse()
    chirpTest()