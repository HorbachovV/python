def main():
    print('This is a monthly loan calculator')
    print('')

    principal = float(input('Input the loan amount: '))
    apr = float(input('Input year percent rate: '))
    year = int(input('Input amount of years '))

    monthly_interst_rate = apr / 1200
    amount_of_months = year * 12
    monthly_payment = principal * monthly_interst_rate / (1 - (1 + monthly_interst_rate) ** (-amount_of_months))
    print(f'The monthly payment for this loan is: {round(monthly_payment, 2)}$')
    round
main()