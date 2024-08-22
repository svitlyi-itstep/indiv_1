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

    def __str__(self):
        return f' -< {self.name} >-\n'\
               f' HEALTH: {self.health}\n' \
               f' DAMAGE: {self.damage}\n' \
               f' DEFENCE: {self.defence}\n' \


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

    def get_health(self):
        return self.health

    def set_health(self, health: int):
        if not isinstance(health, int):
            raise TypeError('health must be integer')
        self.health = max(health, 0)
