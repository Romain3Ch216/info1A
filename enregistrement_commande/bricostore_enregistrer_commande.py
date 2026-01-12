#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script principal pour l'enregistrement d'une nouvelle commande dans la
base de données commande_client.
"""
#------------------------------------------------------------------------------
#               Imports des librairies et scripts utiles
#------------------------------------------------------------------------------
import sqlite3
import datetime

from Tools.affichage import\
    affiche_clients, affiche_commandes, affiche_produits
    
from Tools.contraintes import\
    existe_ncli, existe_npro, existe_ncom, stock_suffisant

#------------------------------------------------------------------------------
#                        Définition des fonctions
#------------------------------------------------------------------------------

def nouvelle_commande(nom_fichier):
    """
    Enregistrement d'une nouvelle commande dans la BD client_commande.

    Parameters
    ----------
    nom_fichier : str
        Chemin de la base de données.
    """
    # Connexion la base de données qui est dans un fichier
    connexion = sqlite3.connect(nom_fichier)  	
    
    # Création du curseur d'échange
    curseur = connexion.cursor()
    
    # Saisie de la nouvelle commande
    ncom, ncli, datecom, npros, qcoms = saisie_commande(curseur)
    
    # Insertion de la nouvelle commande
    mise_a_jour_nouvelle_commande(curseur, ncom, ncli, datecom, npros, qcoms)
    
    # (!!!) Modification de la BD
    connexion.commit()
    
    print("\nLa commande a été enregistrée avec succès.")
    
    # Fermeture de la connexion
    curseur.close() 	  # fermeture du curseur
    connexion.close() 	  # fermeture de la connexion   
    

def saisie_commande(curseur):
    """
    Saisie des informations de la commande.
    Utilisation du curseur pour afficher le contenu de la BD et pour vérifier
    les contraintes d'ingrétité et les contraintes logiques.

    Parameters
    ----------
    curseur : sqlite3.Cursor
        Curseur de la base de données.

    Returns
    -------
    ncom : str
        Clef primaire de la commande.
    ncli : str
        Clef primaire du client.
    datecom : str
        Date de la commande.
    npros : list
        Liste qui contient les clefs primaires des produits commandés (str).
    qcoms : list
        Liste qui contient les quantités commandées (int).

    """
    
    affiche_commandes(curseur)
    ncom = input("\nDonnez le numéro de commande : ")
    
    while ... :
        print('Ce numéro de commande existe dans la table commande')
        ncom = input("\nDonnez le numéro de commande : ")
    
    datecom = str(datetime.date.today())

    affiche_clients(curseur)
    ncli = input("\nDonnez le numéro de client : ")
    
    while ... :
        print("Ce numéro de client n'existe pas dans la table client")
        ncli = input("\nDonnez le numéro de client : ")
    
    affiche_produits(curseur)    
    npros, qcoms = [], []
    
    nv_pro = True
    while ... :
        
        if ... :
            nv_pro = input('\nVoulez vous ajouter un produit à la commande (oui / non) : ')
            nv_pro = nv_pro == 'oui'
        
        if ... :
        
            npro = input("\nDonnez le numéro de produit : ")            
            while ... or npro in npros:
                msg_err = """Ce numéro de produit n'existe pas dans la table
                produit ou a déjà été commandé lors de cette commande.
                """
                print(msg_err)
                npro = input("\nDonnez le numéro de produit : ")
            
            qcom = int(input("\nDonnez la quantité commandée (un entier): "))
            
            while ... :
                print("La quantité commandée est supérieure au stock disponible.")
                qcom = int(input("\nDonnez la quantité commandée (un entier): "))
            
            npros.append(npro)
            qcoms.append(qcom)
    
    return ncom, ncli, datecom, npros, qcoms


def mise_a_jour_nouvelle_commande(curseur, ncom, ncli, datecom, npros, qcoms):    
    """
    Execute les requêtes SQL pour l'enregistrement d'une nouvelle commande.

    Parameters
    ----------
    curseur : sqlite3.Cursor
        Curseur de la base de données.
    ncom : str
        Clef primaire de l'enregistrement de la commande.
    ncli : str
        Clef primaire de l'enregistrement du client.
    datecom : str
        Date de la commance.
    npros : list
        Liste qui contient les clefs primaires des produits commandés (str).
    qcoms : list
        Liste qui contient les quantités commandées (int).

    """
    requete_commande = ...
    curseur.execute(requete_commande, [ncom, ncli, datecom])
    
    for npro, qcom in zip(npros, qcoms):
        requete_detail = ...
        curseur.execute(requete_detail, [ncom, npro, qcom])
        
        requete_produit = ...
        curseur.execute(requete_produit, [qcom, npro])
        
        prix = calcule_prix(curseur, npro, qcom)
        requete_client = ...
        curseur.execute(requete_client, [prix, ncli])
    
    
def calcule_prix(curseur, npro, qcom):
    """
    Calcule le prix d'une sous-partie d'une commande.

    Parameters
    ----------
    curseur : sqlite3.Cursor
        Curseur de la base de données.
    npro : str
        Clef primaire de l'enregistrement du produit.
    qcom: int
        Quantité commandée.
    
    Returns
    -------
    prix: float
        Prix du produit commandé.
    """
    requete = ...
    curseur.execute(requete, [npro])
    res = curseur.fetchall()
    prix = ...
    return prix
    

#------------------------------------------------------------------------------
#                       Programme principal
#------------------------------------------------------------------------------
nouvelle_commande("../Data/DataBase/client_commande.sqlite")
