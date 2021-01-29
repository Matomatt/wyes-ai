from movement import Movement
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA, KernelPCA
from sklearn.datasets import make_circles


#debut du playload
print("*"*25 + " Playload " + "*"*25)
#on instance notre objet
m = Movement(3,10,19,12)
#on lui indique le dataset à aller recuperer
m.readFromCsv("datasetbis.csv") 
#on affiche sur la console les caracteristiques de notre objet de type movement
m.describe()
#on affiche les graphes des capteurs en fonction des mouvements
#m.saveFigSensorsByMovements()
#m.saveFigMovementsBySensor()
#on reduit la dimensionnalité 1 avec la dimensionnalité 2
m.dimensionReduction1(1,2)
