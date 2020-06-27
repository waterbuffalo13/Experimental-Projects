from hillclimber.climbinghill import climbingHill
from hillclimber.secretNumber import secretNumber


def main():
    # random_secret_number = secretNumber().generate_random_secret_number()
    bespoke_secret_number = secretNumber().generate_custom_secret_number(12,16)
    hillclimber = climbingHill(bespoke_secret_number)
    print("bespoke number: " + str(bespoke_secret_number))
    hillclimber.run_hillclimber()








if __name__== "__main__":
    main()