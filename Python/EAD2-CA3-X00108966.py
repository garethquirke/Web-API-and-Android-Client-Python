from functools import reduce

# euro to dollar
def euroToDollar(amount):
    return round((amount  * 1.09), 2)


# dollar to euro
def dollarToEuro(amount):
    return round((amount * 0.92), 2)

print('50 euro to dollars' , euroToDollar(50))
print('50 dollars to euro' , dollarToEuro(50))


# list of account transactions
# current balance 250
account = [100, 200, -50]

# debit an account ensure the amount is less than 0
def debitAccount(amount, transactions):
    if amount >= 0:
        return
    else:
        transactions.append(amount)

# test method
debitAccount(-20, account)
debitAccount(400, account)
print(account)

def creditAccount(amount, transactions):
    # ensuring the amount is not 0
    if amount == 0:return
    if amount < 0: return
    else:transactions.append(amount)

# test credit method
creditAccount(50, account)
creditAccount(0, account)
print(account)

# get balance method
def getBalance(account):
    positive = 0
    negative = 0
    for i in account:
        if i < 0: negative = negative + i
        else: positive = positive + i
    return positive + negative

print("Balance of account: " , getBalance(account))


# using map to to convert the account into dollars
accountdollars = list(map(euroToDollar, account))
print(accountdollars)


#def formatAccount(transactions):
#    details = ""
#    reduce(lambda current: current if current < 0 details = details + "Debit: " + current else details = "Credit: " + current, transactions)
#    print details

#formatAccount(account)                