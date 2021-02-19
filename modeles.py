import sys
from typing import *
from enum import IntEnum

class Helico:
    def __init__(self, serial_number:str):
        self.serial_number:str = sys.intern(serial_number) ## identifiant unique de l'hélico
        self.status:str = None
        self.maintenances:List[Maintenance] = list()  ## Maintenances subis
        self.pieces:List[Piece] = list()  ## Listes des composants associés

class Piece:
    """ Propriétés des pièces du fichier '20210105_MTBF vs MTBUR.xlsx'
    """
    def __init__(self):
        self.index_de:int = 0
        self.designation:str = None
        self.categorie = None  ## identifiant commun à toutes les pièces du même type
        self.mtbf:int = 0  ## Temps supposé de fonctionnement avant panne
        self.mtbur:int = 0  ## Temps réel de fonctionnement avant d'être remplacé
            
class TypeMaintenance(IntEnum):
    CORRECTIVE = 0
    PREVENTIVE = 1
        
class Maintenance:
    """ La liste des maintenances est dans le fichier '20210105_Historique maintenance.xlsx', onglet 'HISTORIQUE_PREV_CORR'
    """
    def __init__(self):
        self.numero = 0
        self.type = TypeMaintenance.CORRECTIVE
        self.temps_passe = 0