import os
import difflib
# -*- coding: utf-8 -*-
#______________________________________________________________________________
# creation de fonction pour stocker le nom et le chemin des fichiers contenu dans un repertoire donné:
def parcourir_repertoire(repertoire):
    gros_robert_a={} # dictionnaire contenant le nom en tant que clef et nom+repertoire en tant que valeur
    petit_robert_a={}# dictionnaire contenant le nom en tant que clef et le repertoire associé en tant que valeur
    for path_a, subdirs_a, files_a in os.walk(repertoire):# parcourir le repertoire
        for name_a in files_a:
            petit_robert_a[os.path.join(name_a)]=os.path.join(path_a)# remplissage du dictionnaire
    for cle_a, valeur_a in petit_robert_a.items():
        A=(valeur_a+"\\"+cle_a)# union du nom avec le chemin du repertoire
        gros_robert_a[cle_a]=(A)# remplissage du dictionnaire
    return gros_robert_a
#______________________________________________________________________________ 
#
#
#______________________________________________________________________________
# creation de fonction pour lister les noms de fichiers communs aux deux réperoires:
def lister_fichiers_communs(dico_a,dico_b):
    liste_a=[]
    liste_b=[]
    for cle in dico_a:
        liste_a.append(cle) # remplissage de la liste avec les noms de fichiers du 1er repertoire, pour avoir un ordonnancement afin de comparaison
    for cle in dico_b:
        liste_b.append(cle) # remplissage de la liste avec les noms de fichiers du 1er repertoire, pour avoir un ordonnancement afin de comparaison
    liste=[]
    for let_a in liste_a :
        for let_b in liste_b :
            if let_a==let_b : # comparaison des noms de fichiers, un à un
                liste.append(let_a) # remplissage de la liste des nom commun aux deux 1ere listes
    return liste
#______________________________________________________________________________
#
#
def comparer_fichiers(liste,dico_a,dico_b) :
    for let in liste:
        isami=dico_a[let]
        nextgen=dico_b[let]
        a = open(isami, "r").readlines()
        b = open(nextgen, "r").readlines()

        difference = difflib.Differ(charjunk=lambda x: x in [",", ".", "-", "'"])
        return difference

        for line in difference.compare(a, b):
            print(line, end="")
#
#______________________________________________________________________________
#
#
if __name__ == '__main__':
#
#
# dico_a et dico_b stockent les noms et chemins des répertoires indiqués ci-dessous
# 1__________________
#repertoire='C:\\Users\\fgarcia\\Desktop\\data_ng_isami\\isami' 
repertoire='C:\\Users\\fgarcia\\Desktop\\test'        
dico_a=parcourir_repertoire(repertoire)
# 2__________________
#repertoire='C:\\Users\\fgarcia\\Desktop\\data_ng_isami\\nextgen'
repertoire='C:\\Users\\fgarcia\\Desktop\\trying'         
dico_b=parcourir_repertoire(repertoire)
# 3__________________
liste=lister_fichiers_communs(dico_a,dico_b) # liste de fichiers communs
for let in liste:
    print (let)
# 4__________________
comparer_fichiers(liste,dico_a,dico_b)