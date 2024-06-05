import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parámetros de la señal
carrier_freq = 1000  # Frecuencia de la portadora en Hz
modulator_freq = 500  # Frecuencia del modulador en Hz
modulation_index = 2  # Índice de modulación

# Tiempo de muestreo
sampling_freq = 10 * carrier_freq  # El teorema de Nyquist requiere una frecuencia de muestreo al menos el doble de la frecuencia de la portadora
duration = 1  # Duración de la señal en segundos
t = np.linspace(0, duration, duration * sampling_freq, endpoint=False)

# Generación de la señal de la portadora
carrier_wave = np.sin(2 * np.pi * carrier_freq * t)

# Generación de la señal del modulador
modulator_wave = np.sin(2 * np.pi * modulator_freq * t)

# Modulación FM
modulated_wave = np.sin(2 * np.pi * (carrier_freq + modulation_index * modulator_wave) * t)

# Plots en el dominio del tiempo
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(t[:len(t)//10], carrier_wave[:len(t)//10])
plt.title(r'$Portadora$')
plt.xlabel(r'$Tiempo\;[s]$')
plt.ylabel(r'$Amplitud$')

plt.subplot(3, 1, 2)
plt.plot(t[:len(t)//10], modulator_wave[:len(t)//10])
plt.title(r'$Modulante$')
plt.xlabel(r'$Tiempo\;[s]$')
plt.ylabel(r'$Amplitud$')

plt.subplot(3, 1, 3)
plt.plot(t[:len(t)//10], modulated_wave[:len(t)//10])
plt.title(r'$Señal\;modulada$')
plt.xlabel(r'$Tiempo\;[s]$')
plt.ylabel(r'$Amplitud$')

plt.tight_layout()

# Plots en el dominio de la frecuencia
plt.figure(figsize=(10, 8))

# Espectro de la portadora
frequencies, spectrum_carrier = signal.periodogram(carrier_wave, sampling_freq)
plt.subplot(3, 1, 1)
plt.plot(frequencies[:len(t)//2], spectrum_carrier[:len(t)//2])
plt.title(r'$Portadora$')
plt.xlabel(r'$Frecuencia\;[Hz]$')
plt.ylabel(r'$Amplitud$')

# Espectro del modulador
frequencies, spectrum_modulator = signal.periodogram(modulator_wave, sampling_freq)
plt.subplot(3, 1, 2)
plt.plot(frequencies[:len(t)//2], spectrum_modulator[:len(t)//2])
plt.title(r'$Modulante$')
plt.xlabel(r'$Frecuencia\;[Hz]$')
plt.ylabel(r'$Amplitud$')
# Espectro de la señal modulada
frequencies, spectrum_modulated = signal.periodogram(modulated_wave, sampling_freq)
plt.subplot(3, 1, 3)
plt.plot(frequencies[:len(t)//2], spectrum_modulated[:len(t)//2])
plt.title(r'$Señal\;modulada$')
plt.xlabel(r'$Frecuencia\;[Hz]$')
plt.ylabel(r'$Amplitud$')

plt.tight_layout()

plt.show()
