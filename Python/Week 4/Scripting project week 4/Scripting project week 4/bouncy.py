def is_equilateral(side1, side2, side3):
  if side1 <= 0 or side2 <= 0 or side3 <= 0:
    return False, "Side lengths must be positive."

  if side1 == side2 == side3:
    return True, "The triangle is equilateral."
  else:
    return False, "The triangle is not equilateral."

if __name__ == "__main__":
  try:
    s1 = float(input("Enter the length of the first side: "))
    s2 = float(input("Enter the length of the second side: "))
    s3 = float(input("Enter the length of the third side: "))

    result, message = is_equilateral(s1, s2, s3)
    print(message)

  except ValueError:
    print("Invalid input. Please enter numeric values for side lengths.")
