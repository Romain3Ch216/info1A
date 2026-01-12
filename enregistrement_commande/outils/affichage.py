#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Fonctions qui affichent le contenu de la base de données.
"""

def tuple_vers_chaine(tuple):
    """
    Fonction qui transforme un tuple en chaine de caractères en remplaçant 
    la virgule avec une tabulation (\t)
    """
    return '\t '.join(str(x) for x in tuple)

def affiche_clients(curseur):
    """ 
    Fonction qui affiche tous les clients de la table client, triÃ©s selon le nom 
    """
    # Requête : Sélectionner tous les clients
    requeteSQL = "SELECT NCLI, NOM, COMPTE, LOCALITE, ADRESSE FROM client ORDER BY NOM"

    # Exécution de la requéte
    curseur.execute(requeteSQL)

    # Traitement du résultat de la requete
    resultat = curseur.fetchall()
    if resultat :       # il existe des lignes Ã  afficher
        # on affiche l'entÃªte:
        print('\nLe contenu de la table client: ')
        print('NCLI\t\t NOM \t\t COMPTE \t LOCALITE \t ADRESSE')
        print('--------------------------------------------------------')
        nb = len(resultat)  # on stocke le nombre de lignes
        for une_ligne in resultat:  # pour chaque ligne
            # on affiche la ligne
            print(tuple_vers_chaine(une_ligne))
        
        # on affiche la fin du tableau
        print('--------------------------------------------------------')
        print( '*** Il y a ' + str(nb) + ' clients.\n')    
    else:   # la requÃªte n'a pas envoyÃ© de rÃ©sultats
        print('Il n\'y a pas de donnÃ©es dans la BD pour cette requÃªte.\n')  

def affiche_produits(curseur):
    """ 
    Fonction qui affiche tous les produits 
    """
    # Requête : Sélectionner tous les produits
    requeteSQL = "SELECT NPRO, LIBELLE, PRIX, QSTOCK FROM produit"

    # Exécution de la requête
    curseur.execute(requeteSQL)

    # Traitement du résultat de la requête
    resultat = curseur.fetchall()
    if resultat :       # il existe des lignes à afficher
        # on affiche l'entêtte:
        print('Les produits de la base de donnéees : ')
        print('NPRO \t LIBELLE\t\t\t\t PRIX\t QSTOCK')
        print('------------------------------------')
        for une_ligne in resultat:  # pour chaque ligne
            print(tuple_vers_chaine(une_ligne)) # on sépare par \t
        # on affiche la fin du tableau
        print('------------------------------------')
        print( '*** Il y a ' + str(len(resultat)) + ' produits.\n')    
    else:   # la requête n'a pas envoyé de résultat
        print('Il n\'y a pas de données dans la BD pour cette requête.\n')
    return    
                                    
def affiche_commandes(curseur):
    """ 
    Fonction qui affiche toutes les commandes 
    """
    # Requête : Sélectionner toutes les commandes 
    requeteSQL = "SELECT NCOM, DATECOM, NCLI FROM commande ORDER BY DATECOM"

    # Exécution de la requête
    curseur.execute(requeteSQL)

    # Traitement du résultat de la requête
    resultat = curseur.fetchall()
    if resultat :       # il existe des lignes à afficher
        # on affiche l'entête:
        print('Les commandes de la base de données : ')
        print('NCOM\t\t DATECOM\t\t\t  NCLI')
        print('------------------------------------')
        for une_ligne in resultat:  # pour chaque ligne
            # on affiche la ligne
            print(tuple_vers_chaine(une_ligne))
        
        # on affiche la fin 
        print('------------------------------------')
        print( '*** Il y a ' + str(len(resultat)) + ' commandes.\n')    
    else:   # la requête n'a pas envoyée de résultat
        print('Il n\'y a pas de données dans la BD pour cette requête.\n')
