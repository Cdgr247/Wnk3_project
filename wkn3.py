#class ROI_calc:

## Find inp income
 
## find then the total monthly expenses inp 

## and then take the income and subtract it from the expenses 

class roi_calc:
    def roi():  # CASH FLOW
        while True: 
            print("Welcome to roi calc, please enter 1 to start")

            operation = input()
            
            if operation == "1":
                rental = input("enter rental income: ")
                monthly = input("enter the total monthly expenses: ")
                totalnum1 = int(rental) - int(monthly)
                print(totalnum1)

                # TOTAL INVESTMENT

            print("This is your CASH FLOW, ready to get your total investment to get your cash on cash ROI?")

            operation = input()

            if operation == "yes":
                down = input("enter down payment: ")
                closing = input("enter closing cost: ")
                rehab = input("enter rehab budet: ")
                totalnum2 = int(down) + int(closing) + int(rehab)
                print(totalnum2)
            elif operation == "no":
                return f"thank you, come again"
            else:
                return("invalid input! Please enter yes or no")
            
                 
                # ANNUAL CASH FLOW & ROI
            
            print("This is your total investment, Would you like to know your annual cash flow and roi?")

            operation = input()

            if operation == "yes":
                year = 12
                annualcash = totalnum1 * year
                print("annual cash flow: ", annualcash)
                roi = annualcash / totalnum2
                print("ROI: ", roi)
            elif operation == "no":
                return f"thank you, come again"
            else:
                return("invalid input! Please enter yes or no")
            return("Enjoy")
    print(roi())
