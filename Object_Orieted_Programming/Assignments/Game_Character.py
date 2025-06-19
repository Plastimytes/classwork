# Base GameObject class
class GameObject:
    def __init__(self, position):
        self.position = position

    def update(self):
        # default update method
        print(f'GameObject at position {self.position} updated.')

    def render(self, ctx=None):
        # default render method
        print(f'GameObject at position {self.position} rendered.')


# Character class without inheritance
class Character:
    def __init__(self, position, health):
        self.position = position
        self.health = health

    def update(self):
        # default update logic for character if needed
        print(f'Character at position {self.position} with health {self.health} updated.')

    def render(self, ctx=None):
        # default render method for character
        print(f'Character at position {self.position} with health {self.health} rendered.')

    def take_damage(self, amount):
        self.health -= amount
        print(f'Character took {amount} damage, health now {self.health}.')
        if self.health <= 0:
            self.die()

    def die(self):
        print('Character died')


# Player class without inheritance - manually include Character behavior
class Player:
    def __init__(self, position, health, name):
        self.name = name
        # Instead of inheritance, create Character instance internally
        self.character = Character(position, health)

    @property
    def position(self):
        return self.character.position

    @position.setter
    def position(self, value):
        self.character.position = value

    @property
    def health(self):
        return self.character.health

    @health.setter
    def health(self, value):
        self.character.health = value

    def update(self):
        print(f'Player "{self.name}" update called.')
        self.character.update()

    def render(self, ctx=None):
        print(f'Player "{self.name}" render called.')
        self.character.render(ctx)

    def take_damage(self, amount):
        print(f'Player "{self.name}" taking damage.')
        self.character.take_damage(amount)

    def die(self):
        print(f'Player "{self.name}" died.')


# Enemy class without inheritance - manually include Character behavior
class Enemy:
    def __init__(self, position, health, type):
        self.type = type
        self.character = Character(position, health)

    @property
    def position(self):
        return self.character.position

    @position.setter
    def position(self, value):
        self.character.position = value

    @property
    def health(self):
        return self.character.health

    @health.setter
    def health(self, value):
        self.character.health = value

    def update(self):
        print(f'Enemy of type "{self.type}" update called.')
        self.character.update()

    def render(self, ctx=None):
        print(f'Enemy of type "{self.type}" render called.')
        self.character.render(ctx)

    def take_damage(self, amount):
        print(f'Enemy of type "{self.type}" taking damage.')
        self.character.take_damage(amount)

    def die(self):
        print(f'Enemy of type "{self.type}" died.')


# Demo usage
def main():
    player = Player(position=(10, 20), health=100, name='Hero')
    enemy = Enemy(position=(15, 25), health=50, type='Goblin')

    print('--- Initial update and render ---')
    player.update()
    player.render()
    enemy.update()
    enemy.render()

    print('\n--- Inflicting damage ---')
    player.take_damage(30)
    enemy.take_damage(60)  # this should kill the enemy

    print('\n--- State after damage ---')
    print(f'Player health: {player.health}')
    print(f'Enemy health: {enemy.health}')


if __name__ == '__main__':
    main()




