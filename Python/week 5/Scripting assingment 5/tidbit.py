def generate_loan_schedule():
    print("--- TidBit Computer Store Loan Payment Schedule ---")

    while True:
        try:
            purchase_price = float(input("Enter the purchase price: $"))
            if purchase_price <= 0:
                print("Purchase price must be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the purchase price.")

    down_payment_rate = 0.10
    annual_interest_rate = 0.12
    monthly_payment_rate = 0.05

    down_payment = purchase_price * down_payment_rate
    loan_amount = purchase_price - down_payment

    fixed_monthly_payment = (purchase_price * monthly_payment_rate) - down_payment

    print(f"\nPurchase Price: ${purchase_price:,.2f}")
    print(f"Down Payment (10%): ${down_payment:,.2f}")
    print(f"Loan Amount: ${loan_amount:,.2f}")
    print(f"Calculated Monthly Payment: ${fixed_monthly_payment:,.2f}")

    print("\n--- Payment Schedule ---")
    print(f"{'Month':<7} {'Balance Owed':>15} {'Interest':>10} {'Principal':>12} {'Payment':>10} {'Remaining Balance':>18}")
    print("-" * 80)

    month_number = 1
    current_total_balance_owed = loan_amount

    while current_total_balance_owed > 0.01 and month_number < 1000:
        interest_owed = current_total_balance_owed * (annual_interest_rate / 12)
        
        if current_total_balance_owed + interest_owed <= fixed_monthly_payment:
            payment_for_month = current_total_balance_owed + interest_owed
            amount_of_principal_owed = current_total_balance_owed
        else:
            payment_for_month = fixed_monthly_payment
            amount_of_principal_owed = payment_for_month - interest_owed

        if amount_of_principal_owed < 0:
            amount_of_principal_owed = 0
            payment_for_month = interest_owed

        balance_remaining_after_payment = current_total_balance_owed - amount_of_principal_owed
        
        if balance_remaining_after_payment < 0:
            balance_remaining_after_payment = 0

        print(f"{month_number:<7} {current_total_balance_owed:>15.2f} {interest_owed:>10.2f} {amount_of_principal_owed:>12.2f} {payment_for_month:>10.2f} {balance_remaining_after_payment:>18.2f}")

        current_total_balance_owed = balance_remaining_after_payment
        month_number += 1
        
        if month_number >= 999:
            print("\nWarning: Loan potentially too long or payment too small. Breaking after 999 months.")
            break

    if current_total_balance_owed <= 0.01:
        print(f"\nLoan fully paid off in {month_number -1} months!")
    else:
        print("\nLoan not fully paid off. Remaining balance: $%.2f" % current_total_balance_owed)

if __name__ == "__main__":
    generate_loan_schedule()
