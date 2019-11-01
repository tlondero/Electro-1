import matplotlib.pyplot as plt
import numpy as np
import pandas as pnd
from SpiceParser import SpiceParser
# from sympy import *

freq_teo = np.logspace(1, 6, 300)

s = (1j)*2*np.pi*freq_teo

#Tensiones
vcc = 15
vss = -15
vdd = 0.7

#Resistencias
r2 = 50
rb = 680
rc = 680
rdd = 6.8E3
rs = 6.8E3
rl = 10E3

#JFET

rds =
rgs =
idss = 2E-3
vp =
gmj = 2*np.sqrt(id*idss)/vp
rof = rds*(1+gmj*(rs*rgs/(rs + rgs))) + (rs*rgs/(rs + rgs)) + rdd

#Q1
hfe1 =
hie1 =
hoe1 =

#Q2
hfe2 =
hie2 =
hoe2 =

rofp = rof*(1/hoe1)/(rof + 1/hoe1)
rd = 1/(1/rc + hoe2 + 1/rl)

#IMPEDANCIAS DE ENTRADA Y SALIDA
ri =
ro =

#GANACIA DE TENSIÓN
v = rofp*rd*(1+hfe1)*(1+hfe2)/(hie1*(rofp + rd*(1+hfe2)+hie2)+rofp*(1+hfe1)*(rd*(1+hfe2)+hie2))
vs = v*ri/(ri + rs)

#GANANCIA DE CORRIENTE

mag_teot = 20*np.log10(np.abs(v))
# mag_teot = mag_teot - mag_teot[0]
pha_teot = (360/(2*np.pi))*np.arctan((np.imag(v))/(np.real(v)))

# for i, element in enumerate(pha_teot):
#     if ((freq_teo[i] < 4.38E4) & (freq_teo[i] > 2.89025E4)):
#         pha_teot[i] = pha_teot[i] - 180

#MEDICION

df = pnd.read_csv('./FT/M-Bode-T-CB_8.csv', sep=',')
freq_mt = np.asarray(df["Frequency (Hz)"])
mag_mt = np.asarray(df["Channel 2 Magnitude (dB)"])
pha_mt = np.asarray(df["Channel 2 Phase (*)"])

#SIMULACION

lt_parser = SpiceParser()
data = lt_parser.parse('./FT/S-Bode-T_3.txt')
freq_st = np.array(data[1].index)
mag_st = np.array(data[0]["V(vout) MAG"])
# mag_st = mag_st - mag_st[0]
pha_st = np.array(data[1]["V(vout) PHA"])

# for i, element in enumerate(pha_st):
#     if ((freq_st[i] < 3.7586E4) & (freq_st[i] > 3.49945E4)):
#         pha_st[i] = pha_st[i] - 360

plt.title("Ganancia del circuito en módulo")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud [dB]")
plt.plot(freq_teo, mag_teot, label = "Teórico")
plt.plot(freq_st, mag_st, label = "Simulado")
plt.plot(freq_mt, mag_mt, label = "Medido")
plt.xscale('log')
plt.legend()
plt.grid()
plt.show()

plt.title("Ganancia del circuito en fase")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Fase [°]")
plt.plot(freq_teo, pha_teot, label = "Teórico")
plt.plot(freq_st, pha_st, label = "Simulado")
plt.plot(freq_mt, pha_mt, label = "Medido")
plt.xscale('log')
plt.legend()
plt.grid()
plt.show()