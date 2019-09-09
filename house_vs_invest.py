#####################################################################
# Desctiption: Down payment & Savings Calculator
# Name: Mehdi Hachimi
# Date Created: 07/12/2014
# Date Modified: 09/09/2019
#####################################################################

from tabulate import tabulate

# getting the variable
starting_salary = float(input("Enter your annual salary: "))

# first calculations and initializing counters
#semiRaiser = float(input("Enter your semi annual raise if known (otherwise type 0): "))
total_cost = float(input("Enter the total cost of the house: "))

portion_down_payment = float(input("Enter your initial down payment: "))
rate_of_interest = float(input("What is the rate that you have been approved : "))
months = input("For how many years : ") * 12
percentage_spend = float(input("How much of your salary can you spend (in percent) : "))


def can_be_bought():
    # these are the steps to calculate the required monthly payments to 
    # repay your mortgage
    # step 1
    mortgage = total_cost - portion_down_payment
    # step 2
    monthly_rate = (rate_of_interest / 100) / 12
    # step 3
    a = (monthly_rate + 1) ** (months)
    # step 4
    b = a * monthly_rate
    # step 5
    c = a - 1
    # step 5.5
    d = b / c
    # step 6
    global monthly_payment = d * mortgage

    # will now check if this monthly payment is in accordance 
    # with the percentage you allow from your salary

    monthly_allowed = (starting_salary * (percentage_spend / 100)) / 12

    if (monthly_allowed < monthly_payment):
        new_monthly_percent = (monthly_payment * 100 * 12) / starting_salary 
        print("Sorry you can't afford this house...you need at least " + str(round(new_monthly_percent, 2)) +"% of your salary, which is " + str(round(monthly_payment, 2)))
        return False
    
    new_monthly_percent = ((monthly_payment * 12) * 100) / starting_salary
    print("Awesome you can afford this house, your monthly payement will be " + str(round(monthly_payment, 2)) + " which is " + str(round(new_monthly_percent, 2)) + "% of your current salary")
    return True


bool_value = can_be_bought()

def vs_investement():
    table = []
    years = months / 12
    principal = portion_down_payement
    s_balance = 0
    interest  = 0
    e_balance = 0
    head = ["Year", "Principal", "Start Balance", "Interest", "End Balance"]

    for month in range(1, months + 1):
        principal = round((principal + month))
        yearly.append(year)
        

        table.append(yearly)

    return tabulate(table, headers=head)







if bool_value:
    print("--------------------------------------")
    answer = raw_input("Would you like to know what your monthly payments would equal in \nthe same period on an investement portfolio at a conservative rate of 6% ? (Y or N) : ")

    if answer == "Y":
        print(vs_investement())
    else:
        print('Thank you for using this program and see you next time')

