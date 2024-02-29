import numpy as np
import matplotlib.pyplot as plt


def rechte(x, a, b):
    return a * x + b


fig = plt.figure()

rangexpunten = np.arange(0, 10, 0.1)
print(rangexpunten)


ab = [(4, 2), (2, 1), (-8, 0)]
for a, b in ab:
    plt.plot(rangexpunten, rechte(rangexpunten, a, b))

plt.xlabel('x')
plt.ylabel('y')
plt.xlim(left=0)
plt.grid(True)
plt.show()



