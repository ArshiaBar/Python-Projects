class character:
    def __init__(self,name, health):
        self.name= name
        self.health= health

    def attack(self):
        print(f"{self.name} attacks!")

class Player(character):
    def __init__(self,name, health, boomower):
        super().__init__(name, health)
        self.boomower = boomower
    def fight(self, amount):
        self.health-=amount
        print(f"The fight has started. {self.name} gets damaged until he's {self.health}.")


class Enemy(character):
    def __init__(self,name, health, boomower):
        super().__init__(name, health)
        self.boomower = boomower
    def fight(self, amount):
        self.health-=amount
        print(f"The fight has started. {self.name} gets damaged until he's {self.health}")

player1= Player("Arshia", 50, 65)

enemy1= Enemy("The street", 50, 70)

player1.fight(20)
enemy1.fight(15)

if player1.health < enemy1.health:
    print(f"{player1.name} loses.")