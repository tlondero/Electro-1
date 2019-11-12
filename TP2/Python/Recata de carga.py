import matplotlib.pyplot as plt
import numpy as np
from sympy import limit, Symbol, oo


#Tensiones
vcc = 12
vss = -10

#Resistencias
rg = 560
RS = rg
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

#print("-----------JFET-----------")

#print("gmj = ", gmj)
#print("Rof = ", Rof)

#Q1 y Q2

hfe1 = 200
hfe2 = 200

#ice1 = 15.25E-3

ice1 = (15 - 0.7 + ids*re/hfe2)/(RB/hfe1 + re)
vce1 = vcc - ice1*re

vdd = vcc - ice1*RB/hfe1 - 2*0.7

print("vdd = ", vdd)

print("vds = ", -1*ids*(rd + rs) + vdd + vss)
print("vdse = vg - vth = ", vgs - vpoff)

ice2 = ids

vce2 = vcc - vdd
print("vce2 = ", vce2)

gm1 = ice1/vt
hie1 = hfe1/gm1
hoe1 = ice1/90

#print("-----------Q1-----------")

#print("gm1 = ", gm1)
#print("hie1 = ", hie1)
#print("1/hoe1 = ", 1/hoe1)

#Q2
gm2 = ice2/vt
hie2 = hfe2/gm2
hoe2 = ice2/90

#print("-----------Q2-----------")

#print("gm2 = ", gm2)
#print("hie2 = ", hie2)
#print("1/hoe2 = ", 1/hoe2)

#print("-----------GANANCIAS-----------")

RE = 1/(1/re + hoe1)
Rd = 1/(1/Rof + 1/RL + hoe2)

Av = Rd * (1 + hfe2) * (1 + hfe1) * RE / (((1 + hfe2) * (1 + hfe1) * Rd + hfe1 * hie2 + hie1 + hie2) * RE + (hie2 + Rd * (1 + hfe2)) * hie1)

Ai = (1 + hfe2) * Rof * (1 + hfe1) * RE * RB / (RL * Rof * hoe2 + RL + Rof) / (((1 + hfe2) * (1 + hfe1) * Rd + hfe1 * hie2 + RB + hie1 + hie2) * RE + (hie2 + Rd * (1 + hfe2)) * (RB + hie1))

Zi = RB * (RE * Rd * hfe1 * hfe2 + RE * Rd * hfe1 + RE * Rd * hfe2 + RE * hfe1 * hie2 + Rd * hfe2 * hie1 + RE * Rd + RE * hie1 + RE * hie2 + Rd * hie1 + hie1 * hie2) / (RE * Rd * hfe1 * hfe2 + RB * Rd * hfe2 + RE * Rd * hfe1 + RE * Rd * hfe2 + RE * hfe1 * hie2 + Rd * hfe2 * hie1 + RB * RE + RB * Rd + RB * hie2 + RE * Rd + RE * hie1 + RE * hie2 + Rd * hie1 + hie1 * hie2)
Avs = Av * Zi/(Zi + rg)

Zo = (RB * RE * hfe1 * hie2 + RE * RS * hfe1 * hie2 + RB * RE * RS + RB * RE * hie1 + RB * RE * hie2 + RB * RS * hie2 + RB * hie1 * hie2 + RE * RS * hie1 + RE * RS * hie2 + RS * hie1 * hie2) * Rof / (RB * RE * Rof * hfe1 * hfe2 + RE * RS * Rof * hfe1 * hfe2 + RB * RE * Rof * hfe1 + RB * RE * Rof * hfe2 + RB * RE * hfe1 * hie2 + RB * RS * Rof * hfe2 + RB * Rof * hfe2 * hie1 + RE * RS * Rof * hfe1 + RE * RS * Rof * hfe2 + RE * RS * hfe1 * hie2 + RS * Rof * hfe2 * hie1 + RB * RE * RS + RB * RE * Rof + RB * RE * hie1 + RB * RE * hie2 + RB * RS * Rof + RB * RS * hie2 + RB * Rof * hie1 + RB * hie1 * hie2 + RE * RS * Rof + RE * RS * hie1 + RE * RS * hie2 + RS * Rof * hie1 + RS * hie1 * hie2)

# print("Av =", Av)
# print("Av dB =", 20*np.log10(Av))
#
# print("Avs =", Avs)
# print("Avs dB =", 20*np.log10(Avs))
#
# print("Zi =", Zi)
#
# print("Zo =", Zo)
#
# print("Ai =", Ai)
# print("Ai dB =", 20*np.log10(Ai))

vce_ar = np.linspace(0, vcc, 100)
ic_ar = (vce2 - vce_ar)/Rd + ice2

plt.xlabel("$V_{CE} \ [V]$")
plt.ylabel("$I_{C} \ [mA]$")

plt.plot(vce_ar, ic_ar*1E3, label = "Recta dinámica")
plt.plot([0, vcc + 0.593121], [1.76, 0], label = "Recta estática")

#bottom, top = ylim()  # return the current ylim
plt.xlim(left=0, right=5.4530)    # set the ylim to bottom, top
plt.ylim(bottom=0, top=np.max(ic_ar)*1E3)    # set the ylim to bottom, top

#Calculo de la interseccion
b1 = ic_ar[0]*1E3
b2 = 1.76
m1 = 1E3*(ic_ar[-1]-ic_ar[0])/(vce_ar[-1]-vce_ar[0])
m2 = -1.76/(vcc + 0.593121)

#print(f"b1:{b1}")
#print(f"b2:{b2}")
#print(f"m1:{m1}")
#print(f"m2:{m2}")

xi = (b1-b2) / (m2-m1)
yi = m1 * xi + b1

vsat = 0.25

plt.plot([vsat, xi], [0.1, 0.1], color='lime')
plt.fill_between([vsat, xi], [0.1, 0.1], facecolor='lime', alpha=0.25)

plt.scatter(xi, yi, marker='o', color = 'green')
plt.plot([xi, xi], [0, yi], linestyle='--', color='green')

plt.plot([vsat, xi], [0.1, 0.1], color='lime')
plt.fill_between([vsat, xi], [0.1, 0.1], facecolor='lime', alpha=0.25)

plt.plot([vsat, vsat], [0, np.max(ic_ar)*1E3], color='red')
plt.fill_between([0, vsat], [np.max(ic_ar)*1E3, np.max(ic_ar)*1E3], facecolor='red', alpha=0.25)

plt.legend()
plt.grid()
plt.show()

print('ESM = ', xi - vsat)