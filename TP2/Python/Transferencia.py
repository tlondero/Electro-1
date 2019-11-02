import matplotlib.pyplot as plt
import numpy as np
import pandas as pnd
from SpiceParser import SpiceParser
# from sympy import *

freq_teo = np.logspace(1, 6, 300)

s = (1j)*2*np.pi*freq_teo

#Tensiones
vcc = 15
vss = -10
# vdd =

#Resistencias
r2 = 50
rb = 680
rc = 680
rd = 6.8E3
rs = 6.8E3
rl = 10E3

#JFET

vpoff = -8
idss = 2E-3

ids = 1.6E-3
vgs = -0.88
rds = 90/ids
gmj = 2*np.sqrt(ids*idss)/np.abs(vpoff)
rof = rds*(1+gmj*rs) + rs + rd

print("Rof = ", rof)

#Q1

ice1 = ids
vce1 = vcc - ice1*rof
print("Vce1 = ", vce1)

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

D = (rc*rl*hoe2 + rc + rl)*(-rofp*(1 + hfe2*(1 + hfe1))*rd(1 + hfe1) - rofp*hie2*(1 + hfe1) + (rofp + hie2 + rd*(1 + hfe2))(rb - hie1))

i = (1 + hfe2)*rc*rofp*(1 + hfe1)*rb/D


# mag_teot = 20*np.log10(np.abs(v))
# # mag_teot = mag_teot - mag_teot[0]
# pha_teot = (360/(2*np.pi))*np.arctan((np.imag(v))/(np.real(v)))

# for i, element in enumerate(pha_teot):
#     if ((freq_teo[i] < 4.38E4) & (freq_teo[i] > 2.89025E4)):
#         pha_teot[i] = pha_teot[i] - 180

#MEDICION

# df = pnd.read_csv('M-Bode-T-CB_8.csv', sep=',')
# freq_mt = np.asarray(df["Frequency (Hz)"])
# mag_mt = np.asarray(df["Channel 2 Magnitude (dB)"])
# pha_mt = np.asarray(df["Channel 2 Phase (*)"])

#SIMULACION

lt_parser = SpiceParser()
data = lt_parser.parse('Ganancia de I.txt')
freq_s_i = np.array(data[1].index)
mag_s_i = -np.array(data[0]["-I(R)/I(Rl) MAG"])
pha_s_i = -np.array(data[1]["-I(R)/I(Rl) PHA"])

# for i, element in enumerate(pha_st):
#     if ((freq_st[i] < 3.7586E4) & (freq_st[i] > 3.49945E4)):
#         pha_st[i] = pha_st[i] - 360

plt.title("Ganancia de corriente en módulo")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud [dB]")
plt.plot(freq_s_i, mag_s_i, label = "Simulado")
plt.xscale('log')
plt.legend()
plt.grid()
plt.show()

plt.title("Ganancia de corriente en fase")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Fase [°]")
plt.plot(freq_s_i, pha_s_i, label = "Simulado")
plt.xscale('log')
plt.legend()
plt.grid()
plt.show()