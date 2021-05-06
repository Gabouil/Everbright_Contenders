from player1 import Player1
from player2 import Player2
from player3 import Player3
from player4 import Player4
from caractere import Caractere
from cartes import Cartes


liam = Player1("Liam", "mcWarren", "riche", "jeune", "M")
ambre = Player2("Ambre", "deCroy", "pauvre", "jeune", "F")
alfred = Player3("Alfred", "Heimsworth", "pauvre", "vieux", "M")
crystal = Player4("Crystal", "Devereux", "riche", "vieux", "F")


print(liam.firstname,liam.name,liam.   e_sociale,liam.age,liam.sexe)
print(ambre.firstname,ambre.name,ambre.   e_sociale,ambre.age,ambre.sexe)
print(alfred.firstname,alfred.name,alfred.   e_sociale,alfred.age,alfred.sexe)
print(crystal.firstname,crystal.name,crystal.   e_sociale,crystal.age,crystal.sexe)


print(liam.list_cartes[1],liam.jauge_de_confiance )
liam.cc()
liam.choix_cartes()

# :::carte unique
#Liam
True_story = True_story( game, "True_story", "Unique")
print(True_story)
Peche_davarice = Peche_davarice(game, "Peche davarice", "Unique")
Gamin_des_rues = Gamin_des_rues(game, "Gamin_des_rues", "Unique")
#Ambre
Secret_familial = Secret_familial(game, "Secret_familial", "Unique")
Regard_enjoleur = Regard_enjoleur( game, "Regard_enjoleur", "Unique")
Conseils_avisees = Conseils_avisees( game, "Conseils_avisees", "Unique")
#Alfred
Cest_pas_au_vieux_singe = Cest_pas_au_vieux_singe(game, "Cest_pas_au_vieux_singe", "Unique")
Seconde_vie = Seconde_vie(game, "Seconde_vie", "Unique")  
Service_sur_mesure = Service_sur_mesure(game, "Service_sur_mesure", "Unique") 

#Crystal
Rhetorique_de_limperatrice = Rhetorique_de_limperatrice(game, "Rhetorique_de_limperatrice", "Unique")    
Sombre_formule = Sombre_formule( game, "Sombre_formule", "Unique") 
Influence_mystique = Influence_mystique(game, "Influence_mystique", "Unique")    

#Cartes Comune
#Jeune
Gout_du_risque = Gout_du_risque( game, "Gout_du_risque", "Jeune") 
Sante_de_fer = Sante_de_fer ( game, "Sante_de_fer", "Jeune")     

   

Adaptation = Adaptation( game, "Adaptation ", "Jeune")    

Esprit_vif = Esprit_vif( game, "Esprit_vif ", "Jeune")     

   

#âgé
Experience_de_lage = Experience_de_lage = Experience_de_lage(game, "Experience_de_lage ", "âgé")    

   

Veteran = Veteran(game, " Veteran ", "âgé")     
   

Sante_fragile = Sante_fragile(game, " Sante fragile ", "âgé")    

   

Oeil_sage = Oeil_sage( game, " Oeil sage", "âgé")     

#Homme
Avantage_masculin = Avantage_masculin( game, "Avantage masculin", "Homme")    
   

Tonalite_virile = Tonalite_virile ( game, "Tonalite virile", "Homme")   
   

Sens_du_sacrifice = Sens_du_sacrifice(game, "Sens du sacrifice", "Homme")   

Monotache = Monotache(game, "Monotache", "Homme")    

   

#Femme
Avantage_feminin = Avantage_feminin(game, "Avantage_feminin", "Femme")    

   

Mauvaise_foi = Mauvaise_foi(game, "Mauvaise foi", "Femme")    
   

Seduction = Seduction(game, "Seduction", "Femme")    

Multitache = Multitache( game, "Multitache", "Femme")     

#Noble
Opulence = Opulence(game, "Opulence", "Noble")    

Hautes_relations = Hautes_relations( game, "Hautes relations", "Noble")     
Mepris_du_fortune = Mepris_du_fortune( game, "Mepris_du_fortune", "Noble")   
Pot_de_vin = Pot_de_vin( game, "Pot_de_vin", "Noble")     
    
#Populaire
Solidarite = Solidarite(game, "Solidarite", "Populaire") 
Priere_misericordieuse = Priere_misericordieuse( game, "Priere_misericordieuse", "Populaire")     
Coup_de_chance = Coup_de_chance( game, "Coup_de_chance", "Populaire") 
Avantage_du_nombre = Avantage_du_nombre( game, "Avantage_du_nombre", "Populaire")    
   




