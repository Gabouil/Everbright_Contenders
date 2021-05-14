mots = [

]
phrase = ""
self.player_turn.mots.append(self.game_mots.mot1.name + " ")

del self.game.player_turn.mots[-1]

for mot in self.player_turn.mots:
    phrase += mot

print(phrase)