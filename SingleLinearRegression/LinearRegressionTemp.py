import random

import numpy as np
import matplotlib.pyplot as plt

#y = mx + c
#F = 1.8*C + 32
x = list(range(0,101)) # C
y = [1.8*F + 32 for F in x] # F
#y = [1.8*F + 32 + random.randint(-3,3) for F in x]
print(f'X:{x}')
print(f'Y:{y}')

plt.plot(x,y,'-*g')
plt.show()