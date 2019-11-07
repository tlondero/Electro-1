import matplotlib.pyplot as plt
import numpy as np
import pandas as pnd
from SpiceParser import SpiceParser

#GANACIA DE V

df = pnd.read_csv('./Darlington/Av.csv', sep=',')
freq_m_av = np.asarray(df["Frequency (Hz)"])
mag_m_av = np.asarray(df["Channel 2 Magnitude (dB)"])
pha_m_av = np.asarray(df["Channel 2 Phase (*)"])

df = pnd.read_csv('./Darlington/Avs.csv', sep=',')
freq_m_avs = np.asarray(df["Frequency (Hz)"])
mag_m_avs = np.asarray(df["Channel 2 Magnitude (dB)"])
pha_m_avs = np.asarray(df["Channel 2 Phase (*)"])

lt_parser = SpiceParser()
data = lt_parser.parse('./Darlington/Av.txt')
freq_s_av = np.array(data[1].index)
mag_s_av = np.array(data[0]["V(vout)/V(n002) MAG"])
pha_s_av = np.array(data[1]["V(vout)/V(n002) PHA"])

data = lt_parser.parse('./Darlington/Avs.txt')
freq_s_avs = np.array(data[1].index)
mag_s_avs = np.array(data[0]["V(vout)/V(vin) MAG"])
pha_s_avs = np.array(data[1]["V(vout)/V(vin) PHA"])

#IMPEDANCIA DE ENTRADA

df = pnd.read_csv('./Darlington/Ria.csv', sep=',')
freq_m_ria = np.asarray(df["Frequency (Hz)"])
mag_m_ria = np.asarray(df["Trace |Z| (Ohm)"])
pha_m_ria = np.asarray(df["Trace th (*)"])

df = pnd.read_csv('./Darlington/Ris.csv', sep=',')
freq_m_ris = np.asarray(df["Frequency (Hz)"])
mag_m_ris = np.asarray(df["Trace |Z| (Ohm)"])
pha_m_ris = np.asarray(df["Trace th (*)"])

lt_parser = SpiceParser()
data = lt_parser.parse('./Darlington/Ria.txt')
freq_s_ria = np.array(data[1].index)
mag_s_ria = 10**(np.array(data[0]["V(n002)/I(I1) MAG"])/20)
pha_s_ria = np.array(data[1]["V(n002)/I(I1) PHA"])

data = lt_parser.parse('./Darlington/Ris.txt')
freq_s_ris = np.array(data[1].index)
mag_s_ris = 10**(np.array(data[0]["V(vin)/I(I1) MAG"])/20)
pha_s_ris = np.array(data[1]["V(vin)/I(I1) PHA"])

#IMPEDANCIA DE SALIDA

df = pnd.read_csv('./Darlington/Ros.csv', sep=',')
freq_m_ros = np.asarray(df["Frequency (Hz)"])
mag_m_ros = np.asarray(df["Trace |Z| (Ohm)"])
pha_m_ros = np.asarray(df["Trace th (*)"])

data = lt_parser.parse('./Darlington/Ros.txt')
freq_s_ros = np.array(data[1].index)
mag_s_ros = 10**(np.array(data[0]["V(vout)/I(I1) MAG"])/20)
pha_s_ros = np.array(data[1]["V(vout)/I(I1) PHA"])

plt.title("Ganancia de tesión del amplificador $\Delta V$")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud [dB]")
plt.plot(freq_m_av, mag_m_av, label = "Medido")
plt.plot(freq_s_av, mag_s_av, label = "Simulado")
plt.xscale('log')
plt.legend()
plt.grid()
plt.show()

plt.title("Ganancia de tesión del sistema $\Delta V_S$")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud [dB]")
plt.plot(freq_m_avs, mag_m_avs, label = "Medido")
plt.plot(freq_s_avs, mag_s_avs, label = "Simulado")
plt.xscale('log')
plt.legend()
plt.grid()
plt.show()

plt.title("Impedancia de entrada del amplificador $R_{ia}$")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Impedancia [k$\Omega$]")
plt.plot(freq_m_ria, mag_m_ria*1E-3, label = "Medido")
plt.plot(freq_s_ria, mag_s_ria*1E-3, label = "Simulado")
plt.xscale('log')
plt.legend()
plt.grid()
plt.show()

plt.title("Impedancia de entrada del sistema $R_{is}$")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Impedancia [k$\Omega$]")
plt.plot(freq_m_ris, mag_m_ris*1E-3, label = "Medido")
plt.plot(freq_s_ris, mag_s_ris*1E-3, label = "Simulado")
plt.xscale('log')
plt.legend()
plt.grid()
plt.show()

plt.title("Impedancia de salida del sistema $R_{os}$")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Impedancia [k$\Omega$]")
plt.plot(freq_m_ros, mag_m_ros*1E-3, label = "Medido")
plt.plot(freq_s_ros, mag_s_ros*1E-3, label = "Simulado")
plt.xscale('log')
plt.legend()
plt.grid()
plt.show()
