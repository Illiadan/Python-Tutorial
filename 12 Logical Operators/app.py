hasHighIncome = True
hasGoodCredit = True
hasCriminalRecord = False

if hasHighIncome and hasGoodCredit:
    print("Eligible for loan")

if hasHighIncome or hasGoodCredit:
    print("Eligible for loan")

if hasGoodCredit and not hasCriminalRecord:
    print("Eligible for loan")
