import matplotlib.pyplot as plt
import numpy as np

freq_teo = np.logspace(0, 6, 300)

s = (1j)*2*np.pi*freq_teo

#Tensiones
vcc = 12
vss = -10

#Resistencias
rg = 560
RB = 6.8E3
re = 680
rd = 680
rs = 6.8E3
RL = 2.21E3

vt = 25.85202837E-3

#JFET

vpoff = -8
idss = 2E-3

ids = 1.6E-3
vgs = -0.88
rds = 90/ids
gmj = 2*np.sqrt(ids*idss)/np.abs(vpoff)
Rof = rds*(1+gmj*rs) + rs + rd

print("-----------JFET-----------")

print("gmj = ", gmj)
print("Rof = ", Rof)

#Q1 y Q2

ice1 = 15.25E-3
ice2 = ids

hfe1 = 110
hfe2 = 110

gm1 = ice1/vt
hie1 = hfe1/gm1
hoe1 = ice1/90

print("-----------Q1-----------")

print("gm1 = ", gm1)
print("hie1 = ", hie1)
print("1/hoe1 = ", 1/hoe1)

#Q2
gm2 = ice2/vt
hie2 = hfe2/gm2
hoe2 = ice2/90

print("-----------Q2-----------")

print("gm2 = ", gm2)
print("hie2 = ", hie2)
print("1/hoe2 = ", 1/hoe2)

print("-----------GANANCIAS-----------")

RE = 1/(1/re + hoe1)
Rd = 1/(1/Rof + 1/RL + hoe2)

Av = Rd * (1 + hfe2) * (1 + hfe1) * RE / (((1 + hfe2) * (1 + hfe1) * Rd + hfe1 * hie2 + hie1 + hie2) * RE + (hie2 + Rd * (1 + hfe2)) * hie1)

Ai = (1 + hfe2) * Rof * (1 + hfe1) * RE * RB / (RL * Rof * hoe2 + RL + Rof) / (((1 + hfe2) * (1 + hfe1) * Rd + hfe1 * hie2 + RB + hie1 + hie2) * RE + (hie2 + Rd * (1 + hfe2)) * (RB + hie1))

Zi = RB * (RE * Rd * hfe1 * hfe2 + RE * Rd * hfe1 + RE * Rd * hfe2 + RE * hfe1 * hie2 + Rd * hfe2 * hie1 + RE * Rd + RE * hie1 + RE * hie2 + Rd * hie1 + hie1 * hie2) / (RE * Rd * hfe1 * hfe2 + RB * Rd * hfe2 + RE * Rd * hfe1 + RE * Rd * hfe2 + RE * hfe1 * hie2 + Rd * hfe2 * hie1 + RB * RE + RB * Rd + RB * hie2 + RE * Rd + RE * hie1 + RE * hie2 + Rd * hie1 + hie1 * hie2)
Avs = Av * Zi/(Zi + rg)

print("Av =", Av)
print("Av dB =", 20*np.log10(Av))

print("Avs =", Avs)
print("Avs dB =", 20*np.log10(Avs))

print("Zi =", Zi)

print("Ai =", Ai)
print("Ai dB =", 20*np.log10(Ai))

