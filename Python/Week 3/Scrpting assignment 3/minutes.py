

def calculate_minutes(years):
    
    days_in_year = 365.25  
    hours_in_day = 24
    minutes_in_hour = 60

    total_minutes = years * days_in_year * hours_in_day * minutes_in_hour
    return total_minutes

if __name__ == "__main__":
    try:
        num_years = float(input("Enter the number of years: "))
        if num_years < 0:
            print("Number of years cannot be negative.")
        else:
            minutes = calculate_minutes(num_years)
            print(f"There are {minutes} minutes in {num_years} years.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for years.")
