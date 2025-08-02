def calculate_bouncy_distance(initial_height, num_bounces):
  if initial_height <= 0 or num_bounces < 0:
    return 0, "Initial height must be positive and number of bounces non-negative."

  total_distance = initial_height
  bounce_height = initial_height * 0.6

  for _ in range(num_bounces):
    total_distance += bounce_height
    bounce_height *= 0.6
    total_distance += bounce_height

  return total_distance, "Total distance traveled by the ball: {:.2f} feet".format(total_distance)

if __name__ == "__main__":
  try:
    initial_h = float(input("Enter the initial height from which the ball is dropped (in feet): "))
    num_b = int(input("Enter the number of times the ball is allowed to bounce: "))

    total_dist, message = calculate_bouncy_distance(initial_h, num_b)
    print(message)

  except ValueError:
    print("Invalid input. Please enter numeric values for height and an integer for bounces.")
  except Exception as e:
    print(f"An error occurred: {e}")
