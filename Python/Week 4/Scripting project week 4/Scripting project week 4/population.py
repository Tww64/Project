def predict_population(initial_organisms, growth_rate, hours_to_achieve_rate, total_growth_hours):
  if initial_organisms <= 0 or growth_rate <= 0 or hours_to_achieve_rate <= 0 or total_growth_hours < 0:
    return "Invalid input: All parameters (except total_growth_hours if 0) must be positive."

  num_growth_periods = total_growth_hours / hours_to_achieve_rate
  final_population = initial_organisms * (growth_rate ** num_growth_periods)

  return int(final_population)

if __name__ == "__main__":
  try:
    initial_org = int(input("Enter the initial number of organisms: "))
    growth_r = float(input("Enter the growth rate (e.g., 2 for doubling): "))
    hours_achieve = float(input("Enter the number of hours it takes to achieve this rate: "))
    total_hours = float(input("Enter the total number of hours during which the population grows: "))

    predicted_pop = predict_population(initial_org, growth_r, hours_achieve, total_hours)

    if isinstance(predicted_pop, str):
      print(predicted_pop)
    else:
      print(f"Predicted total population: {predicted_pop} organisms")

  except ValueError:
    print("Invalid input. Please enter numeric values for all inputs, and integers for initial organisms.")
  except Exception as e:
    print(f"An error occurred: {e}")
