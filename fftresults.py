# Interpreting the FFT results
import matplotlib.pyplot as plt
import numpy as np

def main():
    # create function
    fc = 10;
    fs = 32*fc; #sampling frequency with oversampling factor
    t  = np.arange(0, 2-1./fs, 1./fs);
    x  = np.cos(2*np.pi*fc*t);
    plt.figure();
    plt.subplot(3, 1, 1);
    plt.plot(t, x);    
    plt.title("x[n] = cos(2pi*10*t)");    
    plt.xlabel("t = nT");    
    plt.ylabel("x[n]");    
    # consider N = 256 = 2^8 point FFT (DFT)
    N = 256;
    X = np.fft.fft(x, N); # output is DC at X[0], Nyquist freq @ X[N/2]
                      # Positive frequencies from X[1:N/2-1]
                      # Negative frequencies from X[N/2:N-1]
    df = fs/N;
    sampleIndex = np.arange(0, N);
    f = sampleIndex*df;
    plt.subplot(3, 1, 2); plt.stem(sampleIndex, np.abs(X));
    plt.xlabel("k"); plt.ylabel("|X(K)|");
    plt.subplot(3, 1, 3); plt.stem(f, np.abs(X));
    plt.xlabel("Frequencies (f)");
    plt.ylabel("|X(f)|");
    plt.show();

################################################################################
if __name__ == "__main__":
    main()