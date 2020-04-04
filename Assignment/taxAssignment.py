
# def calculator(gross ,state):
#     state_tax={"BOS":9,"NJ":8,"TX":7,"CA":10,"NY":6}
#     netIncome=gross-(gross*.10)
#
#     if state in state_tax:
#         netIncome=netIncome-(gross*state_tax[state]/100)
#         print("your net income is:" +str(netIncome))
#         return netIncome
#
#     else:
#         print("enter your details correctly")
#
# d=calculator(123456,"NY")



def taxCalculator(state,gross):

    state_tax= {"NY":9, "LA":8, "SFO":7,"BOS":10}
    # 10% is default fedral tax
    netIncome = gross-(gross*.10)

    if state in state_tax:
        netIncome=netIncome-(gross*state_tax[state]/100)
        print("Your net income is :" ,netIncome)
        return netIncome
    else:
        print("please enter your state correctly")




tax = taxCalculator("LA",100000)
