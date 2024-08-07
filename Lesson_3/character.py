class Character:
    name = str()
    health = 100
    damage = 1
    defence = 0

    def __init__(self, name, health=100, damage=1, defence=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence

    def show_info(self):
        print(
            f' -< {self.name} >-\n',
            f' HEALTH: {self.health}\n',
            f' DAMAGE: {self.damage}\n',
            f' DEFENCE: {self.defence}\n',
        )

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack(self, target):
        if not isinstance(target, Character):
            print('Target must be Character!')
        target.take_damage(self.damage)
