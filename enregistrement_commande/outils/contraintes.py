#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Fonctions qui vérifient la validité des contraintes d'intégrité.
"""

def existe_ncom(curseur, ncom):
    """
    Vérifie l'existence d'une commande dans la table commande.

    Parameters
    ----------
    curseur : sqlite3.Cursor
        Curseur de la base de données.
    ncom : str
        Clef primaire de l'enregistrement.

    Returns
    -------
    bool
        True si la clef primaire existe, False sinon.

    """
    requeteSQL = ...
    curseur.execute(requeteSQL, [ncom])
    res = curseur.fetchall()
    
    if res:
        return True
    else:
        return False
    
def existe_npro(curseur, npro):
    """
    Vérifie l'existence d'un produit dans la table produit.

    Parameters
    ----------
    curseur : sqlite3.Cursor
        Curseur de la base de données.
    npro : str
        Clef primaire de l'enregistrement.

    Returns
    -------
    bool
        True si la clef primaire existe, False sinon.

    """
    requeteSQL = ...
    curseur.execute(requeteSQL, [npro])
    res = curseur.fetchall()
    if res:
        return True
    else:
        return False
    
def existe_ncli(curseur, ncli):
    """
    Vérifie l'existence d'un client dans la table client.

    Parameters
    ----------
    curseur : sqlite3.Cursor
        Curseur de la base de données.
    ncli : str
        Clef primaire de l'enregistrement.

    Returns
    -------
    bool
        True si la clef primaire existe, False sinon.

    """
    requeteSQL = ...
    curseur.execute(requeteSQL, [ncli])
    res = curseur.fetchall()
    
    if res:
        return True
    else:
        return False
    
def stock_suffisant(curseur, npro, qcom):
    """
    Vérifie si le stock est en quantité suffisante pour la commande.

    Parameters
    ----------
    curseur : sqlite3.Cursor
        Curseur de la base de données.
    npro : str
        Clef primaire de l'enregistrement du produit.
    qcom : int
        Quantité commandée.

    Returns
    -------
    bool
        True si le stock est supérieur ou égal à la quantité commandée,
        False sinon.

    """
    stock = qstock(curseur, npro)
    return ...
    
def qstock(curseur, npro):
    """
    Extraction de la quantité en stock pour un produit donné.
    
    Parameters
    ----------
    curseur : sqlite3.Cursor
        Curseur de la base de données.
    npro : str
        Clef primaire de l'enregistrement du produit.
    
    Returns
    -------
    stock: int
        Quantité en stock.

    """
    requeteSQL = ...
    curseur.execute(requeteSQL, [npro])
    res = curseur.fetchall()
    stock = ...
    return ...