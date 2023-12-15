def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Please enter a number!")

def get_yes_or_no(prompt):
    while True:
        response = input(prompt).lower()
        if response == 'y' or response == 'n':
            return response
        else:
            print('Please answer "Y" or "N".')

def calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app):
    base_price_per_pizza = 12
    discount_on_tuesday = 0.5
    delivery_charge = 2.5
    app_discount = 0.25

    # Apply Tuesday discount
    if is_tuesday:
        base_price_per_pizza *= (1 - discount_on_tuesday)

    # Calculate total pizza cost
    total_pizza_cost = num_pizzas * base_price_per_pizza

    # Apply delivery charge if required
    if delivery_required and num_pizzas < 5:
        total_pizza_cost += delivery_charge

    # Apply app discount
    if used_app:
        total_pizza_cost *= (1 - app_discount)

    return round(total_pizza_cost, 2)

def main():
    print("BPP Pizza Price Calculator")
    print("==========================")

    try:
        num_pizzas = get_positive_integer("How many pizzas ordered? ")
        delivery_required = get_yes_or_no("Is delivery required? ") == 'y'
        is_tuesday = get_yes_or_no("Is it Tuesday? ") == 'y'
        used_app = get_yes_or_no("Did the customer use the app? ") == 'y'

        total_price = calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app)

        print(f"\nTotal Price: £{total_price:.2f}")
    except KeyboardInterrupt:
        print("\nProgram terminated by the user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
