from caractere import Caractere


class Player1(Caractere):
    def __init__(self, firstname, name, classe_sociale, age, sexe):
        super().__init__(firstname, name, classe_sociale, age, sexe)

        self.list_cartes = [1, 2, 3]
        self.list_boutdephrase = [1, 2, 3]
        self.jauge_de_confiance = 0

    def cc(self):
        pass