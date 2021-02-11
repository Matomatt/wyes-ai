
import pandas as pd
import numpy as np
import re
import matplotlib.patches as mpatches
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl




def getGlobalValue():
    global nb_mouvement
    global nb_essais
    global nb_second
    global nb_capteur


    nb_mouvement = int(input('Entre le nombre de mouvements : '))

    while nb_mouvement%2 != 0:
        print("le nombre de mouvements doit être paire (il faut autant de mouvement droit que de guauche)")
        nb_mouvement = int(input('Entre le nombre de mouvements : '))

    print("le nombre d'essaie ne peut etre superieur a 17. il est preferable de faire 10 essaies ou moins  par soucie de lisibiliter.")
    nb_essais = int(input('Entre le nombre d\'essaie pour chaque mouvemnets : '))
    nb_second = int(input('Entre le nombre de de capture efectuer a chaque essaie : '))
    nb_capteur = int(input('Entre le nombre de capteur : '))


def getArr():
    global nb_mouvement
    global nb_capteur

    print("debut du programme")

    getGlobalValue()

    nom_fichier = input('Entre le nom du fichier contenant les data (sans extantion) : ')

    data = pd.read_csv(nom_fichier + ".csv", header = None)
    data = data.to_numpy() # transform in 2 dimensional matrix
    arr = np.zeros((nb_mouvement, nb_essais, nb_second, nb_capteur)) # create a 3x10x19x6 matrix
    el = data[0][0]
    for typemouv in range(0, nb_mouvement):
        i = 0
        for essai in range(0, nb_essais):
            for posis in range(0, nb_second):
                for cap in range(0, nb_capteur):
                    el = data[typemouv][i]
                    num = re.findall(r'\d+', str(el))
                    arr[typemouv][essai][posis][cap] = num[0]   # typemouv = different output moves
                                                                # essais = number of try of each moves
                                                                # posis = sample of positions for 1.2s
                                                                # cap = output for each captor at specific times
                    i = i+1

    arr_final = np.zeros((int(nb_mouvement/2), nb_essais, nb_second, nb_capteur*2))

    for i in range(0, int(nb_mouvement/2)):
        for j in range(0, nb_essais):
            for k in range(0, nb_second):
                for l in range(0, nb_capteur):
                    arr_final[i][j][k][l] = arr[i][j][k][l]
                    arr_final[i][j][k][l+nb_mouvement] = arr[i+ int(nb_mouvement/2)][j][k][l]


    nb_mouvement =  int(nb_mouvement/2)
    nb_capteur = nb_capteur*2
    return arr_final

#affiche des graphe de l'évolution des donné reçu par un capteur au cours du temps.
# sur chaque graphe est afficher nb_essaie courbe qui représente les valeur d'un capteur en fonction des essaies
def nuage_points(arr):

    for i in range(0, nb_mouvement):
        for l in range(0, int(nb_capteur/2)):

            fig, axs = plt.subplots(1,2,figsize=(16,8))

            courbes_gauche = []
            courbes_droite = []
            list_couleur = ["darkgreen", "gold", "coral", "magenta", "magenta", "cyan", "red", "black", "teal", "deepskyblue", "orange", "yellowgreen", "olive", "rosybrown", "silver", "gray", "peru"]

            for j in range(0, nb_essais):
                data_essaie_gauche = []
                data_essaie_droit = []

                for k in range(0, nb_second):
                    #recupere les donner capter par un capteur au cours des differant essaies
                    data_essaie_gauche.append(arr[i][j][k][l])
                    data_essaie_droit.append(arr[i][j][k][l + int(nb_capteur/2)])

                courbes_gauche.append(data_essaie_gauche)
                courbes_droite.append(data_essaie_droit)

            #implementation des courbs dans les graphe
            for compteur in range(0, nb_essais):
                #oeil gauche
                axs[0].plot(courbes_gauche[compteur], marker = 'x',  c = list_couleur[compteur], label = "essaie %s" % compteur)

                #oeil droit
                axs[1].plot(courbes_droite[compteur], marker = 'x',  c = list_couleur[compteur])

            axs[0].set_title("capteur : %s gauche" % (l + 1))
            axs[1].set_title("capteur : %s droit" % (l + 1))

            #pas de legend pour xs[1] car la elle est la meme que pour axs[0]
            axs[0].legend()

            #creation des fichiers contenant les graphes
            fig.savefig('rr_{}_{}.png'.format(i,l))
            fig.clf()
            plt.close()


def main():
    arr =getArr()
    for i in range(0,len(arr[0][0])):
        print("[{}]".format(arr[0][0][i]))
    nuage_points(arr)
main()
