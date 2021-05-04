from player1 import Player1
from player2 import Player2
from player3 import Player3
from player4 import Player4
from caractere import Caractere


liam = Player1("Liam", "mcWarren", "riche", "jeune", "M")
ambre = Player2("Ambre", "deCroy", "pauvre", "jeune", "F")
alfred = Player3("Alfred", "Heimsworth", "pauvre", "vieux", "M")
crystal = Player4("Crystal", "Devereux", "riche", "vieux", "F")


print(liam.firstname,liam.name,liam.classe_sociale,liam.age,liam.sexe)
print(ambre.firstname,ambre.name,ambre.classe_sociale,ambre.age,ambre.sexe)
print(alfred.firstname,alfred.name,alfred.classe_sociale,alfred.age,alfred.sexe)
print(crystal.firstname,crystal.name,crystal.classe_sociale,crystal.age,crystal.sexe)


print(liam.list_cartes[1],liam.jauge_de_confiance )
liam.cc()
liam.choix_cartes()