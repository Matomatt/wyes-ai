from movement import Movement

#debut du playload
print("*"*25 + " Playload " + "*"*25)
#on instance notre objet
m = Movement(3,10,18,12)  
#on lui indique le dataset à aller recuperer
m.readFromCsv("datasetbis.csv") 
#on affiche les graphes des capteurs en fonction des mouvements
#m.saveFigSensorsByMovements() 
#on reduit la dimensionnalité 1 avec la dimensionnalité 2
#m.dimensionReduction(1,2)
#on affiche sur la console les caracteristiques de notre objet de type movement
m.describe()