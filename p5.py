def compound_interest(principal, rate, time):
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)
compound_interest(float(input("enter the principal amount:")), float(input("enter the rate amount:")), float(input("enter the time:")))