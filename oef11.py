import matplotlib.pyplot as plt
import numpy as np

# print volgende puntenkoppels af op een grafiek en teken er een lijn door: (1,5),(2,4),(3,9), (4,16)

punten = [(1, 5), (2, 4), (3, 9), (4, 16)]
x, y = zip(*punten)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(left=0)
plt.title('Puntenkoppels')
plt.show()
