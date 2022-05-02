# Ghana's E-Levy Charge Calculator.

eLevyPercentage = 1.50
taxLimit = 100.00

amount = int(input('Please enter the amount you want to send: '))

if (amount > taxLimit):
    eLevy = (eLevyPercentage / 100) * amount
else: 
    eLevy = 0.00 * amount
    
totalCharge = eLevy + amount

print('\n')
print(f'The E-Levy charge on GH₵{amount:.2f} is GH₵{eLevy:.2f}')
print(f'the total charge on your transaction is GH₵{totalCharge:.2f}, thank you.')

