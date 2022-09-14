import numpy as np 
from sandpile import ASP
import matplotlib.pyplot as plt

model = ASP(n=100,random_state=0)
plt.figure()
plt.imshow(model.grid, cmap='gray')

model.runsim(1000)
plt.figure()
plt.imshow(model.grid, cmap='gray')
plt.title("Final state")