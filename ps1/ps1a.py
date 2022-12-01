'''
 In Part A, we are going to determine how long it will take you to save enough
money to make the down payment given the following assumptions:
'''

annual_salary = float(input("starting annual salary: "))
portion_saved = float(input("\nportion of salary to be saved: "))
total_cost = float(input("\ncost of your dream home: "))
portion_down_payment = .25
current_savings = float(0)
r = 0.04
number_months = 0

while current_savings <= total_cost * portion_down_payment:
    current_savings = current_savings + (annual_salary * portion_saved / 12) + (current_savings * r / 12)
#    print(current_savings)
    number_months += 1
#    print(number_months)

print("\nNumber of months: ", number_months)

#print(total_cost * portion_down_payment)
