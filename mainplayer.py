from player1 import Player1
from player2 import Player2

from caractere import Caractere
from cartes import *
from game import *


liam = Caractere("Liam", "mcWarren", "populaire", "jeune", "M")
ambre = Caractere("Ambre", "deCroy", "noble", "jeune", "F")
alfred = Caractere("Alfred", "Heimsworth", "noble", "vieux", "M")
crystal = Caractere("Crystal", "Devereux", "populaire", "vieux", "F")


# print(liam.firstname,liam.name,liam.   e_sociale,liam.age,liam.sexe)
# print(ambre.firstname,ambre.name,ambre.   e_sociale,ambre.age,ambre.sexe)
# print(alfred.firstname,alfred.name,alfred.   e_sociale,alfred.age,alfred.sexe)
# print(crystal.firstname,crystal.name,crystal.   e_sociale,crystal.age,crystal.sexe)


# print(liam.list_cartes[1],liam.jauge_de_confiance )

# :::carte unique
#Liam
#Ambre
Secret_familial = Secret_familial(Game, "Secret_familial", "Unique")
Regard_enjoleur = Regard_enjoleur( Game, "Regard_enjoleur", "Unique")
Conseils_avisees = Conseils_avisees( Game, "Conseils_avisees", "Unique")
#Alfred
Cest_pas_au_vieux_singe = Cest_pas_au_vieux_singe(Game, "Cest_pas_au_vieux_singe", "Unique")
Seconde_vie = Seconde_vie(Game, "Seconde_vie", "Unique")  
Service_sur_mesure = Service_sur_mesure(Game, "Service_sur_mesure", "Unique") 

#Crystal
Rhetorique_de_limperatrice = Rhetorique_de_limperatrice(Game, "Rhetorique_de_limperatrice", "Unique")    
Sombre_formule = Sombre_formule( Game, "Sombre_formule", "Unique") 
Influence_mystique = Influence_mystique(Game, "Influence_mystique", "Unique")    

#Cartes Comune
#Jeune
Gout_du_risque = Gout_du_risque( Game, "Gout_du_risque", "Jeune") 
Sante_de_fer = Sante_de_fer ( Game, "Sante_de_fer", "Jeune")     

   

Adaptation = Adaptation( Game, "Adaptation ", "Jeune")    

Esprit_vif = Esprit_vif( Game, "Esprit_vif ", "Jeune")     

   

#âgé
Experience_de_lage = Experience_de_lage = Experience_de_lage(Game, "Experience_de_lage ", "âgé")    

   

Veteran = Veteran(Game, " Veteran ", "âgé")     
   

Sante_fragile = Sante_fragile(Game, " Sante fragile ", "âgé")    

   

Oeil_sage = Oeil_sage( Game, " Oeil sage", "âgé")     

#Homme
Avantage_masculin = Avantage_masculin( Game, "Avantage masculin", "Homme")    
   

Tonalite_virile = Tonalite_virile ( Game, "Tonalite virile", "Homme")   
   

Sens_du_sacrifice = Sens_du_sacrifice(Game, "Sens du sacrifice", "Homme")   

Monotache = Monotache(Game, "Monotache", "Homme")    

   

#Femme
Avantage_feminin = Avantage_feminin(Game, "Avantage_feminin", "Femme")    

   

Mauvaise_foi = Mauvaise_foi(Game, "Mauvaise foi", "Femme")    
   

Seduction = Seduction(Game, "Seduction", "Femme")    

Multitache = Multitache( Game, "Multitache", "Femme")     

#Noble
Opulence = Opulence(Game, "Opulence", "Noble")    

Hautes_relations = Hautes_relations( Game, "Hautes relations", "Noble")     
Mepris_du_fortune = Mepris_du_fortune( Game, "Mepris_du_fortune", "Noble")   
Pot_de_vin = Pot_de_vin( Game, "Pot_de_vin", "Noble")     
    
#Populaire
Solidarite = Solidarite(Game, "Solidarite", "Populaire") 
Priere_misericordieuse = Priere_misericordieuse( Game, "Priere_misericordieuse", "Populaire")     
Coup_de_chance = Coup_de_chance( Game, "Coup_de_chance", "Populaire") 
Avantage_du_nombre = Avantage_du_nombre( Game, "Avantage_du_nombre", "Populaire")    
   




