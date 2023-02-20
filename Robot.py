import random
class robot:
    def __init__(self,name,type):
     self.name = ''
     self.type = ''
     self.health = 100
     self.attacks = ['Electric Shock']
     def create_attacks(self):
        user_input = ''
        while user_input != '1':
            user_input = input(f'Please Enter a new attack for {self.name}. or press enter to exit.')
            if user_input != '1':
                self.attacks.append(user_input)
                print(f'you have successfully added {user_input} to attack list')
        print(f'Final Attack list for {self.name}:')
        print(self.attacks)
        def attack(self,other_opponent):
            damage = random.randit(10,20)
            random_attacks = random.choice(self.attacks)
            other_opponent.health -= damage
            print(f'{self.name} attacks {other_opponent.name} with {random_attacks}')