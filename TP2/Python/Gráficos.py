import matplotlib.pyplot as plt
import numpy as np
import pandas as pnd
from SpiceParser import SpiceParser

freq_teo_1 = np.logspace(2, 6, 300)
freq_teo_2 = np.logspace(3, 6, 300)
freq_teo_3 = np.logspace(2, 6, 300)

av_db = freq_teo_1*0 - 0.09004275199198589 #- 0.08970650365039494
avs_db = freq_teo_1*0 - 0.8139629700664324  #- 0.8432197260313168
ai_db = freq_teo_3*0 + 9.203870424010491 # 8.841197029645336

zia = freq_teo_2*0 + 6442.997049785562 # + 6179.27396184769
zis = freq_teo_2*0 + 6442.997049785562 + 560 #+ 6179.27396184769 + 560
zo = freq_teo_2*0 + 16.097079622947092 #16.06739415843958


#GANACIA DE V

df = pnd.read_csv('./Darlington/Av.csv', sep=',')
freq_m_av = np.asarray(df["Frequency (Hz)"])
mag_m_av = np.asarray(df["Channel 2 Magnitude (dB)"])
pha_m_av = np.asarray(df["Channel 2 Phase (*)"])

df = pnd.read_csv('./Darlington/Avs.csv', sep=',')
freq_m_avs = np.asarray(df["Frequency (Hz)"])
mag_m_avs = np.asarray(df["Channel 2 Magnitude (dB)"]) #+ 0.65
pha_m_avs = np.asarray(df["Channel 2 Phase (*)"])

lt_parser = SpiceParser()
data = lt_parser.parse('./Darlington/Av.txt')
freq_s_av = np.array(data[1].index)
mag_s_av = np.array(data[0]["V(Vout)/V(n002) MAG"])
pha_s_av = np.array(data[1]["V(Vout)/V(n002) PHA"])

data = lt_parser.parse('./Darlington/Avs.txt')
freq_s_avs = np.array(data[1].index)
mag_s_avs = np.array(data[0]["V(vout)/V(vin) MAG"])
pha_s_avs = np.array(data[1]["V(vout)/V(vin) PHA"])

#IMPEDANCIA DE ENTRADA

suav_ria = 1E6
suav_ris = 1E6
suav_ros = 10

df = pnd.read_csv('./Darlington/Ria_fixed.csv', sep=',')
freq_m_ria = np.asarray(df["Frequency (Hz)"])
mag_m_ria = np.asarray(pnd.DataFrame(df["Trace |Z| (Ohm)"]).ewm(com=suav_ria).mean())
#mag_m_ria = np.asarray(pnd.DataFrame(df["Trace |Z| (Ohm)"]))
pha_m_ria = np.asarray(df["Trace th (*)"])

df = pnd.read_csv('./Darlington/Ris_fixed.csv', sep=',')
freq_m_ris = np.asarray(df["Frequency (Hz)"])
mag_m_ris = np.asarray(pnd.DataFrame(df["Trace |Z| (Ohm)"]).ewm(com=suav_ris).mean())
#mag_m_ris = np.asarray(pnd.DataFrame(df["Trace |Z| (Ohm)"]))
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
mag_m_ros = np.asarray(pnd.DataFrame(df["Trace |Z| (Ohm)"]).ewm(com=suav_ros).mean())
pha_m_ros = np.asarray(df["Trace th (*)"])

data = lt_parser.parse('./Darlington/Ros.txt')
freq_s_ros = np.array(data[1].index)
mag_s_ros = 10**(np.array(data[0]["V(vout)/I(I1) MAG"])/20)
pha_s_ros = np.array(data[1]["V(vout)/I(I1) PHA"])

#GRÁFICOS

plt.plot(freq_s_av, mag_s_av, label = "Simulado")
plt.title("Ganancia de tesión del amplificador $\Delta V$")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Ganancia [dB]")
plt.plot(freq_m_av, mag_m_av, label = "Medido")

plt.plot(freq_teo_1, av_db, label = "Teórico", color='r')

plt.xscale('log')
plt.legend()
plt.grid()
plt.show()

plt.title("Ganancia de tesión del sistema $\Delta V_S$")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Ganancia [dB]")
plt.plot(freq_m_avs, mag_m_avs, label = "Medido")
plt.plot(freq_s_avs, mag_s_avs, label = "Simulado")

plt.plot(freq_teo_1, avs_db, label = "Teórico", color='r')

plt.xscale('log')
plt.legend()
plt.grid()
plt.show()

plt.title("Impedancia de entrada del amplificador $R_{ia}$")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Impedancia [k$\Omega$]")
plt.plot(freq_m_ria, mag_m_ria*1E-3, label = "Medido")
plt.plot(freq_s_ria, mag_s_ria*1E-3, label = "Simulado")

plt.plot(freq_teo_2, zia*1E-3, label = "Teórico", color='r')

plt.xscale('log')
plt.legend()
plt.grid()
plt.show()

plt.title("Impedancia de entrada del sistema $R_{is}$")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Impedancia [k$\Omega$]")
plt.plot(freq_m_ris, mag_m_ris*1E-3, label = "Medido")
plt.plot(freq_s_ris, mag_s_ris*1E-3, label = "Simulado")

plt.plot(freq_teo_2, zis*1E-3, label = "Teórico", color='r')

plt.xscale('log')
plt.legend()
plt.grid()
plt.show()

plt.title("Impedancia de salida del sistema $R_{os}$")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Impedancia [k$\Omega$]")
plt.plot(freq_m_ros, mag_m_ros*1E-3, label = "Medido")
plt.plot(freq_s_ros, mag_s_ros*1E-3, label = "Simulado")

plt.plot(freq_teo_2, zo*1E-3, label = "Teórico", color='r')

plt.xscale('log')
plt.legend()
plt.grid()
plt.show()

#GANANCIA DE CORRIENTE

lt_parser = SpiceParser()
data = lt_parser.parse('./Darlington/Ai.txt')
freq_s_ai = np.array(data[1].index)
mag_s_ai = np.array(data[0]["-I(Rl)/I(I1) MAG"])
pha_s_av = np.array(data[1]["-I(Rl)/I(I1) PHA"])

df = pnd.read_csv('./Darlington/Ai_3.csv', sep=',')
freq_i = np.asarray(df["Frequency (Hz)"])
ir1 = np.asarray(df["Channel 1 Magnitude (dB)"])
ir2 = np.asarray(df["Channel 2 Magnitude (dB)"])

r1 = 560
r2 = 2.21E3

i_db = 20*np.log10((10**((ir2 - ir1)/20))*r1/r2)

plt.title("Ganancia de corriente $\Delta I$")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Ganancia [$dB$]")
plt.plot(freq_i, i_db[::-1] - (np.max(i_db) - np.max(mag_s_ai)), label = "Medido")
plt.plot(freq_s_ai, mag_s_ai, label = "Simulado")

plt.plot(freq_teo_3, ai_db, label = "Teórico", color='r')

plt.xscale('log')
plt.legend()
plt.grid()
plt.show()

print(f'max ir2:{ np.max(ir2) }')
print(f'max ir1:{np.max(ir1)}')
print(f'diferencia {10**( (np.max(ir2)-np.max(ir1)) /20)}')