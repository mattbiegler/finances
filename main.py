# House Finances Calculator
# Written by Matt Biegler

downPayment = 40000
houseCost = 355000
houseAssessedValue = 258500
interestRate = 2.5
years = 15
months = years * 12
propertyTaxRate = 1.26
houseInsuranceRate = 0.66
pmiRate = 0.75
monthlyPayment = 3000

downPaymentPercentage = downPayment / houseCost * 100
mortgageAmount = houseCost - downPayment
propertyTaxes = houseAssessedValue * (propertyTaxRate / 100)
houseInsurance = houseCost * (houseInsuranceRate / 100)
if downPaymentPercentage >= 20:
    pmi = 0
else:
    pmi = mortgageAmount * (pmiRate / 100)
monthlyMortgagePayment = mortgageAmount * (((interestRate / 100 / 12) * (1 + (interestRate / 100 / 12)) ** months ) / ((1 + (interestRate / 100 / 12)) ** months - 1))


print('House Cost:\t\t$' + f"{houseCost:,.0f}")
print('House Assessed Value:\t$' + f"{houseAssessedValue:,.0f}")
print('Down Payment:\t\t$' + f"{downPayment:,.0f}" + ' (' + f"{downPaymentPercentage:,.2f}" + '%)')
print('Mortgage Amount:\t$' + f"{mortgageAmount:,.0f} (Total) | ${monthlyMortgagePayment:,.2f} (Monthly)")
print('Property Taxes:\t\t$' + f"{propertyTaxes:,.2f} (Annually) | ${propertyTaxes / 12:,.2f} (Monthly)")
print('House Insurance:\t$' + f"{houseInsurance:,.2f} (Annually) | ${houseInsurance / 12:,.2f} (Monthly)")
print('PMI:\t\t\t$' + f"{pmi:,.2f} (Annually) | ${pmi / 12:,.2f} (Monthly)\n")
print('Monthly Payment:\t$' + f"{monthlyMortgagePayment + propertyTaxes / 12 + houseInsurance / 12 + pmi / 12:,.2f}")
while 1:
    i = 0
