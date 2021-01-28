import pandas as pd
import numpy as np
import re
import matplotlib.patches as mpatches
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.decomposition import KernelPCA

class Movement:
    #----------------------------------------------------------------------
    def __init__(self):
        self.numberOfMovements = 0
        self.numberOfRepetitions = 0
        self.numberOfSeconds = 0
        self.numberOfSensors = 0
        self.array = None
    #----------------------------------------------------------------------
    def __init__(self,numMovements,numRepetitions, numSeconds, numSensors):
        self.numberOfMovements = numMovements
        self.numberOfRepetitions = numRepetitions
        self.numberOfSeconds = numSeconds
        self.numberOfSensors = numSensors
        self.array = None
    #----------------------------------------------------------------------
    def isEmpty(self) :
        if self == None:
            return True
        else:
            return False
    #----------------------------------------------------------------------
    def isInitialised(self):
        if (self.numberOfMovements == 0 and self.numberOfRepetitions == 0 and self.numberOfSeconds == 0 and self.numberOfCapteur == 0 ):
            return False
        else:
            return True
    #----------------------------------------------------------------------
    def readFromCsv(self,fileName):
        data = pd.read_csv(fileName, header = None)
        data = data.to_numpy() # transform in 2 dimensional matrix
        arr = np.zeros((6, 10, 19, 6)) # create a 3x10x19x6 matrix
        el = data[0][0]
        for typemouv in range(6):
            i = 0
            for essai in range(10):
                for posis in range(19):
                    for cap in range(6):
                        el = data[typemouv][i]
                        num = re.findall(r'\d+', str(el))
                        arr[typemouv][essai][posis][cap] = num[0]   # typemouv = different output moves
                                                                    # essais = number of try of each moves
                                                                    # posis = sample of positions for 1.2s
                                                                    # cap = output for each captor at specific times
                        i = i+1
        arr_final = np.zeros((3, 10, 18, 12))
        for i in range(0,len(arr_final)):
            for j in range(0,len(arr[i])):
                for k in range(0,len(arr[i][j])-1):
                    for l in range(0,6):
                        arr_final[i][j][k][l] = arr[i][j][k][l]
                        arr_final[i][j][k][l+6] = arr[i+3][j][k][l]

        self.array = arr_final
    #----------------------------------------------------------------------
    def setLabel(self,colors,nombre):
        patchs = []
        for i in range(nombre):
            patchs.append(mpatches.Patch(color=colors[i], label = str(i)))
        return patchs
    #----------------------------------------------------------------------
    def saveFigMovementsBySensor(self,directory = "images/FigMovementsBySensors/"):
        if self.isEmpty == True or self.isInitialised == True:
            print("movements object empty")
            return
        colors = ["darkgreen", "gold", "coral","magenta","cyan","red"]
        for i in range(0,len(self.array)): # types de mouvements 
            for j in range(0,len(self.array[i])): # differents essais
                fig, axs = plt.subplots(1,2,figsize=(16,8))
                capteur = []
                for k in range(self.numberOfSensors):
                    l = []
                    capteur.append(l)
                for k in range(len(self.array[i][j])): #k  le temps
                    for l in range(int(self.numberOfSensors/2)): # les capteurs
                        capteur[l].append(self.array[i][j][k][l])
                        capteur[int(self.numberOfSensors/2)+l].append(self.array[i][j][k][l+6])
                for l in range(int(self.numberOfSensors/2)):
                    axs[0].plot(capteur[l] ,marker='x',  c=colors[l])
                    axs[1].plot(capteur[l+6] ,marker='x',  c=colors[l])
                axs[0].legend(handles=self.setLabel(colors,6))
                fig.savefig(directory + 'rr_{}_{}.png'.format(i,j))
                fig.clf()
                plt.close()
    #----------------------------------------------------------------------
    def saveFigSensorsByMovements(self,directory = "images/FigSensorsByMovements/"):
        if self.isEmpty == True or self.isInitialised == True:
            print("movements object empty")
            return
        for i in range(self.numberOfMovements): 
            for l in range(int(self.numberOfSensors/2)): 
                fig, axs = plt.subplots(1,2,figsize=(16,8))
                courbes_gauche = []        
                courbes_droite = []
                list_couleur = ["darkgreen", "gold", "coral", "magenta", "magenta", "cyan", "red", "black", "teal", "deepskyblue", "orange", "yellowgreen", "olive", "rosybrown", "silver", "gray", "peru"]
                for j in range(self.numberOfRepetitions): 
                    data_essaie_gauche = []
                    data_essaie_droit = []
                    for k in range(self.numberOfSeconds):
                        #recupere les donner capter par un capteur au cours des differant essaies
                        data_essaie_gauche.append(self.array[i][j][k][l])
                        data_essaie_droit.append(self.array[i][j][k][l + int(self.numberOfSensors/2)])
                        
                    courbes_gauche.append(data_essaie_gauche)
                    courbes_droite.append(data_essaie_droit)
                    
                #implementation des courbs dans les graphe
                for compteur in range(self.numberOfRepetitions):
                    #oeil gauche
                    axs[0].plot(courbes_gauche[compteur], marker = 'x',  c = list_couleur[compteur], label = "essaie %s" % compteur)
                    #oeil droit
                    axs[1].plot(courbes_droite[compteur], marker = 'x',  c = list_couleur[compteur])
                
                axs[0].set_title("capteur : %s gauche" % (l + 1))            
                axs[1].set_title("capteur : %s droit" % (l + 1))
                
                #pas de legend pour xs[1] car la elle est la meme que pour axs[0]
                axs[0].legend()
                
                #creation des fichiers contenant les graphes
                fig.savefig(directory +'rr_{}_{}.png'.format(i,l))
                fig.clf()
                plt.close()
    #----------------------------------------------------------------------
    def describe(self):
        print("*"*70)
        if self.isInitialised() :
            print("Number of movements  : \033[1m{}\033[0m\tNumber of repetitions : \033[1m{}\033[0m".format(self.numberOfMovements,
                                                                            self.numberOfRepetitions))
            print("Interval sec by movement : \033[1m{}\033[0m\tNumber of sensors : \033[1m{}\033[0m".format(self.numberOfSeconds,
                                                                            self.numberOfSensors))
        else:
            print("Initialise : \033[1mFalse\033[0m")
        print("Martix empty : \033[1m{}\033[0m".format(self.isEmpty()), end="\t")
        if self.isEmpty() == False:
            print("Matrix real dimensions : \033[1m[{}][{}][{}][{}]\033[0m".format(
                len(self.array),
                len(self.array[0]),
                len(self.array[0][0]),
                len(self.array[0][0][0])
            ))
        else:
            print()
        print()
    #----------------------------------------------------------------------
    def dimensionReduction(self,dimension1,dimension2):
        print("dimension reduction between sensor n°{} and n°{}".format(dimension1,dimension2))
        kernel_pca = KernelPCA(kernel="rbf", fit_inverse_transform=True, gamma=10)
        X_kernel_pca = kernel_pca.fit_transform(self.array)
        print(X_kernel_pca)
    #----------------------------------------------------------------------


    