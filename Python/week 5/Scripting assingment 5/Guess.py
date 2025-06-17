import math

def computer_guesses_game():
    print("Think of a number, and I will try to guess it!")

    while True:
        try:
            smaller = int(input("Enter the smallest possible number: "))
            larger = int(input("Enter the largest possible number: "))
            if smaller >= larger:
                print("The 'smallest' number must be less than the 'largest' number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter integers for the range.")

    max_guesses = math.ceil(math.log2(larger - smaller + 1))
    print(f"\nI can guess your number in at most {max_guesses} tries.")

    count = 0
    low = smaller
    high = larger
    found = False

    while count < max_guesses:
        count += 1
        guess = (low + high) // 2

        print(f"\nMy guess is: {guess}")
        
        while True:
            hint = input("Is my guess (e)qual, (s)maller, or (l)arger than your number? (e/s/l): ").lower()
            if hint in ['e', 's', 'l']:
                break
            else:
                print("Invalid hint. Please enter 'e', 's', or 'l'.")

        if hint == 'e':
            found = True
            print(f"Hooray, I've got it in {count} tries!")
            break
        elif hint == 's':
            if guess <= low:
                print("I'm out of guesses, and you cheated!")
                print(f"Your number must be {guess} or greater, but you said it was smaller.")
                return
            high = guess - 1
        elif hint == 'l':
            if guess >= high:
                print("I'm out of guesses, and you cheated!")
                print(f"Your number must be {guess} or less, but you said it was larger.")
                return
            low = guess + 1
        
        if low > high:
            print("I'm out of guesses, and you cheated!")
            print("Your hints were inconsistent, causing the search range to become invalid.")
            return

    if not found:
        print("I'm out of guesses, and something went wrong or you cheated!")
        print(f"My last range was between {low} and {high}. Please ensure your hints were correct.")

if __name__ == "__main__":
    computer_guesses_game()
