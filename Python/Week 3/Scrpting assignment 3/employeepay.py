def calculate_weekly_pay(hourly_wage, regular_hours, overtime_hours):
   
    regular_pay = hourly_wage * regular_hours
    overtime_pay = overtime_hours * 1.5 * hourly_wage
    total_pay = regular_pay + overtime_pay
    return total_pay

if __name__ == "__main__":
    try:
        hourly_wage = float(input("Enter the hourly wage: "))
        regular_hours = float(input("Enter the total regular hours: "))
        overtime_hours = float(input("Enter the total overtime hours: "))

        total_weekly_pay = calculate_weekly_pay(hourly_wage, regular_hours, overtime_hours)

        print(f"An employee's total weekly pay is: ${total_weekly_pay:.2f}")

    except ValueError:
        print("Invalid input. Please enter numerical values for wage and hours.")
    except Exception as e:
        print(f"An error occurred: {e}")
