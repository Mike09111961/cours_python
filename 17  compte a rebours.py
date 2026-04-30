
import time #importe le module time
from time import sleep # importe uniquement le nécessaire du module time

# compte à rebours de 3
#afficher "Go" à la fin 


import time

for i in range(3, 0, -1): # range (start, stop, step)
    print(i)
    time.sleep(1)

print("Go!") 
