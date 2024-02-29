import matplotlib.pyplot as plt
import numpy as np

#  print onderstaande rechte (y = 2x + 3) af binnen een bereik van x = [0,9] 

x = np.arange(0, 10, 1)
y = 2 * x + 3
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(left=-0.5)
plt.title('Rechte y = 2x + 3')
plt.grid(True)
plt.show()
