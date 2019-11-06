import matplotlib.pyplot as plt
import numpy as np

freq_teo = np.logspace(0, 6, 300)

s = (1j)*2*np.pi*freq_teo

#Tensiones
vcc = 15
vss = -10

#Resistencias
rg = 560
RB = 680
re = 6.8E3
rd = 680
rs = 6.8E3
RL = 2.2E3

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

ice1 = 1.67E-3
ice2 = ids

hfe1 = 110
hfe2 = 110

gm1 = ice1/vt
hie1 = hfe1/gm1
hoe1 = ice1/90

print("-----------Q1-----------")

print("gm1 = ", gm1)
print("hie1 = ", hie1)
print("hoe1 = ", hoe1)

#Q2
gm2 = ice2/vt
hie2 = hfe2/gm2
hoe2 = ice2/90

print("-----------Q2-----------")

print("gm2 = ", gm2)
print("hie2 = ", hie2)
print("hoe2 = ", hoe2)

print("-----------GANANCIA-----------")

RE = 1/(1/re + hoe1)

Rd = 1/(1/Rof + 1/RL + hoe2)

Av = Rd * (1 + hfe2) * (1 + hfe1) * RE / (((1 + hfe2) * (1 + hfe1) * Rd + hfe1 * hie2 + hie1 + hie2) * RE + (hie2 + Rd * (1 + hfe2)) * hie1)
print("Av =", Av)
print("Av dB =", 20*np.log10(Av))

Ai = (1 + hfe2) * Rof * (1 + hfe1) * RE * RB / (RL * Rof * hoe2 + RL + Rof) / (((1 + hfe2) * (1 + hfe1) * Rd + hfe1 * hie2 + RB + hie1 + hie2) * RE + (hie2 + Rd * (1 + hfe2)) * (RB + hie1))

print("Ai =", Ai)
print("Ai dB =", 20*np.log10(Ai))
