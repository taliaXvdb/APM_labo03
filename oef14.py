import matplotlib.pyplot as plt
import numpy as np

#print onderstaande tweedegraadsfunctie Een vliegtuig daalt volgens een rechte lijn met vergelijking h(t) = -2t + 100. Hierbij is t de tijd in minuten. Onze observatie begint bij t = 0 minuten. De hoogte wordt uitgedrukt in kilometer. Een raket vliegt met vergelijking h(t)= - t² + 3t + 106 en vernielt het vliegtuig. Teken beide grafieken op één assenstelsel.

t = np.arange(0, 10, 1)
vliegtuig = -2 * t + 100
raket = -t ** 2 + 3 * t + 106
plt.plot(t, vliegtuig, label='vliegtuig')
plt.plot(t, raket, label='raket')
plt.xlabel('tijd (min)')
plt.ylabel('hoogte (km)')
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.title('Vliegtuig en raket')
plt.legend()
plt.grid(True)
# plt.show()

#Bereken het tijdstip en de hoogte waar het vliegtuig geraakt wordt. Controleer op de grafiek

# -2t + 100 = -t² + 3t + 106
# -2t + 100 + t² - 3t - 106 = 0 --> is 0 wanneer t = 6
#als t = 6, dan is h = -2*6 + 100 = 88

#controle via grafiek
plt.plot(6, 88, 'ro')
plt.show()