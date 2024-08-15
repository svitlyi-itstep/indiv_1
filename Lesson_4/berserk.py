from Lesson_3.character import Character


class Berserk(Character):
    max_health = int()

    def __init__(self, name, health=100, damage=1, defence=0):
        super().__init__(name, health, damage, defence)
        self.max_health = health

    def attack(self, target):
        if not isinstance(target, Character):
            print('Target must be Character!')
        additional_damage = round((1 - self.health / self.max_health) * self.damage, 2)
        target.take_damage(self.damage + additional_damage)
