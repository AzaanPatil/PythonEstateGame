from utils.dice import roll_dice


class Player:
    def __init__(self, name, is_cpu=False, difficulty="easy", balance=100000):
        self.name = name
        self.balance = balance
        self.position = 0
        self.properties = []
        self.is_cpu = is_cpu
        self.difficulty = difficulty
        self.is_bankrupt = False

    def roll_dice(self):
        return roll_dice()

    def move_by(self, steps, board):
        previous_position = self.position
        self.position = (self.position + steps) % len(board.tiles)
        return previous_position, self.position

    def can_afford(self, amount):
        return self.balance >= amount

    def pay(self, amount):
        self.balance -= amount

    def receive(self, amount):
        self.balance += amount

    def buy_property(self, property):
        self.pay(property.price)
        property.owner = self
        self.properties.append(property)

    def net_worth(self):
        return self.balance + sum(property.price for property in self.properties)
