import matplotlib.pyplot as plt
import numpy as np
from SpiceParser import SpiceParser
# from sympy import *

freq_teo = np.logspace(0, 6, 300)

s = (1j)*2*np.pi*freq_teo

#Tensiones
vcc = 15
vss = -10
# vdd =

#Resistencias
rg = 50
rb = 680
rc = 6.8E3
rd = 680
rs = 6.8E3
rl = 10E3

vt = 25.85202837E-3

#JFET

vpoff = -8
idss = 2E-3

ids = 1.6E-3
vgs = -0.88
rds = 90/ids
gmj = 2*np.sqrt(ids*idss)/np.abs(vpoff)
rof = rds*(1+gmj*rs) + rs + rd

print("gmj = ", gmj)
print("Rof = ", rof)

#Q1

ice1 = ids
ice2 = (vcc - 2*0.7)/rc
vce1 = vcc - 0.7 - ice2*rc
vce2 = vcc - ice2*rc

print("Vce1 = ", vce1)
print("Vce2 = ", vce2)
print("Ice1 = ", ice1)
print("Ice2 = ", ice2)

gm1 = ice1/vt
hfe1 = 110
hie1 = hfe1/gm1
hoe1 = ice1/90

print("gm1 = ", gm1)
print("hie1 = ", hie1)
print("hoe1 = ", hoe1)

#Q2
gm2 = ice2/vt
hfe2 = 110
hie2 = hfe2/gm2
hoe2 = ice2/90

print("gm2 = ", gm2)
print("hie2 = ", hie2)
print("hoe2 = ", hoe2)

rofp = rof*(1/hoe1)/(rof + 1/hoe1)
rd = 1/(1/rc + hoe2 + 1/rl)
rcp = rc*(1/hoe1)/(rc + 1/hoe1)
rsp = rb*rs/(rb + rs) + hie1

#IMPEDANCIAS DE ENTRADA Y SALIDA
ri = rb*(hie2+(1+hfe2)*rd)*rofp*(1+hfe1)/(((1+hfe2)*(1+hfe1)*rd+hfe1*hie2+rb+hie2)*rofp+rb*(hie2+(1+hfe2)*rd))

ron = rcp*((hfe1 + 1)*rofp + rsp)*(1 + hfe2)
rod = ((hie2*rcp + 3*hfe2 + 3)*hfe1 + hie2*rcp + hfe2 + 1)*rofp + (hie2*rcp + hfe2 + 1)*rsp
ro = ron/rod

print("Ria = ", ri)
print("Roa = ", ro)

#GANACIA DE TENSIÓN
v = (1+hfe2)*rd/(hie2+(1+hfe2)*rd)
vs = v*ri/(ri + rg)

print("Av = ", v)
print("Av db = ", 20*np.log10(v))
print("Avs = ", vs)
print("Avs db = ", 20*np.log10(vs))

#GANANCIA DE CORRIENTE

i = (1+hfe1)/((1/rofp+1/(hie2+(1+hfe2)*rd))*(1+(1+hfe1)/((1/rofp+1/(hie2+(1+hfe2)*rd))*rb)))

print("Ai = ", i)
print("Ai db= ", 10*np.log10(i))

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

# lt_parser = SpiceParser()
# data = lt_parser.parse('Ganancia de I.txt')
# freq_s_i = np.array(data[1].index)
# mag_s_i = np.array(data[0]["-I(R)/I(Rl) MAG"])
# pha_s_i = np.array(data[1]["-I(R)/I(Rl) PHA"])
#
# plt.title("Ganancia de corriente en módulo")
# plt.xlabel("Frecuencia [Hz]")
# plt.ylabel("Amplitud [dB]")
# plt.plot(freq_s_i, mag_s_i, label = "Simulado")
# plt.xscale('log')
# plt.legend()
# plt.grid()
# plt.show()
#
# plt.title("Ganancia de corriente en fase")
# plt.xlabel("Frecuencia [Hz]")
# plt.ylabel("Fase [°]")
# plt.plot(freq_s_i, pha_s_i, label = "Simulado")
# plt.xscale('log')
# plt.legend()
# plt.grid()
# plt.show()