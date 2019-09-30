def main():
    print("Time to cash out!")
    hundreds = input("How many Hundred dollar bills do you have?: ")
    fifties = input("How many Fifty dollar bills do you have?: ")
    twenties = input("How many Twenty dollar bills do you have? ")
    tens = input("How many Ten dollar bills do you have? ")
    fives = input("How many Five dollar bills do you have? ")
    ones = input("How many One dollar bills do you have? ")

    print("\nCalculating...\n")

    hundredsAmount = 100 * int(hundreds)
    fiftiesAmount = 50 * int(fifties)
    twentiesAmount = 20 * int(twenties)
    tensAmount = 10 * int(tens)
    fivesAmount = 5 * int(fives)
    onesAmount = 1 * int(ones)
    total = hundredsAmount + fiftiesAmount + twentiesAmount + tensAmount + fivesAmount + onesAmount

    print("Breakdown:\n")
    print("Type of Bill\tNumber of bills\tDollar amount of bills")
    print("Hundreds\t" + hundreds + "\t\t$" + str(hundredsAmount))
    print("Fifties\t\t" + fifties + "\t\t$" + str(fiftiesAmount))
    print("Twenties\t" + twenties + "\t\t$" + str(twentiesAmount))
    print("Tens\t\t" + tens + "\t\t$" + str(tensAmount))
    print("Fives\t\t" + fives + "\t\t$" + str(fivesAmount))
    print("Ones\t\t" + ones + "\t\t$" + str(onesAmount))
    print("Total: $" + str(total))

    input ("\nPress \'Enter\' to exit")
main()
