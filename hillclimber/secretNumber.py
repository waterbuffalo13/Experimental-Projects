import random

class secretNumber:

    def __init__(self):
        self.factor_1 = random.randrange(1,10)
        self.factor_2 = random.randrange(1,10)

    def generate_random_secret_number(self):
        secret_number = self.factor_1 * self.factor_2
        return secret_number

    def generate_custom_secret_number(self, input_1, input_2):
        secret_number = input_1*input_2
        return secret_number