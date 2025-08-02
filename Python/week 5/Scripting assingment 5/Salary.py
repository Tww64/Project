def generate_salary_schedule():
    print("--- Teacher Salary Schedule Generator ---")

    while True:
        try:
            starting_salary = float(input("Enter the starting salary: $"))
            if starting_salary <= 0:
                print("Starting salary must be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the starting salary.")

    while True:
        try:
            percentage_increase = float(input("Enter the percentage increase (e.g., 2 for 2%): ")) / 100
            if percentage_increase < 0:
                print("Percentage increase cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the percentage increase.")

    while True:
        try:
            num_years = int(input("Enter the number of years in the schedule: "))
            if num_years <= 0:
                print("Number of years must be a positive integer. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the number of years.")

    print("\n--- Salary Schedule ---")
    print("{:<5} {:>15}".format("Year", "Salary"))
    print("-" * 22)

    current_salary = starting_salary
    for year in range(1, num_years + 1):
        print("{:<5} ${:>13.2f}".format(year, current_salary))
        current_salary *= (1 + percentage_increase)

if __name__ == "__main__":
    generate_salary_schedule()
