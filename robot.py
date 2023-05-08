from dinosaur import Dinosaur
from weapon import Weapon


attack_one = Weapon('Electric Shock', 35)
attack_two = Weapon('Rocket Blast', 65)
attack_three = Weapon('Laser Beam', 95)
attack_four = Weapon('Skip Turn', 0)


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = attack_one
    

    def choose_weapon(self):
        

        print(f'If you plan on winning, youre going to need a weapon!')
        print(f'You have 3 choices. They are: Electric Shock(1), Rocket Blast(2) & Laser Beam(3)! ' )
        user_choice = input(f'Which of these 3 attacks would you like to use against your opponenet? ')

        if user_choice == ("Electric Shock",'1'):
            attack_one ==self.active_weapon
        elif user_choice == ("Rocket Blast",'2'):
            attack_two == self.active_weapon
        elif user_choice == ('Laser Beam', '3'):
            attack_three == self.active_weapon
        elif user_choice == ("Skip Turn", "4"):
            self.active_weapon==attack_four

    def attack(self,dinosaur):
        print(f'{self.name} attacked {dinosaur.name} with {self.active_weapon.name} and caused {self.active_weapon.attack_power}')
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{dinosaur.name} has {dinosaur.health} health!')
        print("")
