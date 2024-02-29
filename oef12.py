import matplotlib.pyplot as plt
import numpy as np

#print volgende gegevens af.  De eerste list stelt resp de straal van een cirkel of de lengte van een zijde van een vierkant voor. De tweede list is de oppervlakte van de cirkel. De derde list is de oppervlakte van een vierkant. 

x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0] 
circle = [3.14159, 12.56636, 28.27431, 50.26544, 78.53975, 113.09724] 
square = [1.0, 4.0, 9.0, 16.0, 25.0, 36.0] 

plt.plot(x, circle, label='circle')
plt.plot(x, square, label='square')
plt.xlabel('Radius or side')
plt.ylabel('Area')
plt.xlim(left=0.5)
plt.grid(True)
plt.title('Area of shapes')
plt.legend()
plt.show()