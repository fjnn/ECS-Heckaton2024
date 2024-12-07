class Energy:
    def __init__(self):
        self.current_energy = 25
        self.max_energy = 100

    def add_energy(self, amount):
        if self.current_energy + amount > self.max_energy:
            self.current_energy = self.max_energy
        else:
            self.current_energy += amount

    def reduce_energy(self, amount):
        if self.current_energy - amount < 0:
            self.current_energy = 0
        else:
            self.current_energy -= amount
