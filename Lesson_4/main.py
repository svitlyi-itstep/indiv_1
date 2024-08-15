from Lesson_3.character import Character
from berserk import Berserk

player1 = Character("Valera", damage=11)
player2 = Berserk(name="Petro", health=120, damage=10)

player1.show_info()
player2.show_info()

while player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    player2.attack(player1)

    player1.show_info()
    player2.show_info()