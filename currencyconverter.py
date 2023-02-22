def main():
    print("This program converts US dollars to UAH")
    print()

    dollars = eval(input("Enter amount in dollars: "))

    hryvnia = convert_to_uah(dollars)

    print("That is" , hryvnia, "hryvnia. ")

convert_to_uah = lambda dollars: dollars * 36.93

main()
