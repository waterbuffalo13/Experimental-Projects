import random

class climbingHill:
    def __init__(self, secret_number):
        self.estimated_factor_1 = random.randrange(1, 5)
        self.estimated_factor_2 = random.randrange(1, 5)
        self.estimated_result = self.estimated_factor_1*self.estimated_factor_2
        self.secret_number = secret_number

    def get_estimated_result(self):
        return self.estimated_result

    def get_equivalence(self):
        if self.estimated_result == self.secret_number:
            return "True"
        else:
            return "False"

    def generate_new_factors(self, est_factor1, est_factor2):
        self.estimated_factor_1=est_factor1
        self.estimated_factor_2=est_factor2
        self.estimated_result = est_factor1*est_factor2



    def run_hillclimber(self):
        flag = "True"
        iteration = 0
        # heuristic = None
        while flag == "True" and iteration < 5:
            if self.get_equivalence() == "False":
                #the estimated number is too big
                # if self.get_estimated_result() > self.secret_number:
                factor1 = random.randrange(1, 5)
                factor2 = random.randrange(1, 5)
                self.generate_new_factors(factor1, factor2)

                print("--------")
                print("Iteration: " + str(iteration))
                print("estimated vs real: " + str(self.get_estimated_result()), "vs " + str(self.secret_number))
                print("equivalence:" + self.get_equivalence())

                if self.get_estimated_result() > self.secret_number:
                    heuristic = "too big"
                elif self.get_estimated_result() < self.secret_number:
                    heuristic = "too small"
                else:
                    flag = "False"
                print(heuristic)

                # elif self.get_estimated_result() < self.secret_number:
                #     heuristic ="too small"
                #     factor1 = random.randrange(1, 5)
                #     factor2 = random.randrange(1, 5)
                #     self.generate_new_factors(factor1, factor2)
                #     print("--------")
                #     print("Iteration: " + str(iteration))
                #     print("estimated vs real: " + str(self.get_estimated_result()), "vs " + str(self.secret_number))
                #     print("equivalence:" + self.get_equivalence())
                #     print(heuristic)
                iteration = iteration + 1
            else:
                flag="False"
                print("----")
                print("Congrats")





