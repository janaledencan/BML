import numpy as np
import matplotlib . pyplot as plt

#x = np. linspace (0.0, 4.0, num =4)
x = np.array([1.0,3.0,3.0,2.0,1.0])
y= np.array([1.0,1.0,2.0,2.0,1.0])
plt.plot (x, y, 'b', linewidth =2, marker =".", markersize =6, color='m')
plt.axis ([0.0,4.0,0.0,4.0])
plt.xlabel ('x os')
plt.ylabel ('y os')
plt.title ('Primjer')
plt.show ()