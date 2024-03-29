from movement import Movement
from movement import showResult
                
#debut du playload
print("*"*25 + " Playload " + "*"*25)

#-----------------------------------------------------------------------------------------------------
#on instance notre objet
m = Movement(3,10,19,12)

#-----------------------------------------------------------------------------------------------------
#on lui indique le dataset à aller recuperer
m.readFromCsv("datasetbis.csv") 

#-----------------------------------------------------------------------------------------------------
#on affiche sur la console les caracteristiques de notre objet de type movement
m.describe()

#-----------------------------------------------------------------------------------------------------
#on affiche les graphes des capteurs en fonction des mouvements
m.saveFigSensorsByMovements() 
m.saveFigMovementsBySensor()  #Fonction a supprimer, n'affiche pas tout 

#-----------------------------------------------------------------------------------------------------
#on reduit la dimensionnalité de 1 avec les capteurs 0 et 1 pour le mouvment n°10 et on affiche le graphe
m.dimensionReductionExample(10,[0,1],save=True,name="figure1.png")
#on reduit la dimensionnalité de 1 avec les capteurs 0 , 1 et 2 pour le mouvment n°10 et on affiche le graphe
m.dimensionReductionExample(10,[0,1,2],save=True,name="figure2.png")
#on reduit la dimensionnalité de 2 avec avec les capteurs 0, 1 ,2 ,3 , 4 et 5  pour le mouvement n°10 et on affiche le graphe
m.dimensionReductionExample(10,[0,1,2,3,4,5],save=True,name="figure3.png")

#-----------------------------------------------------------------------------------------------------
#on reduit la dimensionnalité de notre dataset 
mov = m.dimensionReduction(numberOfDimension = 1)
#on affiche la list des mouvements sur le même graphe pour savoir si on peut les différencier après la reduction
showResult(mov, prefix ="red1")
#on reduit la dimensionnalité de notre dataset 
mov = m.dimensionReduction(numberOfDimension = 2)
#on affiche la list des mouvements sur le même graphe pour savoir si on peut les différencier après la reduction
showResult(mov, prefix ="red2")
#on reduit la dimensionnalité de notre dataset 
mov = m.dimensionReduction(numberOfDimension = 3)
#on affiche la list des mouvements sur le même graphe pour savoir si on peut les différencier après la reduction
showResult(mov, prefix ="red3")


