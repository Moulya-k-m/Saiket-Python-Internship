import requests

print("===== Currency Converter =====")

history = []

while True:
    from_currency = input("\nEnter currency you have (or type exit): ").upper()

    if from_currency == "EXIT":
        break

    to_currency = input("Enter currency you want: ").upper()

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Please enter an amount greater than 0.")
            continue

        url = f"https://open.er-api.com/v6/latest/{from_currency}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if data["result"] == "success":
                rates = data["rates"]

                if to_currency in rates:
                    rate = rates[to_currency]
                    converted_amount = amount * rate

                    print("\nExchange Rate:", rate)
                    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

                    history.append(
                        f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
                    )
                else:
                    print("Currency not found.")

            else:
                print("Unable to get exchange rates.")

        else:
            print("Error connecting to the API.")

    except ValueError:
        print("Please enter a valid number.")

print("\n===== Conversion History =====")

if history:
    for item in history:
        print(item)
else:
    print("No conversions made.")

print("\n Thank you for using the Currency Converter!")

