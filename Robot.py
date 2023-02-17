import random
class robot:
    def __init__(self, name, type):
     self.name = name
     self.type = type
     self.health = 100
     self.attacks = ['electric shock']
     self.create_attack()

     def create_attack(self):
        user_input = ''
        while user_input != '2':
         user_input = input(f'enter a new attack for{self.name}:')
        if user_input != '2':
            self.attacks.append(user_input)
        print(f'final attack list for {self.name}:')
        print(self.attacks)
        print('')
        def attack(self,other_class):
         damage = random.randit(10,20)
         random_attack = random.choice(self.attacks)

