#####################################################################
# Desctiption: Down payment & Savings Calculator
# Name: Mehdi Hachimi
# Date Created: 07/12/2014
# Date Modified: 10/09/2019
#####################################################################

from tabulate import tabulate

# getting the variable
starting_salary = float(input("Enter your annual salary: "))

# first calculations and initializing counters
#semiRaiser = float(input("Enter your semi annual raise if known (otherwise type 0): "))
total_cost = float(input("Enter the total cost of the house: "))

portion_down_payement = float(input("Enter your initial down payment: "))
rate_of_interest = float(input("What is the rate that you have been approved : "))
months = input("For how many years : ") * 12
percentage_spend = float(input("How much of your salary can you spend (in percent) : "))


def can_be_bought():
    # these are the steps to calculate the required monthly payments to 
    # repay your mortgage
    # step 1
    mortgage = total_cost - portion_down_payement
    # step 2
    global monthly_rate
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
    global monthly_payement
    monthly_payement = d * mortgage

    # will now check if this monthly payment is in accordance 
    # with the percentage you allow from your salary

    monthly_allowed = (starting_salary * (percentage_spend / 100)) / 12

    if (monthly_allowed < monthly_payement):
        new_monthly_percent = (monthly_payement * 100 * 12) / starting_salary 
        print("Sorry you can't afford this house...you need at least " + str(round(new_monthly_percent, 2)) +"% of your salary, which is " + str(round(monthly_payement, 2)))
        return False
    
    new_monthly_percent = ((monthly_payement * 12) * 100) / starting_salary
    print("Awesome you can afford this house, your monthly payement will be " + str(round(monthly_payement, 2)) + " which is " + str(round(new_monthly_percent, 2)) + "% of your current salary")
    return True


bool_value = can_be_bought()

def vs_investement():
    table = []
    year = 0
    s_principal = portion_down_payement
    last_interest = 0
    s_balance = portion_down_payement
    interest  = 0
    e_balance = 0
    head = ["Year", "Start Principal", "Interest", "End Balance"]

    for month in range(1, months + 1):
        interest = round((s_balance * monthly_rate), 1)
        e_balance = round((s_balance + monthly_payement + interest), 1)
        s_balance = e_balance
        
        if month % 12 == 0:
            yearly = []
            year += 1
            interest = (e_balance - (portion_down_payement + (monthly_payement * month))) - last_interest
            last_interest += interest
            yearly.extend([year, s_principal, interest, e_balance])
            s_principal += (monthly_payement * 12)
            table.append(yearly)
    s_principal = s_principal - (monthly_payement * 12)
    print("With your contributions of a total of " + str(s_principal) + "$ your estimated total returns would be " + str(e_balance - s_principal) + "$. A grand total of " + str(e_balance) + "$." )
    answer = raw_input("Would you like to see a detailed year by year table ? : ")
    if answer == "Y" or answer == "Yes" or answer == "yes":
        return tabulate(table, headers=head, tablefmt="fancy_grid")
    return "Thank you for using me! Good Day."



if bool_value:
    print("--------------------------------------")
    answer = raw_input("Would you like to know what your monthly payments would equal in \nthe same period on an investement portfolio at a conservative rate of 6% ? (Y or N) : ")

    if answer == "Y":
        print(vs_investement())
    else:
        print('Thank you for using this program and see you next time')

