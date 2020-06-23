import random

class climbingHill:
    def __init__(self, secret_number):
        self.estimated_factor_1 = random.randrange(1, 5)
        self.estimated_factor_2 = random.randrange(1, 5)
        self.estimated_result = self.estimated_factor_1 * self.estimated_factor_2

        self.secret_number = secret_number
        self.iteration = 1

    def get_estimated_result(self):
        return self.estimated_result

    def get_equivalence(self):
        if self.estimated_result == self.secret_number:
            return "True"
        else:
            return "False"

    def set_new_factors(self, est_factor1, est_factor2):
        self.estimated_factor_1=est_factor1
        self.estimated_factor_2=est_factor2
        self.estimated_result = est_factor1*est_factor2

    def run_hillclimber(self):
        self.print_state()

        estimate_too_big = self.get_estimated_result() > self.secret_number
        estimate_too_small = self.get_estimated_result() < self.secret_number

        iteration = 0
        while self.iteration < 10:
            if self.get_equivalence() == "False":
                if self.get_estimated_result() > self.secret_number:
                    random_number1 = random.randint(0,1)
                    random_number2 = random.randint(0,1)
                    print("random_number_1:" + str(random_number1))
                    print("random_number_2:" + str(random_number2))

                    factor1 = self.estimated_factor_1 - random_number1
                    factor2 = self.estimated_factor_2 - random_number2
                    # factor1 = random.randrange(1, 5)
                    # factor2 = random.randrange(1, 5)
                #too small
                elif self.get_estimated_result() < self.secret_number:
                    random_number1 = random.randint(0,1)
                    random_number2 = random.randint(0,1)
                    print("random_number_1:" + str(random_number1))
                    print("random_number_2:" + str(random_number2))

                    factor1 = self.estimated_factor_1 + random_number1
                    factor2 = self.estimated_factor_2 + random_number2
                    # factor1 = random.randrange(1, 5)
                    # factor2 = random.randrange(1, 5)

                self.set_new_factors(factor1, factor2)
                self.print_state()
                self.iteration = self.iteration + 1
            else:
                break
                print("----")
                print("Congrats")

    def print_state(self):
        print("estimated vs real: " + str(self.get_estimated_result()), "vs " + str(self.secret_number))
        print("equivalence:" + self.get_equivalence())
        print("factor1: " + str(self.estimated_factor_1))
        print("factor2: " + str(self.estimated_factor_2))
        if self.get_estimated_result() > self.secret_number:
            heuristic = "too big -> reduce a factor"
        elif self.get_estimated_result() < self.secret_number:
            heuristic = "too small -> increase a factor"
        else:
            heuristic = "just right"
        print(heuristic)
        print("----")
        print("iteration: " + str(self.iteration))





