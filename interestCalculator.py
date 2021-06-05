def compoundRateFinder():
    compoundRateDeterminer = input("What is the compound rate?\n1. Annually\n2. Semi-annually\n3. Quarterly\n 4. Monthly\n 5.Weekly\n")
    global compoundRate
    if int(compoundRateDeterminer) == 1:
        compoundRate = 1
        return 1
    elif int(compoundRateDeterminer) == 2:
        compoundRate = 2
        return 2
    elif int(compoundRateDeterminer) == 3:
        compoundRate = 4
        return 4
    elif int(compoundRateDeterminer) == 4:
        compoundRate = 12
        return 12
    elif int(compoundRateDeterminer) == 5:
        compoundRate = 52
        return 52
    else:
        print("Invalid Response")


def compoundInterest():
    principle = input("What is the initial amount?")
    time = input("What is the amount of time in years? (Ex. \'3\')")
    interestRate = input("What is the interest rate (in decimals)?")
    compoundRate = compoundRateFinder()
    percentTotal = (1+(float(interestRate) / compoundRate))
    compoundTotal = (compoundRate * float(time))
    interestTotal = percentTotal ** compoundTotal
    print("This is your total with interest:")
    print(int(principle) * interestTotal)


def simpleInterest(intRate, prin, time2):
    interestTotal2 = intRate * prin * time2
    print("This is your interest:" + str(interestTotal2))
    print("This is your total with interest:")
    print(prin + interestTotal2)


print("Welcome to Zack's Interest Calculator")
interestType = input("What sort of interest would you like to calculate?\n 1. for simple interest\n 2. for compound interest\n")
if int(interestType) == 1:
    inputHolder1 = input("what is your interest rate (decimals)?\n")
    inputHolder2 = input("What is your principal?\n")
    inputHolder3 = input("What is the amount of years?\n")
    simpleInterest(float(inputHolder1), float(inputHolder2), float(inputHolder3))
elif int(interestType) == 2:
    compoundInterest()
