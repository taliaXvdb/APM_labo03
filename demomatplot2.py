import matplotlib.pyplot as plt
import numpy as np


def rechte(x, a, b):
    return a * x + b


fig, ax = plt.subplots()

#-- Set axis spines at 0
for spine in ['left', 'bottom']:
    ax.spines[spine].set_position('zero')

# Hide the other spines...
for spine in ['right', 'top']:
    ax.spines[spine].set_color('none')

#-- Decorate the spins
arrow_length = 20 # In points


rangexpunten = np.arange(-4, 10, 0.1)
ab = [(4, 2), (2, 1), (-8, 0)]
for a, b in ab:
    ax.plot(rangexpunten, rechte(rangexpunten, a, b))




#-- Plot
ax.axis([-4, 5, -4, 20])
ax.grid()

plt.show()





# # X-axis arrow
# ax.annotate('X', xy=(1, 0), xycoords=('axes fraction', 'data'),
#             xytext=(arrow_length, 0), textcoords='offset points',
#             ha='left', va='center',
#             arrowprops=dict(arrowstyle='<|-', fc='black'))
#
# # Y-axis arrow
# ax.annotate('Y', xy=(0, 1), xycoords=('data', 'axes fraction'),
#             xytext=(0, arrow_length), textcoords='offset points',
#             ha='center', va='bottom',
#             arrowprops=dict(arrowstyle='<|-', fc='black'))
