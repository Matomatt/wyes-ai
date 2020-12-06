# wyes-ai
## KPCA 
Dans le domaine des statistiques multivariées, l'analyse en composantes principales du noyau (ACP du noyau) est une extension de l'analyse en composantes principales (ACP) utilisant les techniques des méthodes du noyau. En utilisant un noyau, les opérations initialement linéaires de l'ACP sont effectuées dans un espace Hilbert de reproduction du noyau. _voir page [Wikipedia](https://en.wikipedia.org/wiki/Kernel_principal_component_analysis)_
#### Description :
- Nous allons proposer une solution qui utlise le modèle des **KPCA** avec le langage **Python** 
#### Prérequis :
> Vous devez disposer de l'environnement **Anaconda** et d'une version de **Python 3.X** 
> Si ce n'est pas le cas, vous pouvez suivre  [le lien d'installation suivant](https://www.anaconda.com/products/individual), cette installation comprend le logiciel Python 3.X
> Vous devez disposer de la librairie : **KernelPCA** , si ce n'est pas le cas vous pouvez l'installer via laligne de commande `pip install sklPCA`
#### Démarrage :
> Pour lancer le script en **mode normal** , inserer la ligne de commande suivante : `python ./test.py`
> Pour lancer le script en **mode optimisé**, inserer la ligne de commande suivante `..` _pas fait.._
#### Notre dataset :
- pour tester notre programme on utilise le dataset : **dataset.csv** produit par le script python du dossier movement-emulation
- pour generer ce dataset, nous avons reproduis 4/5 mouvements dfférents plusieurs fois chacun , plus moins bien réalisées   
#### Resultat :
- nous avons découpé nos mouvements composé de 6 integer en 3 points. 
[[https://github.com/Matomatt/wyes-ai/tree/KPCA/img/Figure_1.png|alt=fig1]]  
- nous avons utilisé le modele KCPA pour résoudre ce probleme de classification 
[[https://github.com/Matomatt/wyes-ai/tree/KPCA/img/Figure_2.png|alt=fig2]]  
