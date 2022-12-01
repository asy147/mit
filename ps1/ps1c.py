'''
 In Part A, we are going to determine how long it will take you to save enough
money to make the down payment given the following assumptions:
'''

annual_salary = float(input("starting annual salary: "))
init_salary = annual_salary
total_cost = 1000000
semi_annual_raise = .07
portion_down_payment = .25
current_savings = float(0)
r = 0.04

number_months = 0

target_months = 36
number_guesses = 0
epsilon = 100
low = 0
high = 10000
guess_int = int((low + high) / 2)
portion_saved  = guess_int / 10000.0
print(portion_saved, "portion")
#try 100% save to see if it is possible ?
print("target: ", total_cost * portion_down_payment)

while abs(current_savings - total_cost * portion_down_payment) >= epsilon:
    current_savings = current_savings + (annual_salary * portion_saved / 12) + (current_savings * r / 12)
    #add check that if value is higher than target and mo < 36 try lower?
    if number_months == 36:
        print("number guess ", number_guesses, " was it greater than target? ", current_savings > total_cost * portion_down_payment)
        if abs(total_cost * portion_down_payment - current_savings) <= epsilon:
            print("found a value!")
            break
        elif current_savings < total_cost * portion_down_payment:
            print("\nat 36 mo",current_savings ," was LOWER so previous low bound was ", low)
            low = guess_int
            print("new low bound is ",low, "high bound is still", high)
        elif current_savings > total_cost * portion_down_payment:
            print("\nat 36 mo" , current_savings,"was HIGHER so previous high bound was ", high)
            high = guess_int
            print("new high bound is ",high, "low bound is still", low)

        #we have set net boundaries, now we need to reset the iterable growing values
        current_savings = float(0)
        number_months = 0
        annual_salary = init_salary
        guess_int  = int((low + high) / 2)
        portion_saved = guess_int / 10000.0
        print(portion_saved * 10000, "new portion")
        number_guesses += 1
        if number_guesses >= 20:
            print("not possible")
            break
        
    number_months += 1
    if number_months % 6 == 0:
        annual_salary *= (1 + semi_annual_raise)


print("\nBest saving rate: ", portion_saved)
print("\nSteps in bisection search: ", number_guesses)


#print(total_cost * portion_down_payment)

#tenta um numero, vai subindo os meses e o dinheiro, se bater din antes dos meses abaixa, senao aumenta, increase guess number
#    if number_months == 36: didnt work
#while abs(current_savings - total_cost * portion_down_paymen) >= epsilon:
