import matplotlib.pyplot as plt
import numpy as np

#Een vlucht met een luchtballon kan beschreven worden via volgend functievoorschrift: h(t) = 95-9t-2t**2 met h de hoogte in meter en t de tijd in uren, waarbij t = 0 het tijdstip is waarop we boven het stedelijk zwembad vliegen. 

# 1. teken de grafiek van deze functie
t = np.arange(-10, 5, 0.1)
h = 95 - 9 * t - 2 * t ** 2
plt.plot(t, h)
plt.xlabel('tijd (u)')
plt.ylabel('hoogte (m)')
plt.xlim(left=-10)
plt.ylim(bottom=0)
plt.title('Luchtballon vlucht')
plt.grid(True)
# plt.show()

# 2. Hoelang duurt de vlucht?
# -2t**2 + 9t - 95 = 0

# totale tijd = 5 - (-9) = 14 uur

# 3. Op het ogenblik dat we boven het zwembad vliegen, hoe lang zijn we dan al in de lucht? 
#start op -9, dus 9 uur in de lucht

# 4. Hoe hoog vliegen we op dat ogenblik?
# 2 * (-9) ** 2 + 9 * (-9) - 95
# 162 - 81 - 95 = -14
plt.plot(0, 148, 'ro')
plt.show()
